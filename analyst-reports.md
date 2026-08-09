# Analyst Reports — Sell-Side Earnings Forecasts

## SDK Method

```python
client.analyst_reports(symbol=None, start_date=None, end_date=None)
```

## Returns

`pd.DataFrame` — 23 columns. Numeric fields are `float64`. Returns empty DataFrame if no data.

## Example

```python
df = client.analyst_reports(symbol="600519.SH")
print(df[["report_date", "org_name", "rating", "max_price", "eps"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Report start date, YYYYMMDD |
| `end_date` | str | None | Report end date, YYYYMMDD |

## Key Response Fields

For the exact complete field list, use `api-contract.md`.

symbol, name, report_date, report_title, org_name (brokerage), author_name, quarter (forecast period), op_rt/op_pr/tp/np (revenue/profit forecasts), eps, pe, roe, ev_ebitda, rating (buy/hold/sell), max_price, min_price, imp_dg.

## Data Coverage

- From: 2010+
- Useful for tracking analyst consensus and price targets
- API path: `GET /v2/financials/analyst-reports`
