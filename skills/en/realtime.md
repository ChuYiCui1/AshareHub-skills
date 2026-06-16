# Realtime — Real-time Quote Snapshot

## SDK Method

```python
client.realtime(ts_code=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: ts_code, name, price, open, high, low, pre_close, pct_chg, volume, amount, trade_time, updated_at. Returns empty DataFrame if no data.

## Example

```python
# A basket of securities in one call (comma-separated ts_code, up to 200)
df = client.realtime(ts_code="600519.SH,000001.SZ,000001.SH")
print(df[["ts_code", "name", "price", "pct_chg"]])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| ts_code | str | No | Ticker, or comma-separated basket (up to 200), e.g. `600519.SH,000001.SZ`. Omit to page through the whole market. |
| limit | int | No | Max rows (default 100, max 5000) |
| offset | int | No | Pagination offset (default 0) |

## Response Fields

| Field | Description |
|-------|-------------|
| ts_code | Stock / index ticker |
| name | Security name |
| price | Latest traded price |
| open / high / low | Intraday open / high / low |
| pre_close | Previous close |
| pct_chg | Percent change vs previous close (%) |
| volume | Cumulative volume (shares) |
| amount | Cumulative turnover (CNY) |
| trade_time | Quote timestamp from the source |
| updated_at | Last refresh time into AShareHub |

## Notes

- One row per security, continuously refreshed during trading hours — an intraday snapshot, not a time series.
- Outside trading hours it returns the last session's closing snapshot.
- For historical daily bars use `client.market_daily()`; for intraday technical indicators see `client.technical_factors()`.
