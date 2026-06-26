# 大宗交易

## SDK 方法

```python
client.block_trade(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.block_trade(symbol="000001.SZ")
print(df[["trade_date", "price", "vol", "buyer", "seller"]])
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
| `price` | 成交价 |
| `vol` | 成交量（万股） |
| `amount` | 成交额（万元） |
| `buyer` | 买方营业部 |
| `seller` | 卖方营业部 |

## 数据范围

- 起始日期：20100104
- API 路径：`GET /v2/market/block-trade`
