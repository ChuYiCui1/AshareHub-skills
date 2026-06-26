# Stock List — A-Share Stock Reference

## SDK Method

```python
client.stock_list(symbol=None, name=None, market=None, list_status=None, exchange=None, is_hs=None)
```

## Returns

`pd.DataFrame` — columns: symbol, symbol, name, industry, list_date, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.stock_list(symbol="000001.SZ")
print(df[["symbol", "name", "industry", "list_date"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `name` | str | None | Stock name |
| `market` | str | None | Market: 主板/创业板/科创板/北交所/CDR |
| `list_status` | str | None | List status: L/D/P |
| `exchange` | str | None | Exchange: SSE/SZSE/BSE |
| `is_hs` | str | None | HSGT: N/H/S |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock ticker (e.g. 000001.SZ) |
| `symbol` | Ticker symbol (e.g. 000001) |
| `name` | Stock name (Chinese) |
| `area` | Province/city |
| `industry` | Industry |
| `fullname` | Full company name (Chinese) |
| `enname` | English company name |
| `cnspell` | Pinyin abbreviation |
| `market` | Market: 主板/创业板/科创板/北交所 |
| `exchange` | Exchange: SSE/SZSE/BSE |
| `curr_type` | Currency type |
| `list_status` | L=listed, D=delisted, P=paused |
| `list_date` | IPO date |
| `delist_date` | Delist date |
| `is_hs` | Stock Connect eligible: H/S/N |

## Data Coverage

- Static reference data
- API path: `GET /v2/reference/stocks`
