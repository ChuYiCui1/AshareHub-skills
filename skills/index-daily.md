# Index Daily — 指数日线

Query daily OHLC data for major Chinese market indices.

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `ts_code` | No | Index code (default `000001.SH`) | `000300.SH` |
| `start_date` | No | Start date (YYYY-MM-DD) | `2024-01-01` |
| `end_date` | No | End date (YYYY-MM-DD) | `2024-12-31` |
| `limit` | No | Max rows (default 100, max 2000) | `200` |

## Common Index Codes

| Code | Name |
|------|------|
| `000001.SH` | SSE Composite (上证综指) |
| `000300.SH` | CSI 300 (沪深300) |
| `399001.SZ` | SZSE Component (深证成指) |
| `399006.SZ` | ChiNext (创业板指) |
| `000016.SH` | SSE 50 (上证50) |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.index_daily(ts_code="000300.SH", start_date="2024-01-01", end_date="2024-12-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code` | Index code |
| `trade_date` | Trading date |
| `open`, `high`, `low`, `close` | Index level |
| `pre_close` | Previous close |
| `change` | Point change |
| `pct_chg` | Daily return % |
| `vol` | Volume in lots |
| `amount` | Turnover in thousands of CNY |

## Notes

- Data available from 2010-01-04
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_index_daily`)
- Also available via REST API: `GET https://asharehub.com/v1/indices/daily`
