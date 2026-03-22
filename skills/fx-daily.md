# FX Daily — 外汇日线

Query daily FX rates with bid/ask prices. Default pair: USD/CNH (offshore RMB).

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `ts_code` | No | FX pair code (default `USDCNH.FXCM`) | `USDCNH.FXCM` |
| `start_date` | No | Start date (YYYY-MM-DD) | `2024-01-01` |
| `end_date` | No | End date (YYYY-MM-DD) | `2024-12-31` |
| `limit` | No | Max rows (default 100, max 2000) | `200` |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.fx_daily(ts_code="USDCNH.FXCM", start_date="2024-01-01", end_date="2024-12-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code` | FX pair code |
| `trade_date` | Trading date |
| `bid_open`, `bid_close`, `bid_high`, `bid_low` | Bid prices |
| `ask_open`, `ask_close`, `ask_high`, `ask_low` | Ask prices |
| `tick_qty` | Number of quote ticks |

## Notes

- Data available from 2012-01-01
- Rising USDCNH = CNY weakening, typically pressures A-share foreign inflows
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_fx_daily`)
- Also available via REST API: `GET https://asharehub.com/v1/fx/daily`
