# Index Daily — Major Market Indices

## SDK Method

```python
client.index_daily(symbol="000001.SH", start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, open, high, low, close, pct_chg, vol, amount. Returns empty DataFrame if no data.

## Example

```python
df = client.index_daily(symbol="000001.SH", limit=3)
print(df[["trade_date", "close", "pct_chg"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | `000001.SH` | Index code |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |
| `limit` | int | 100 | Max rows, up to 2000 |
| `offset` | int | 0 | Pagination offset |

## Common Index Codes

| Code | Name |
|------|------|
| `000001.SH` | SSE Composite |
| `000300.SH` | CSI 300 |
| `399001.SZ` | SZSE Component |
| `399006.SZ` | ChiNext |
| `000016.SH` | SSE 50 |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Index code |
| `trade_date` | Trading date |
| `open`, `high`, `low`, `close` | Index level |
| `pre_close` | Previous close |
| `change` | Point change |
| `pct_chg` | Daily return % |
| `vol` | Volume in lots |
| `amount` | Turnover in thousands of CNY |

## Data Coverage

- From: 20100104
- API path: `GET /v2/indices/daily`
