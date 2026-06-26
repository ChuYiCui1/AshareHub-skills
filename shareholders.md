# Shareholders — Shareholder Count

## SDK Method

```python
client.shareholders(symbol=None, start_date=None, end_date=None, enddate=None, ann_date=None)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, end_date, holder_num. Returns empty DataFrame if no data.

## Example

```python
df = client.shareholders(symbol="000001.SZ")
print(df[["end_date", "holder_num"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Report period start, YYYYMMDD |
| `end_date` | str | None | Report period end, YYYYMMDD |
| `enddate` | str | None | Stat cutoff date YYYYMMDD |
| `ann_date` | str | None | Announcement date YYYYMMDD |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `ann_date` | Announcement date |
| `end_date` | Report period end date |
| `holder_num` | Number of shareholders |

## Data Coverage

- From: 20240401
- Quarterly reports. Declining count = chip concentration (accumulation by large holders)
- API path: `GET /v2/market/shareholders`
