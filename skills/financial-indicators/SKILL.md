# Financial Indicators — 财务指标

Query quarterly financial indicators: ROE, EPS, margins, ratios (50+ metrics).

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `ts_code` | No | Stock code | `000001.SZ` |
| `start_date` | No | Report period start (YYYY-MM-DD) | `2023-01-01` |
| `end_date` | No | Report period end (YYYY-MM-DD) | `2024-12-31` |
| `limit` | No | Max rows (default 20, max 200) | `50` |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.financial_indicators(ts_code="000001.SZ", start_date="2023-01-01", end_date="2024-12-31", limit=20)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Category | Fields |
|----------|--------|
| **Per-share** | `eps`, `dt_eps`, `total_revenue_ps`, `revenue_ps`, `bps`, `ocfps` |
| **Profitability** | `roe`, `roe_waa`, `roe_dt`, `roa`, `gross_margin`, `netprofit_margin` |
| **Leverage** | `debt_to_assets` |
| **Liquidity** | `current_ratio`, `quick_ratio`, `cash_ratio` |
| **Efficiency** | `assets_turn`, `inv_turn`, `ar_turn` |
| **Returns** | `roic` |
| **Growth** | `basic_eps_yoy`, `dt_eps_yoy`, `netprofit_yoy`, `dt_netprofit_yoy` |
| **R&D** | `rd_exp` (CNY) |
| **Dates** | `ann_date` (announcement), `end_date` (fiscal period) |

## Notes

- `end_date` refers to fiscal period end (e.g. `2024-12-31` = annual report, `2024-06-30` = semi-annual)
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_financial_indicators`)
- Also available via REST API: `GET https://asharehub.com/v1/financials/indicators`
