# Disclosure Dates — Financial Report Schedule

## SDK Method

```python
client.disclosure_date(symbol=None, start_date=None, end_date=None, pre_date=None, actual_date=None)
```

## Returns

`pd.DataFrame` — 6 columns. Returns empty DataFrame if no data.

## Example

```python
df = client.disclosure_date(symbol="000001.SZ")
print(df[["end_date", "pre_date", "actual_date"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code |
| `start_date` | str | None | Period start YYYYMMDD |
| `end_date` | str | None | Period end YYYYMMDD |
| `pre_date` | str | None | Planned disclosure date YYYYMMDD |
| `actual_date` | str | None | Actual disclosure date YYYYMMDD |

## Response Fields

symbol, ann_date (latest announcement), end_date (fiscal period), pre_date (planned date), actual_date (actual disclosure), modify_date.

## Data Coverage

- From: 20010206
- Use to track when companies will release earnings
- API path: `GET /v2/financials/disclosure-date`
