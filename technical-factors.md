# Technical Factors — Indicators & Adjusted Prices

## SDK Method

```python
client.technical_factors(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, close_qfq, macd, kdj_k, rsi_6, boll_upper/mid/lower, cci, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.technical_factors(symbol="000001.SZ")
print(df[["trade_date", "close_qfq", "macd", "kdj_k", "rsi_6"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |

## Response Fields

| Category | Fields |
|----------|--------|
| **Backward adjusted (hfq)** | `open_hfq`, `close_hfq`, `high_hfq`, `low_hfq`, `pre_close_hfq` |
| **Forward adjusted (qfq)** | `open_qfq`, `close_qfq`, `high_qfq`, `low_qfq`, `pre_close_qfq` |
| **MACD** | `macd_dif`, `macd_dea`, `macd` |
| **KDJ** | `kdj_k`, `kdj_d`, `kdj_j` |
| **RSI** | `rsi_6`, `rsi_12`, `rsi_24` |
| **Bollinger Bands** | `boll_upper`, `boll_mid`, `boll_lower` |
| **CCI** | `cci` |

## Notes

- qfq = forward adjusted (前复权), hfq = backward adjusted (后复权)
- API path: `GET /v2/market/technical-factors`
