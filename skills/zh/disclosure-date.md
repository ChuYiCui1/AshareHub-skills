# 财报披露日期

## SDK 方法

```python
client.disclosure_date(symbol=None, start_date=None, end_date=None, pre_date=None, actual_date=None)
```

## 返回类型

`pd.DataFrame` — 6 列。无数据时返回空 DataFrame。

## 示例

```python
df = client.disclosure_date(symbol="000001.SZ")
print(df[["end_date", "pre_date", "actual_date"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码 |
| `start_date` | str | None | 起始日期 YYYYMMDD |
| `end_date` | str | None | 结束日期 YYYYMMDD |
| `pre_date` | str | None | 计划披露日期，YYYYMMDD |
| `actual_date` | str | None | 实际披露日期，YYYYMMDD |

## 返回字段

symbol、ann_date(最新公告日)、end_date(报告期)、pre_date(预约披露日)、actual_date(实际披露日)、modify_date(修改日)。

## 数据范围

- 起始日期：20010206
- 用于追踪上市公司财报披露时间
- API 路径：`GET /v2/financials/disclosure-date`
