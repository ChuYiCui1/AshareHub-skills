# Financial Indicators — Quarterly Financials

## SDK Method

```python
client.financial_indicators(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, end_date, roe, eps, netprofit_margin, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.financial_indicators(symbol="000001.SZ")
print(df[["end_date", "roe", "eps", "netprofit_margin"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Report period start, YYYYMMDD |
| `end_date` | str | None | Report period end, YYYYMMDD |
| `period` | str | None | Report period YYYYMMDD, e.g. 20231231 |
| `ann_date` | str | None | Announcement date YYYYMMDD |

## Response Fields

| Category | Fields |
|----------|--------|
| **Per-share** | `eps`, `dt_eps`, `total_revenue_ps`, `revenue_ps`, `bps`, `ocfps` |
| **Profitability** | `roe`, `roe_waa`, `roe_dt`, `roa`, `gross_margin`, `netprofit_margin`, `grossprofit_margin` |
| **Leverage** | `debt_to_assets` |
| **Liquidity** | `current_ratio`, `quick_ratio`, `cash_ratio` |
| **Efficiency** | `assets_turn`, `inv_turn`, `ar_turn` |
| **Returns** | `roic` |
| **Growth** | `basic_eps_yoy`, `dt_eps_yoy`, `netprofit_yoy`, `dt_netprofit_yoy` |
| **R&D** | `rd_exp` (CNY) |
| **Dates** | `ann_date` (announcement date), `end_date` (fiscal period end) |

## Data Coverage

- `end_date` refers to fiscal period end (e.g. `20241231` = annual, `20240630` = semi-annual)
- API path: `GET /v2/financials/indicators`
