---
name: market-fundamentals
description: Query daily valuation metrics (PE, PB, turnover, market cap) for A-share stocks
user-invocable: true
---

# Market Fundamentals — A股每日估值指标

使用 AShareHub SDK 查询 PE、PB、换手率、市值等每日估值数据。

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
data = client.fundamentals(ts_code='${TS_CODE}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, trade_date, close, turnover_rate, turnover_rate_f, volume_ratio, pe, pe_ttm, pb, ps, ps_ttm, dv_ratio, dv_ttm, total_share, float_share, free_share, total_mv, circ_mv

## 注意

- 数据从 2010-01-04 起可用，最完整的数据集
- total_mv/circ_mv 单位为万元
