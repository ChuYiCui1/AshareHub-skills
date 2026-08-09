# Dividend — Cash & Stock Distribution

## SDK Method

```python
client.dividend(symbol=None, start_date=None, end_date=None, record_date=None, ex_date=None, imp_ann_date=None)
```

## Returns

`pd.DataFrame` — columns: symbol, end_date, ann_date, cash_div, stk_div, ex_date, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.dividend(symbol="000001.SZ")
print(df[["end_date", "cash_div", "stk_div", "ex_date"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Announcement start date, YYYYMMDD |
| `end_date` | str | None | Announcement end date, YYYYMMDD |
| `record_date` | str | None | Record date YYYYMMDD |
| `ex_date` | str | None | Ex-dividend date YYYYMMDD |
| `imp_ann_date` | str | None | Implementation announcement date YYYYMMDD |

## Key Response Fields

For the exact complete field list, use `api-contract.md`.

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `end_date` | Dividend fiscal year end |
| `ann_date` | Plan announcement date |
| `div_proc` | Progress: 预案/董事会预案/股东大会/实施 |
| `cash_div` | Cash dividend per share pre-tax (CNY) |
| `cash_div_tax` | Cash dividend per share after-tax (CNY) |
| `stk_div` | Total stock dividend per share |
| `stk_bo_rate` | Bonus share rate per share |
| `stk_co_rate` | Share conversion rate per share |
| `record_date` | Record date (股权登记日) |
| `ex_date` | Ex-dividend date (除权除息日) |
| `pay_date` | Payment date |
| `div_listdate` | Stock-dividend listing date |
| `imp_ann_date` | Implementation announcement date |

## Notes

- Buy before `ex_date` to qualify for dividend
- API path: `GET /v2/shareholders/dividend`
