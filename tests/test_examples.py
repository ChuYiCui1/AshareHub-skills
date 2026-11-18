"""Execute the shipped Markdown examples with real DataFrames and no network."""
import ast
from contextlib import redirect_stdout
import io
import inspect
from pathlib import Path
import re
from unittest.mock import patch

import pandas as pd
import pytest

from asharehub import AShareHub as SDKClient, PUBLIC_CONTRACT

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = [
    pytest.param(path, index, code, id=f'{path.relative_to(ROOT)}:{index}')
    for path in sorted(ROOT.rglob('*.md'))
    if '.git' not in path.parts
    for index, code in enumerate(re.findall(r'```python\s*\n(.*?)```', path.read_text(), re.S))
]


class ExampleClient:
    def __init__(self, mode='nonempty', empty_methods=(), disjoint=False):
        self.mode = mode
        self.empty_methods = empty_methods
        self.disjoint = disjoint
        self.closed = False

    def close(self):
        self.closed = True

    def __getattr__(self, method):
        entry = PUBLIC_CONTRACT['interfaces'][method]
        def fetch(*args, **params):
            bound = inspect.signature(getattr(SDKClient, method)).bind(None, *args, **params)
            params = {key: value for key, value in bound.arguments.items() if key != "self"}
            fields = entry['response_fields']
            if self.mode == 'empty' or method in self.empty_methods:
                return pd.DataFrame()  # Matches the SDK's columnless empty result.
            if self.mode == 'empty_with_columns':
                return pd.DataFrame(columns=fields)
            rows = []
            for index, day in enumerate(['20240103', '20240102']):
                row = {field: 1.0 for field in fields}
                for field in fields:
                    if field.endswith('date'):
                        row[field] = day
                if 'symbol' in fields:
                    row['symbol'] = params.get('symbol') or '000001.SZ'
                if 'event_id' in fields:
                    row['event_id'] = 'a' * 64
                if 'month' in fields:
                    row['month'] = params.get('month') or '202611'
                if method == 'market_daily':
                    row['close'] = [30.0, 20.0][index]
                if method == 'adj_factor':
                    row['adj_factor'] = [3.0, 2.0][index]
                    if self.disjoint:
                        row['trade_date'] = ['20240203', '20240202'][index]
                rows.append(row)
            return pd.DataFrame(rows, columns=fields)
        return fetch


def execute(code, client):
    scope = {'client': client, 'source': 'cls'}  # news_flash signature placeholder
    output = io.StringIO()
    with patch.dict('os.environ', {'ASHAREHUB_API_KEY': 'example-test'}), \
         patch('asharehub.AShareHub', return_value=client), redirect_stdout(output):
        exec(compile(code, '<skill-example>', 'exec'), scope)
    return scope, output.getvalue()


@pytest.mark.parametrize('path,index,code', BLOCKS)
@pytest.mark.parametrize('mode', ['empty', 'empty_with_columns', 'nonempty'])
def test_shipped_python_examples(path, index, code, mode):
    scope, output = execute(code, ExampleClient(mode))
    tree = ast.parse(code)
    column_selection = any(
        isinstance(node, ast.Subscript) and isinstance(node.slice, ast.List)
        for node in ast.walk(tree)
    )
    if column_selection:
        if mode.startswith('empty'):
            assert 'No matching data' in output or '没有符合条件的数据' in output
        else:
            assert not scope['df'].empty
            assert 'No matching data' not in output and '没有符合条件的数据' not in output
            assert str(scope['df'].index[0]) in output


ADJUSTMENT_EXAMPLES = [
    pytest.param(path, code, id=str(path.relative_to(ROOT)))
    for path in [ROOT / 'adj-factor.md', ROOT / 'skills/en/adj-factor.md', ROOT / 'skills/zh/adj-factor.md']
    for code in re.findall(r'```python\s*\n(.*?)```', path.read_text(), re.S)
    if 'daily.merge' in code
]


@pytest.mark.parametrize('path,code', ADJUSTMENT_EXAMPLES)
@pytest.mark.parametrize('empty_methods', [('market_daily',), ('adj_factor',), ('market_daily', 'adj_factor')])
def test_adjustment_handles_one_missing_input(path, code, empty_methods):
    scope, output = execute(code, ExampleClient(empty_methods=empty_methods))
    assert 'close_qfq' not in scope.get('df', pd.DataFrame()).columns
    assert 'cannot be calculated' in output or '无法计算' in output


@pytest.mark.parametrize('path,code', ADJUSTMENT_EXAMPLES)
def test_adjustment_handles_non_overlapping_dates(path, code):
    scope, output = execute(code, ExampleClient(disjoint=True))
    assert scope['df'].empty
    assert 'No matching trading dates' in output or '没有匹配的交易日' in output


@pytest.mark.parametrize('path,code', ADJUSTMENT_EXAMPLES)
def test_adjustment_keeps_nonempty_price_calculation(path, code):
    scope, _ = execute(code, ExampleClient())
    frame = scope['df'].sort_values('trade_date')
    assert scope['anchor_factor'] == 3.0  # Most recent date, not last returned row.
    assert frame['close_qfq'].tolist() == pytest.approx([20 * 2 / 3, 30])
    assert frame['close_hfq'].tolist() == pytest.approx([40, 90])
