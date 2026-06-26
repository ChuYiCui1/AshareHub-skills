# Market Daily — Daily OHLC Prices

## SDK Method

```python
client.market_daily(symbol=None, start_date=None, end_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount. Returns empty DataFrame if no data.

## Example

```python
df = client.market_daily(symbol="000001.SZ", limit=3)
print(df[["trade_date", "close", "pct_chg"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` (Ping An Bank), `600519.SH` (Moutai) |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `trade_date` | Trading date |
| `open`, `high`, `low`, `close` | OHLC prices (CNY) |
| `pre_close` | Previous close (ex-dividend adjusted) |
| `change` | Price change (CNY) |
| `pct_chg` | Daily return % |
| `vol` | Volume in lots (1 lot = 100 shares) |
| `amount` | Turnover in thousands of CNY |

## Data Coverage

- From: 20200102
- API path: `GET /v2/market/daily`
