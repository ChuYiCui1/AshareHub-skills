---
name: chip-distribution
description: Query chip distribution (cost basis and winner rate) data
user-invocable: true
---

# Chip Distribution — 筹码分布

使用 AShareHub SDK 查询筹码分布数据（成本分位 + 获利比例）。

## 参数

- `ts_code`: 股票代码，如 `000001.SZ`
- `start_date`: 起始日期，YYYY-MM-DD
- `end_date`: 结束日期，YYYY-MM-DD
- `limit`: 返回行数（默认 100，最大 5000）

## 使用方式

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.chip_distribution(ts_code='${TS_CODE}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, trade_date, his_low, his_high, cost_5pct, cost_15pct, cost_50pct, cost_85pct, cost_95pct, weight_avg, winner_rate

## 注意

- 数据从 2020-01-02 起可用
- winner_rate > 80 通常意味着强势行情
- 中国市场特有的持仓成本分析指标
