# Chip Distribution — 筹码分布

Query chip distribution (cost basis and winner rate) data for A-share stocks.

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
data = client.chip_distribution(ts_code="000001.SZ", start_date="2024-01-01", end_date="2024-12-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code`, `trade_date` | Stock code and date |
| `his_low`, `his_high` | Historical price extremes (CNY) |
| `cost_5pct`, `cost_15pct`, `cost_50pct`, `cost_85pct`, `cost_95pct` | Cost basis percentiles (CNY) |
| `weight_avg` | Weighted average cost of all holders (CNY) |
| `winner_rate` | % of holders in profit (0-100) |

## Notes

- Data available from 2020-01-02, 7.3M+ records
- `winner_rate` > 80 typically suggests strong bullish momentum
- Chinese market-specific metric for analyzing shareholder cost structure
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_chip_distribution`)
- Also available via REST API: `GET https://asharehub.com/v1/chips/distribution`
