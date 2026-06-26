# 每日估值指标

## SDK 方法

```python
client.fundamentals(symbol=None, start_date=None, end_date=None, limit=100, offset=0)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.fundamentals(symbol="600519.SH", limit=3)
print(df[["trade_date", "pe_ttm", "pb", "total_mv"]])
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
| `symbol`, `trade_date` | 股票代码、日期 |
| `close` | 收盘价 |
| `turnover_rate`, `turnover_rate_f` | 换手率 % |
| `volume_ratio` | 量比（当日均量/5日均量） |
| `pe`, `pe_ttm` | 市盈率 |
| `pb` | 市净率 |
| `ps`, `ps_ttm` | 市销率 |
| `dv_ratio`, `dv_ttm` | 股息率 % |
| `total_share`, `float_share`, `free_share` | 总/流通/自由流通股本（万股） |
| `total_mv`, `circ_mv` | 总/流通市值（万元） |

## 数据范围

- 起始日期：20100104
- API 路径：`GET /v2/market/fundamentals`
