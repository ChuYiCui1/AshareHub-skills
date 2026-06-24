# Realtime — Real-time Quote Snapshot

## SDK Method

```python
client.realtime(symbol=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, name, price, open, high, low, pre_close, pct_chg, volume, amount, trade_time. Returns empty DataFrame if no data.

## Example

```python
# A basket of securities in one call (comma-separated symbol, up to 200)
df = client.realtime(symbol="600519.SH,000001.SZ,000001.SH")
print(df[["symbol", "name", "price", "pct_chg"]])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| symbol | str | No | Ticker, or comma-separated basket (up to 200), e.g. `600519.SH,000001.SZ`. Omit to page through the whole market. |
| limit | int | No | Max rows (default 100, max 5000) |
| offset | int | No | Pagination offset (default 0) |

## Response Fields

| Field | Description |
|-------|-------------|
| symbol | Stock / index ticker |
| name | Security name |
| price | Latest traded price |
| open / high / low | Intraday open / high / low |
| pre_close | Previous close |
| pct_chg | Percent change vs previous close (%) |
| volume | Cumulative volume (shares) |
| amount | Cumulative turnover (CNY) |
| trade_time | Quote timestamp from the source |

## Notes

- One row per security, continuously refreshed during trading hours — an intraday snapshot, not a time series.
- Outside trading hours it returns the last session's closing snapshot.
- For historical daily bars use `client.market_daily()`; for intraday technical indicators see `client.technical_factors()`.
