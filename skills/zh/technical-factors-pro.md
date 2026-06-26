# 技术因子专业版 — 200+ 指标

## SDK 方法

```python
client.technical_factors_pro(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## 返回类型

`pd.DataFrame` — 200+ 列，数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.technical_factors_pro(symbol="000001.SZ", limit=1)
print(df[["trade_date", "close_qfq", "macd_qfq", "rsi_qfq_6", "ma_qfq_20"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ` |
| `start_date` | str | None | 起始日期 YYYYMMDD |
| `end_date` | str | None | 结束日期 YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |
| `limit` | int | 100 | 返回行数，最大 5000 |
| `offset` | int | 0 | 分页偏移量 |

## 返回字段

200+ 列：OHLCV、估值指标(PE/PB/PS/市值)、以及技术指标(MA/EMA/MACD/KDJ/RSI/BOLL/CCI/ATR/BBI/BIAS/BRAR/CR/DFMA/DMI/DPO/EMV/EXPMA/Keltner/MASS/MFI/MTM/OBV/PSY/ROC/TRIX/VR/W&R/ASI/TAQ/XSII)。每个技术指标都有 `_bfq`(不复权)/`_qfq`(前复权)/`_hfq`(后复权) 三个版本。

## 数据范围

- 起始日期：20200102
- API 路径：`GET /v2/market/technical-factors-pro`
