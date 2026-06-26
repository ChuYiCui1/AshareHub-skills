# 复权因子

## SDK 方法

```python
client.adj_factor(symbol=None, start_date=None, end_date=None, limit=100, offset=0)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.adj_factor(symbol="000001.SZ", limit=3)
print(df[["trade_date", "adj_factor"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ` |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `limit` | int | 100 | 返回行数，最大 5000 |
| `offset` | int | 0 | 分页偏移量 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `trade_date` | 交易日期 |
| `adj_factor` | 复权因子 |

## 备注

- 前复权价 = 未复权价 × adj_factor / 最新 adj_factor
- 后复权价 = 未复权价 × adj_factor
- API 路径：`GET /v2/market/adj-factor`
