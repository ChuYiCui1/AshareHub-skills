# 股票列表

## SDK 方法

```python
client.stock_list(symbol=None, name=None, market=None, list_status=None, exchange=None, is_hs=None)
```

## 返回类型

`pd.DataFrame` — 无数据时返回空 DataFrame。

## 示例

```python
df = client.stock_list(symbol="000001.SZ")
print(df[["symbol", "name", "industry", "list_date"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ`（平安银行）、`600519.SH`（贵州茅台） |
| `name` | str | None | 股票名称 |
| `market` | str | None | 市场类别：主板/创业板/科创板/北交所/CDR |
| `list_status` | str | None | 上市状态：L上市/D退市/P暂停 |
| `exchange` | str | None | 交易所：SSE/SZSE/BSE |
| `is_hs` | str | None | 沪深港通：N否/H沪股通/S深股通 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `symbol` | 证券代码 |
| `name` | 股票名称 |
| `area` | 地域 |
| `industry` | 行业 |
| `fullname` | 公司全称 |
| `enname` | 英文名 |
| `cnspell` | 拼音缩写 |
| `market` | 市场 |
| `exchange` | 交易所 |
| `curr_type` | 币种 |
| `list_status` | 上市状态（L=上市 D=退市 P=暂停） |
| `list_date` | 上市日期 |
| `delist_date` | 退市日期 |
| `is_hs` | 沪深港通标的（H/S/N） |

## 数据范围

- 数据类型：静态数据
- API 路径：`GET /v2/reference/stocks`
