# 业绩预告

## SDK 方法

```python
client.forecast(symbol=None, start_date=None, end_date=None, period=None, type=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.forecast(symbol="000001.SZ")
print(df[["ann_date", "end_date", "type", "net_profit_min", "net_profit_max"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码 |
| `start_date` | str | None | 公告起始日期，YYYYMMDD |
| `end_date` | str | None | 公告截止日期，YYYYMMDD |
| `period` | str | None | 报告期，YYYYMMDD，如20231231 |
| `type` | str | None | 预告类型：预增/预减/扭亏/首亏/续亏/续盈/略增/略减 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `ann_date` | 公告日期 |
| `end_date` | 报告期 |
| `type` | 预告类型（预增/预减/扭亏/首亏/续亏/续盈/略增/略减） |
| `p_change_min` / `p_change_max` | 净利润变动幅度范围 % |
| `net_profit_min` / `net_profit_max` | 预计净利润范围（万元） |
| `last_parent_net` | 上年同期归母净利润（万元） |
| `first_ann_date` | 首次公告日期 |
| `summary` | 业绩摘要 |
| `change_reason` | 变动原因 |

## 备注

- API 路径：`GET /v2/financials/forecast`
