# Technical Factors Pro — Professional Indicators (200+)

## SDK Method

```python
client.technical_factors_pro(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## Returns

`pd.DataFrame` — 200+ columns. Numeric fields are `float64`. Returns empty DataFrame if no data.

## Example

```python
df = client.technical_factors_pro(symbol="000001.SZ")
print(df[["trade_date", "close_qfq", "macd_qfq", "rsi_qfq_6", "ma_qfq_20"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |

## Response Fields

200+ columns: OHLCV, valuation (PE/PB/PS/MV), and technical indicators (MA, EMA, MACD, KDJ, RSI, BOLL, CCI, ATR, BBI, BIAS, BRAR, CR, DFMA, DMI, DPO, EMV, EXPMA, Keltner, MASS, MFI, MTM, OBV, PSY, ROC, TRIX, VR, W&R, ASI, TAQ, XSII). Each technical indicator has `_bfq` (unadjusted), `_qfq` (forward-adjusted), `_hfq` (backward-adjusted) variants.

## Data Coverage

- From: 20200102
- API path: `GET /v2/market/technical-factors-pro`
