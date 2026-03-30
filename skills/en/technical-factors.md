# Technical Factors — Indicators & Adjusted Prices

## SDK Method

```python
client.technical_factors(ts_code=None, start_date=None, end_date=None, limit=100, offset=0)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ts_code` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYY-MM-DD |
| `end_date` | str | None | End date, YYYY-MM-DD |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

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
- API path: `GET /v1/market/technical-factors`
