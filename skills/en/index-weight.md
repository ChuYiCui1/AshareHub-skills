# Index Weight — Constituent Weights

## SDK Method

```python
client.index_weight(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, con_symbol, con_name, weight. Returns empty DataFrame if no data.

## Example

```python
df = client.index_weight(symbol="399300.SZ", limit=5)
print(df[["con_symbol", "con_name", "weight"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Index code, e.g. `399300.SZ` (CSI 300) |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Index code |
| `trade_date` | Effective date |
| `con_symbol` | Constituent stock code |
| `con_name` | Constituent stock name |
| `weight` | Weight in index % |

## Common Index Codes

| Code | Name |
|------|------|
| `399300.SZ` | CSI 300 |
| `000905.SH` | CSI 500 |
| `000016.SH` | SSE 50 |

## Notes

- Rebalanced periodically (semi-annual for major indices)
- API path: `GET /v2/indices/index-weight`
