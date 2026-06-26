# 主营业务构成

## SDK 方法

```python
client.main_business(symbol=None, start_date=None, end_date=None, period=None)
```

## 返回类型

`pd.DataFrame` — 7 列，数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.main_business(symbol="600519.SH")
print(df[["end_date", "bz_item", "bz_sales", "bz_profit"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码 |
| `start_date` | str | None | 起始日期 YYYYMMDD |
| `end_date` | str | None | 结束日期 YYYYMMDD |
| `period` | str | None | 报告期，YYYYMMDD，如20231231 |

## 返回字段

symbol、end_date、bz_item(业务名称)、bz_sales(业务收入)、bz_profit(业务利润)、bz_cost(业务成本)、curr_type(币种)。

## 数据范围

- 起始日期：20141231
- 用于了解公司业务构成（按产品/地区）
- API 路径：`GET /v2/financials/main-business`
