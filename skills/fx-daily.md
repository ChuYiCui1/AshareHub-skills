---
name: fx-daily
description: Query daily FX rates (default USD/CNH)
user-invocable: true
---

# FX Daily — 外汇日线

使用 AShareHub SDK 查询外汇日线行情（默认美元/离岸人民币）。

## 参数

- `ts_code`: 外汇对代码，默认 `USDCNH.FXCM`
- `start_date`: 起始日期，YYYY-MM-DD
- `end_date`: 结束日期，YYYY-MM-DD
- `limit`: 返回行数（默认 100，最大 2000）

## 使用方式

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.fx_daily(ts_code='${TS_CODE:-USDCNH.FXCM}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, trade_date, bid_open, bid_close, bid_high, bid_low, ask_open, ask_close, ask_high, ask_low, tick_qty

## 注意

- 数据从 2012-01-01 起可用
- USDCNH 上涨 = 人民币贬值，通常对 A 股外资流入形成压力
