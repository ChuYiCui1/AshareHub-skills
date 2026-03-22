---
name: northbound-flows
description: Query northbound capital flows via Stock Connect
user-invocable: true
---

# Northbound Flows — 北向资金

使用 AShareHub SDK 查询沪深港通北向资金数据。

## 参数

- `start_date`: 起始日期，YYYY-MM-DD
- `end_date`: 结束日期，YYYY-MM-DD
- `limit`: 返回行数（默认 100，最大 2000）

## 使用方式

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.northbound_flows(start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

trade_date, ggt_ss, ggt_sz, hgt_ss, hgt_sz, north_money, south_money

## 注意

- 数据从 2014-11-17 起可用
- north_money 为正表示外资净买入（单位：百万元）
- 每日仅一条记录
