# 日线行情

## SDK 方法

```python
client.market_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`，可直接运算。无数据时返回空 DataFrame。

## 示例

```python
df = client.market_daily(symbol="000001.SZ")
print(df[["trade_date", "close", "pct_chg"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ`（平安银行）、`600519.SH`（贵州茅台） |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `trade_date` | 交易日期 |
| `open`, `high`, `low`, `close` | 开高低收价格（元） |
| `pre_close` | 昨收价（除权后） |
| `change` | 涨跌额（元） |
| `pct_chg` | 涨跌幅 % |
| `vol` | 成交量（手，1手=100股） |
| `amount` | 成交额（千元） |

## 数据范围

- 起始日期：20200102
- API 路径：`GET /v2/market/daily`
