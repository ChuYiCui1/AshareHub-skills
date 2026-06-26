# Adjustment Factor — Forward/Backward Price Restoration

## SDK Method

```python
client.adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, adj_factor. Returns empty DataFrame if no data.

## Example

```python
df = client.adj_factor(symbol="000001.SZ", limit=3)
print(df[["trade_date", "adj_factor"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `trade_date` | Trading date |
| `adj_factor` | Adjustment factor |

## Notes

- Forward adjusted price = unadjusted price * adj_factor / latest adj_factor
- Backward adjusted price = unadjusted price * adj_factor
- API path: `GET /v2/market/adj-factor`
