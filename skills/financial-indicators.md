---
name: financial-indicators
description: Query quarterly financial indicators (ROE, EPS, margins, ratios)
user-invocable: true
---

# Financial Indicators — 财务指标

使用 AShareHub SDK 查询季度财务指标（ROE、EPS、利润率等 50+ 指标）。

## 参数

- `ts_code`: 股票代码，如 `000001.SZ`
- `start_date`: 报告期起始，YYYY-MM-DD
- `end_date`: 报告期结束，YYYY-MM-DD
- `limit`: 返回行数（默认 20，最大 200）

## 使用方式

```bash
ASHAREHUB_API_KEY="${ASHAREHUB_API_KEY}" python3 -c "
from asharehub import AShareHub
import os, json

client = AShareHub(api_key=os.environ['ASHAREHUB_API_KEY'])
data = client.financial_indicators(ts_code='${TS_CODE}', start_date='${START_DATE}', end_date='${END_DATE}', limit=${LIMIT:-20})
for row in data:
    print(json.dumps(row.model_dump(mode='json'), ensure_ascii=False))
client.close()
"
```

## 返回字段

ts_code, ann_date, end_date, eps, dt_eps, roe, roe_waa, roe_dt, roa, gross_margin, netprofit_margin, debt_to_assets, current_ratio, quick_ratio, cash_ratio, assets_turn, inv_turn, ar_turn, roic, basic_eps_yoy, netprofit_yoy, rd_exp ...

## 注意

- 数据目前较少（116 条），后续会批量补充
- end_date 指财务报告期（如 2024-12-31 为年报）
