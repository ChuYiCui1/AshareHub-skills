# Earnings Forecast — Profit Warnings

## SDK Method

```python
client.forecast(symbol=None, start_date=None, end_date=None, limit=50, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, end_date, type, net_profit_min, net_profit_max, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.forecast(symbol="000001.SZ", limit=3)
print(df[["ann_date", "end_date", "type", "net_profit_min", "net_profit_max"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Announcement start date, YYYYMMDD |
| `end_date` | str | None | Announcement end date, YYYYMMDD |
| `limit` | int | 50 | Max rows, up to 1000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `ann_date` | Announcement date |
| `end_date` | Fiscal period end |
| `type` | Forecast type (see below) |
| `p_change_min` / `p_change_max` | Net profit change range % |
| `net_profit_min` / `net_profit_max` | Forecast net profit range (10k CNY) |
| `last_parent_net` | Prior year net income (10k CNY) |
| `summary` | Performance summary |
| `change_reason` | Reason for change |

## Forecast Types

| Chinese | English |
|---------|---------|
| 预增 | Significant increase |
| 预减 | Significant decrease |
| 扭亏 | Turnaround to profit |
| 首亏 | First-time loss |
| 续亏 | Continued loss |
| 续盈 | Continued profit |
| 略增 | Slight increase |
| 略减 | Slight decrease |

## Notes

- API path: `GET /v2/financials/forecast`
