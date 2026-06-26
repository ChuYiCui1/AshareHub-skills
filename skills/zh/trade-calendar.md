# 交易日历

## SDK 方法

```python
client.trade_calendar(exchange=None, start_date=None, end_date=None, is_open=None, limit=100, offset=0)
```

## 返回类型

`pd.DataFrame` — 无数据时返回空 DataFrame。

## 示例

```python
df = client.trade_calendar(exchange="SSE", start_date="20240325", end_date="20240331")
print(df[["cal_date", "is_open"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `exchange` | str | None | 交易所：`SSE`（上交所）或 `SZSE`（深交所） |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `is_open` | int | None | `1`=仅交易日，`0`=仅休市日 |
| `limit` | int | 100 | 返回行数，最大 5000 |
| `offset` | int | 0 | 分页偏移量 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `exchange` | 交易所代码 |
| `cal_date` | 日历日期 |
| `is_open` | 1=交易日，0=休市 |
| `pretrade_date` | 上一交易日 |

## 备注

- 覆盖上交所和深交所
- API 路径：`GET /v2/reference/trade-calendar`
