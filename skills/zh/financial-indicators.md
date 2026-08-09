# 财务指标

## SDK 方法

```python
client.financial_indicators(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.financial_indicators(symbol="000001.SZ")
print(df[["end_date", "roe", "eps", "netprofit_margin"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ` |
| `start_date` | str | None | 报告期起始，YYYYMMDD |
| `end_date` | str | None | 报告期结束，YYYYMMDD |
| `period` | str | None | 报告期，YYYYMMDD，如20231231 |
| `ann_date` | str | None | 公告日期，YYYYMMDD |

## 返回字段

| 类别 | 字段 |
|------|------|
| **每股指标** | `eps`, `dt_eps`, `total_revenue_ps`, `revenue_ps`, `bps`, `ocfps` |
| **盈利能力** | `roe`, `roe_waa`, `roe_dt`, `roa`, `gross_margin`, `netprofit_margin`, `grossprofit_margin` |
| **偿债能力** | `debt_to_assets`, `current_ratio`, `quick_ratio`, `cash_ratio` |
| **运营效率** | `assets_turn`, `inv_turn`, `ar_turn` |
| **投资回报** | `roic` |
| **增长率** | `basic_eps_yoy`, `dt_eps_yoy`, `netprofit_yoy`, `dt_netprofit_yoy` |
| **研发** | `rd_exp`（元） |
| **日期** | `ann_date`（公告日）, `end_date`（报告期） |

## 数据范围

- `end_date` 为财务报告期（如 20241231 为年报，20240630 为半年报）
- API 路径：`GET /v2/financials/indicators`
