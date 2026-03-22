---
name: market-daily
description: Query daily OHLC price data for A-share stocks
user-invocable: true
---

# Market Daily — A股日线行情

使用 AShareHub SDK 查询 A 股日线 OHLC 数据。

## 参数

- `ts_code`: 股票代码，如 `000001.SZ`（平安银行）、`600519.SH`（贵州茅台）
- `start_date`: 起始日期，YYYY-MM-DD
- `end_date`: 结束日期，YYYY-MM-DD
- `limit`: 返回行数（默认 100，最大 5000）

## 使用方式

通过 Bash 运行 Python 脚本查询数据：

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.market_daily(ts_code='${TS_CODE}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-100})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, trade_date, open, high, low, close, pre_close, change, pct_chg, vol, amount

## 注意

- 数据从 2020-01-02 起可用
- vol 单位为手（1手=100股），amount 单位为千元
