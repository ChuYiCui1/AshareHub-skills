# Balance Sheet

## SDK Method

```python
client.balance_sheet(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, report_type=None, comp_type=None)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, end_date, total_assets, total_liab, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.balance_sheet(symbol="000001.SZ")
print(df[["end_date", "total_assets", "total_liab"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Report period start, YYYYMMDD |
| `end_date` | str | None | Report period end, YYYYMMDD |
| `period` | str | None | Report period YYYYMMDD, e.g. 20231231 |
| `ann_date` | str | None | Announcement date YYYYMMDD |
| `report_type` | str | None | Report type |
| `comp_type` | str | None | Company type: 1 general / 2 bank / 3 insurance / 4 securities |

## Response Fields

| Category | Fields |
|----------|--------|
| **Current assets** | `total_cur_assets`, `money_cap`, `notes_receiv`, `accounts_receiv`, `inventories` |
| **Non-current assets** | `total_nca`, `lt_eqt_invest`, `fix_assets`, `cip`, `intan_assets`, `goodwill` |
| **Total** | `total_assets` |
| **Current liabilities** | `total_cur_liab`, `st_borr`, `notes_payable`, `acct_payable` |
| **Non-current liabilities** | `total_ncl`, `lt_borr`, `bond_payable` |
| **Total liabilities** | `total_liab` |
| **Equity** | `total_hldr_eqy_exc_min_int`, `total_hldr_eqy_inc_min_int`, `minority_int` |

## Notes

- All monetary values in CNY
- API path: `GET /v2/financials/balance-sheet`
