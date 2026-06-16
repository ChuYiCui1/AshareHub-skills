# 实时行情 — 实时盘口快照

## SDK 方法

```python
client.realtime(ts_code=None, limit=100, offset=0)
```

## 返回

`pd.DataFrame` — 列：ts_code, name, price, open, high, low, pre_close, pct_chg, volume, amount, trade_time。无数据时返回空 DataFrame。

## 示例

```python
# 一次查一篮子(ts_code 逗号分隔，最多 200 只)
df = client.realtime(ts_code="600519.SH,000001.SZ,000001.SH")
print(df[["ts_code", "name", "price", "pct_chg"]])
```

## 参数

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| ts_code | str | 否 | 单只代码，或逗号分隔的一篮子(最多 200)，如 `600519.SH,000001.SZ`。不填则翻页查全市场。 |
| limit | int | 否 | 最大行数(默认 100，最大 5000) |
| offset | int | 否 | 分页偏移(默认 0) |

## 返回字段

| 字段 | 说明 |
|------|------|
| ts_code | 股票/指数代码 |
| name | 证券名称 |
| price | 最新成交价 |
| open / high / low | 当日开/高/低 |
| pre_close | 昨收价 |
| pct_chg | 相对昨收的涨跌幅(%) |
| volume | 累计成交量(股) |
| amount | 累计成交额(元) |
| trade_time | 数据源的行情时间戳 |

## 说明

- 每只证券一行，盘中持续刷新 —— 是当下快照，不是时间序列。
- 非交易时段返回上一交易日的收盘快照。
- 历史日线用 `client.market_daily()`；盘中技术指标见 `client.technical_factors()`。
