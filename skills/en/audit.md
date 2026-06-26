# Audit Opinions — Annual Report Audit Results

## SDK Method

```python
client.audit(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, limit=50, offset=0)
```

## Returns

`pd.DataFrame` — 7 columns. Returns empty DataFrame if no data.

## Example

```python
df = client.audit(symbol="000001.SZ", limit=3)
print(df[["end_date", "audit_result", "audit_agency", "audit_fees"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code |
| `start_date` | str | None | Period start YYYYMMDD |
| `end_date` | str | None | Period end YYYYMMDD |
| `period` | str | None | Report period YYYYMMDD, e.g. 20231231 |
| `ann_date` | str | None | Announcement date YYYYMMDD |
| `limit` | int | 50 | Max rows, up to 1000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

symbol, ann_date, end_date, audit_result (opinion type), audit_fees, audit_agency (firm name), audit_sign (signing auditors).

## Data Coverage

- From: 20060420
- Annual data only (released with annual reports)
- API path: `GET /v2/financials/audit`
