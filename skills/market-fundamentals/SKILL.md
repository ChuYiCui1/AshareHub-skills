# Market Fundamentals — A股每日估值指标

Query daily valuation metrics: PE, PB, turnover rate, market cap.

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `ts_code` | No | Stock code | `000001.SZ` |
| `start_date` | No | Start date (YYYY-MM-DD) | `2024-01-01` |
| `end_date` | No | End date (YYYY-MM-DD) | `2024-12-31` |
| `limit` | No | Max rows (default 100, max 5000) | `500` |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.fundamentals(ts_code="000001.SZ", start_date="2024-01-01", end_date="2024-12-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code`, `trade_date` | Stock code and date |
| `close` | Closing price |
| `turnover_rate`, `turnover_rate_f` | Turnover rates % |
| `volume_ratio` | Volume ratio (today avg / 5-day avg) |
| `pe`, `pe_ttm` | P/E ratios |
| `pb` | Price-to-Book ratio |
| `ps`, `ps_ttm` | Price-to-Sales ratios |
| `dv_ratio`, `dv_ttm` | Dividend yields % |
| `total_share`, `float_share`, `free_share` | Share counts (10k shares) |
| `total_mv`, `circ_mv` | Market caps (10k CNY) |

## Notes

- Data available from 2010-01-04, 13.6M+ records (most complete dataset)
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_market_fundamentals`)
- Also available via REST API: `GET https://asharehub.com/v1/market/fundamentals`
