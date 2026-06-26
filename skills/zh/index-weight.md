# 指数权重

## SDK 方法

```python
client.index_weight(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.index_weight(symbol="399300.SZ", limit=5)
print(df[["con_symbol", "con_name", "weight"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 指数代码，如 `399300.SZ`（沪深300） |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |
| `limit` | int | 100 | 返回行数，最大 5000 |
| `offset` | int | 0 | 分页偏移量 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 指数代码 |
| `trade_date` | 生效日期 |
| `con_symbol` | 成分股代码 |
| `con_name` | 成分股名称 |
| `weight` | 权重 % |

## 常用指数

| 代码 | 名称 |
|------|------|
| `399300.SZ` | 沪深300 |
| `000905.SH` | 中证500 |
| `000016.SH` | 上证50 |

## 备注

- API 路径：`GET /v2/indices/index-weight`
