# Northbound Flows — 北向资金

Query northbound capital flows via Stock Connect (Shanghai-HK, Shenzhen-HK).

## Setup

```bash
pip install asharehub
export ASHAREHUB_API_KEY="your_key_here"
```

## Parameters

| Parameter | Required | Description | Example |
|-----------|----------|-------------|---------|
| `start_date` | No | Start date (YYYY-MM-DD) | `2024-01-01` |
| `end_date` | No | End date (YYYY-MM-DD) | `2024-03-31` |
| `limit` | No | Max rows (default 100, max 2000) | `200` |

## Code

```python
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
data = client.northbound_flows(start_date="2024-01-01", end_date="2024-03-31", limit=100)
for row in data:
    print(json.dumps(row.model_dump(mode="json"), ensure_ascii=False))
client.close()
```

## Response Fields

| Field | Description |
|-------|-------------|
| `trade_date` | Trading date |
| `hgt_ss`, `hgt_sz` | Shanghai/Shenzhen → HK northbound (millions CNY) |
| `ggt_ss`, `ggt_sz` | HK → Shanghai/Shenzhen southbound (millions CNY) |
| `north_money` | Total northbound net inflow (millions CNY) — positive = net buying |
| `south_money` | Total southbound net inflow (millions CNY) |

## Notes

- Data available from 2014-11-17, one record per trading day
- Positive `north_money` indicates foreign investors are net buying A-shares
- Key indicator of foreign investor sentiment toward Chinese markets
- Also available via MCP: `https://asharehub.com/mcp/sse` (tool: `get_northbound_flows`)
- Also available via REST API: `GET https://asharehub.com/v1/flows/northbound`
