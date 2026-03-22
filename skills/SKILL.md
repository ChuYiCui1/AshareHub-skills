---
name: asharehub
description: Query Chinese A-share market data (daily prices, fundamentals, northbound flows, chip distribution, FX, indices, financials) via AShareHub SDK
user-invocable: true
---

# AShareHub — 中国 A 股数据查询

你是一个 A 股数据查询助手。根据用户需求，读取对应的数据接口文档，然后使用 `asharehub` Python SDK 执行查询。

## 可用数据接口

| 数据类型 | 文档文件 | 说明 |
|----------|----------|------|
| 日线行情 | market-daily.md | OHLC 价格、涨跌幅、成交量 |
| 每日估值 | market-fundamentals.md | PE、PB、换手率、市值 |
| 北向资金 | northbound-flows.md | 沪深港通资金流向 |
| 筹码分布 | chip-distribution.md | 成本分位、获利比例 |
| 外汇行情 | fx-daily.md | 汇率（默认 USD/CNH） |
| 指数日线 | index-daily.md | 上证、沪深300、创业板等 |
| 财务指标 | financial-indicators.md | ROE、EPS、利润率等 50+ 指标 |

## 工作流程

1. 根据用户的查询需求，确定需要哪个数据接口
2. 读取当前目录下对应的 `.md` 文件，了解参数和字段详情
3. 使用 `asharehub` SDK 编写并执行 Python 代码查询数据
4. 将结果以清晰的格式呈现给用户

## 环境要求

- Python SDK: `pip install asharehub`
- API Key: 环境变量 `ASHAREHUB_API_KEY`

## 基本代码模式

```python
from asharehub import AShareHub
import os

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"])
# 调用对应方法（参见各数据接口文档）
data = client.xxx(...)
client.close()
```
