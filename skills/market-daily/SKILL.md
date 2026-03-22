# Market Daily — A股日线行情

Query daily OHLC price data for A-share stocks.

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"  # Get free key at asharehub.com/console/register
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `ts_code` | No | Stock code | `000001.SZ` (Ping An Bank), `600519.SH` (Moutai) |
| `start_date` | No | Start date (YYYY-MM-DD) | `2024-01-01` |
| `end_date` | No | End date (YYYY-MM-DD) | `2024-12-31` |
| `limit` | No | Max rows (default 100, max 5000) | `500` |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.market_daily(ts_code="000001.SZ", start_date="2024-01-01", end_date="2024-12-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code` | Stock code |
| `trade_date` | Trading date |
| `open`, `high`, `low`, `close` | OHLC prices (CNY) |
| `pre_close` | Previous close (ex-dividend adjusted) |
| `change` | Price change (CNY) |
| `pct_chg` | Daily return % |
| `vol` | Volume in lots (1 lot = 100 shares) |
| `amount` | Turnover in thousands of CNY |

## Notes

- Data available from 2020-01-02, 7.3M+ records
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_market_daily`)
- Also available via REST API: `GET https://asharehub.com/v1/market/daily`
