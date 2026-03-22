---
name: index-daily
description: Query daily OHLC data for major Chinese market indices
user-invocable: true
---

# Index Daily — 指数日线

使用 AShareHub SDK 查询主要中国市场指数日线数据。

## 参数

- `ts_code`: 指数代码，默认 `000001.SH`（上证综指）
- `start_date`: 起始日期，YYYY-MM-DD
- `end_date`: 结束日期，YYYY-MM-DD
- `limit`: 返回行数（默认 100，最大 2000）

## 常用指数代码

- `000001.SH` — 上证综指
- `000300.SH` — 沪深300
- `399001.SZ` — 深证成指
- `399006.SZ` — 创业板指
- `000016.SH` — 上证50

## 使用方式

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.index_daily(ts_code='${TS_CODE:-000001.SH}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount
