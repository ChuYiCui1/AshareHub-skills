# 指数日线

## SDK 方法

```python
client.index_daily(symbol="000001.SH", start_date=None, end_date=None, trade_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.index_daily(symbol="000001.SH")
print(df[["trade_date", "close", "pct_chg"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | `000001.SH` | 指数代码 |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |

## 常用指数代码

| 代码 | 名称 |
|------|------|
| `000001.SH` | 上证综指 |
| `000300.SH` | 沪深300 |
| `399001.SZ` | 深证成指 |
| `399006.SZ` | 创业板指 |
| `000016.SH` | 上证50 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 指数代码 |
| `trade_date` | 交易日期 |
| `open`, `high`, `low`, `close` | 指数点位 |
| `pre_close` | 昨收 |
| `change` | 涨跌点 |
| `pct_chg` | 涨跌幅 % |
| `vol` | 成交量（手） |
| `amount` | 成交额（千元） |

## 数据范围

- 起始日期：20100104
- API 路径：`GET /v2/indices/daily`
