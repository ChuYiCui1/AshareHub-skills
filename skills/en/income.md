# Income Statement

## SDK Method

```python
client.income(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None, limit=20, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, end_date, revenue, n_income, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.income(symbol="000001.SZ", limit=3)
print(df[["end_date", "revenue", "n_income"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Report period start, YYYYMMDD |
| `end_date` | str | None | Report period end, YYYYMMDD |
| `period` | str | None | Report period YYYYMMDD, e.g. 20231231 |
| `ann_date` | str | None | Announcement date YYYYMMDD |
| `f_ann_date` | str | None | Actual announcement date YYYYMMDD |
| `report_type` | str | None | Report type |
| `comp_type` | str | None | Company type: 1 general / 2 bank / 3 insurance / 4 securities |
| `limit` | int | 20 | Max rows, up to 200 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Category | Fields |
|----------|--------|
| **Revenue** | `total_revenue`, `revenue` |
| **Costs** | `total_cogs`, `oper_cost`, `sell_exp`, `admin_exp`, `fin_exp`, `rd_exp` |
| **Profit** | `operate_profit`, `total_profit`, `n_income`, `n_income_attr_p` |
| **Non-operating** | `non_oper_income`, `non_oper_exp` |
| **Per-share** | `basic_eps`, `diluted_eps` |
| **Other** | `income_tax`, `ebit`, `ebitda` |
| **Dates** | `ann_date`, `f_ann_date`, `end_date` |
| **Meta** | `report_type`, `comp_type`, `update_flag` |

## Notes

- All monetary values in CNY
- `end_date` = fiscal period (e.g. 20241231 for annual, 20240630 for H1)
- API path: `GET /v2/financials/income`
