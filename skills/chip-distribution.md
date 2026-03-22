# Chip Distribution — 筹码分布

## SDK 方法

```python
client.chip_distribution(ts_code=None, start_date=None, end_date=None, limit=100, offset=0)
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `ts_code` | str | None | 股票代���，如 `000001.SZ` |
| `start_date` | str | None | 起始日期，YYYY-MM-DD |
| `end_date` | str | None | 结束日期，YYYY-MM-DD |
| `limit` | int | 100 | 返回行数，最大 5000 |
| `offset` | int | 0 | 分页偏移量 |

## 返回字段

| 字段 | 说明 |
|------|------|
| `ts_code`, `trade_date` | 股票代码、日期 |
| `his_low`, `his_high` | 历史最低/最高价（元） |
| `cost_5pct` | 5% 成本分位（元） |
| `cost_15pct` | 15% 成本分位（元） |
| `cost_50pct` | 50% 成本分位（中位成本，元） |
| `cost_85pct` | 85% 成本分位（元） |
| `cost_95pct` | 95% 成本分位（元） |
| `weight_avg` | 加权平均成本（元） |
| `winner_rate` | 获利比例（0-100），>80 通常为强势行情 |

## 数据范围

- 起始日期：2020-01-02
- 记录数：7.3M+
- 中国市场特有指标
- API 路径：`GET /v1/chips/distribution`
