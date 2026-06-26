# 分红送股

## SDK 方法

```python
client.dividend(symbol=None, start_date=None, end_date=None, record_date=None, ex_date=None, imp_ann_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.dividend(symbol="000001.SZ")
print(df[["end_date", "cash_div", "stk_div", "ex_date"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码 |
| `start_date` | str | None | 公告起始日期，YYYYMMDD |
| `end_date` | str | None | 公告截止日期，YYYYMMDD |
| `record_date` | str | None | 股权登记日，YYYYMMDD |
| `ex_date` | str | None | 除权除息日，YYYYMMDD |
| `imp_ann_date` | str | None | 实施公告日，YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `end_date` | 分红年度 |
| `ann_date` | 预案公告日 |
| `div_proc` | 实施进度（预案/董事会预案/股东大会/实施） |
| `cash_div` | 每股分红（税前，元） |
| `cash_div_tax` | 每股分红（税后，元） |
| `stk_div` | 每股送转 |
| `record_date` | 股权登记日 |
| `ex_date` | 除权除息日 |
| `pay_date` | 派息日 |

## 备注

- 在 `ex_date` 之前买入可获得分红
- API 路径：`GET /v2/shareholders/dividend`
