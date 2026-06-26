# 股东户数

## SDK 方法

```python
client.shareholders(symbol=None, start_date=None, end_date=None, enddate=None, ann_date=None)
```

## 返回类型

`pd.DataFrame` — 无数据时返回空 DataFrame。

## 示例

```python
df = client.shareholders(symbol="000001.SZ")
print(df[["end_date", "holder_num"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ`（平安银行）、`600519.SH`（贵州茅台） |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `enddate` | str | None | 统计截止日，YYYYMMDD |
| `ann_date` | str | None | 公告日期，YYYYMMDD |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `ann_date` | 公告日期 |
| `end_date` | 报告期末 |
| `holder_num` | 股东户数 |

## 数据范围

- 起始日期：20240101
- API 路径：`GET /v2/market/shareholders`

## 备注

- 户数下降通常意味着筹码集中，可作为主力吸筹的参考信号
