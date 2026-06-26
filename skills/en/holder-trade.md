# Holder Trade — Major Shareholder Trades

## SDK Method

```python
client.holder_trade(symbol=None, start_date=None, end_date=None, trade_type=None, holder_type=None)
```

## Returns

`pd.DataFrame` — columns: symbol, ann_date, holder_name, in_de, change_vol, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.holder_trade(symbol="000001.SZ")
print(df[["ann_date", "holder_name", "in_de", "change_vol"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_type` | str | None | IN=increase / DE=decrease |
| `holder_type` | str | None | C=company / P=person / G=executive |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `ann_date` | Announcement date |
| `holder_name` | Shareholder/executive name |
| `holder_type` | G=executive, P=individual, C=company |
| `in_de` | Direction: IN=buy, DE=sell |
| `change_vol` | Number of shares changed |
| `change_ratio` | Change as % of total shares |
| `after_share` | Shares held after change |
| `after_ratio` | Holding ratio after change % |
| `avg_price` | Average transaction price (CNY) |
| `total_share` | Total company shares |
| `begin_date` | Trade period start |
| `close_date` | Trade period end |

## Data Coverage

- From: 20191120
- Key signal for insider sentiment
- API path: `GET /v2/market/holder-trade`
