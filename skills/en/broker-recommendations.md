# Broker monthly stock picks

Each row is a recommendation for one month, broker and stock. These monthly stock picks are distinct from `analyst_reports`, which provides earnings forecasts.

Filter by `month` (YYYYMM), exact `broker`, or `symbol`. Omit month to query all stored months. Defaults: `limit=100`, `offset=0`; maximum limit 1000. Order: month descending, broker ascending, symbol ascending. Advance offset until a page has fewer than limit rows. Invalid months and bare stock codes return 422. V2 only. Recommendation records are source data and do not imply future returns.

## Point-in-time limitations

Neither dataset exposes a reliable public release timestamp. `month` labels a recommendation month; `surv_date` records the meeting date, not when its transcript became public. Do not use either date alone for strict point-in-time backtests: doing so can introduce look-ahead bias. Such backtests require independently verified publication/availability timestamps and historical source versions.

## Example

```python
offset = 0
while True:
    page = client.broker_recommendations(month="202611", limit=100, offset=offset)
    print(page)
    if len(page) < 100:
        break
    offset += len(page)
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_broker_recommendations`.
