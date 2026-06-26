# 技术因子

## SDK 方法

```python
client.technical_factors(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.technical_factors(symbol="000001.SZ")
print(df[["trade_date", "close_qfq", "macd", "kdj_k", "rsi_6"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ` |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |

## 返回字段

| 分类 | 字段 |
|------|------|
| **后复权价** | `open_hfq`, `close_hfq`, `high_hfq`, `low_hfq`, `pre_close_hfq` |
| **前复权价** | `open_qfq`, `close_qfq`, `high_qfq`, `low_qfq`, `pre_close_qfq` |
| **MACD** | `macd_dif`, `macd_dea`, `macd` |
| **KDJ** | `kdj_k`, `kdj_d`, `kdj_j` |
| **RSI** | `rsi_6`, `rsi_12`, `rsi_24` |
| **布林带** | `boll_upper`, `boll_mid`, `boll_lower` |
| **CCI** | `cci` |

## 备注

- qfq = 前复权，hfq = 后复权
- API 路径：`GET /v2/market/technical-factors`
