---
name: asharehub
description: 查询中国A股与 ETF 市场数据（ETF 基础资料、跟踪指数、日行情、复权因子、份额规模、净值和季度持仓，以及股票日线行情、估值指标、沪深港通资金、资金流向、融资融券、财务报表、技术因子、交易日历等），共 30+ 个数据接口
user-invocable: true
---

# AShareHub — 中国 A 股数据查询

你是一个 A 股数据查询助手。根据用户需求，读取对应的数据接口文档，然后使用 `asharehub` Python SDK 执行查询。

## 可用数据接口

### 行情数据
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 实时行情 | realtime.md | 每股最新盘中快照价(支持一篮子查询) |
| 日线行情 | market-daily.md | OHLC 价格、涨跌幅、成交量 |
| 每日估值 | market-fundamentals.md | PE、PB、换手率、市值 |
| 融资融券 | margin.md | 融资余额、融券余额 |
| 大宗交易 | block-trade.md | 场外协议成交，含买卖方 |
| 龙虎榜 | top-list.md | 异动股机构买卖披露 |
| 股东户数 | shareholders.md | 季度股东户数变化 |
| 股东增减持 | holder-trade.md | 重要股东及高管交易 |
| 概念板块 | concepts.md | AI、新能源等主题板块指数 |
| 概念成分 | concept-members.md | 概念板块成分股 |
| 复权因子 | adj-factor.md | 前/后复权价格计算因子 |
| 技术因子 | technical-factors.md | MACD、KDJ、RSI、布林带、CCI + 复权价 |
| 技术因子专业版 | technical-factors-pro.md | 200+ 指标，含 bfq/qfq/hfq 三种复权 |
| 涨跌停统计 | limit-list.md | 每日涨停/跌停/炸板统计（2020 年起） |
| 龙虎榜机构明细 | top-inst.md | 异动股机构席位买卖明细 |

### 资金流向
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 沪深港通资金 | moneyflow-hsgt.md | 沪深港通资金流向（北向+南向汇总） |
| 个股资金流 | moneyflow.md | 大中小单资金流向 |
| 北向持股 | northbound-holdings.md | 外资 A 股持仓明细 |
| 南向持股 | southbound-holdings.md | 内地持有港股的明细 |

### 财务数据
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 财务指标 | financial-indicators.md | ROE、EPS、利润率等 50+ 指标 |
| 利润表 | income.md | 营收、成本、净利润（按季度） |
| 资产负债表 | balance-sheet.md | 资产、负债、所有者权益 |
| 现金流量表 | cash-flow.md | 经营/投资/筹资现金流 |
| 业绩预告 | forecast.md | 预增/预减/扭亏等预告 |
| 业绩快报 | express.md | 正式财报前的快报 |
| 分红送股 | dividend.md | 现金分红与送转股 |
| 券商盈利预测 | analyst-reports.md | 卖方研报：目标价、评级、EPS/PE 预测 |
| 审计意见 | audit.md | 年报审计意见与审计费用 |
| 主营业务构成 | main-business.md | 按业务/产品/地区的收入利润明细 |
| 财报披露日期 | disclosure-date.md | 预约披露日和实际披露日 |

### 指数
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 指数日线 | index-daily.md | 上证综指、沪深300、创业板等 |
| 指数权重 | index-weight.md | 指数成分股权重 |

### ETF
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| ETF 全链路 | etf.md | 档案、指数、行情、复权、规模、净值、持仓和申赎篮子 |

### 其他
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 财经快讯 | news-flash.md | 实时新闻快讯（财联社/金十/新浪，中文） |
| 筹码分布 | chip-distribution.md | 成本分位、获利比例 |
| 外汇行情 | fx-daily.md | 汇率（默认 USD/CNH） |

### 参考数据
| 数据类型 | 参考文档 | 说明 |
|----------|----------|------|
| 股票列表 | stocks.md | 全部上市 A 股基本信息 |
| 行业分类 | industries.md | 申万三级行业分类 |
| 交易日历 | trade-calendar.md | 沪深交易所交易日与休市日 |

## 返回类型

- 所有方法返回 `pd.DataFrame`，与 Tushare 风格一致
- 数值列为 `float64`，字符串列为 `object`，可直接运算
- 访问方式：`df["close"]`、`df.close`、`df.iloc[0]`
- 无数据时返回空 DataFrame，用 `df.empty` 判断

### 非交易日处理

API 只包含交易日数据。查询非交易日（周末/节假日）会返回空 DataFrame。
推荐获取最新数据的方式：

```python
# 不指定日期，结果按日期倒序，第一行即最近一个交易日
df = client.market_daily(symbol="000001.SZ")
```

## 工作流程

1. 根据用户的查询需求，确定需要哪个数据接口
2. 读取当前目录下对应的 `.md` 文件，了解参数和字段详情
3. 使用 `asharehub` SDK 编写并执行 Python 代码查询数据
4. 将结果以清晰的格式呈现给用户

## 环境要求

- Python SDK: `pip install asharehub`
- API Key: 环境变量 `ASHAREHUB_API_KEY`

## 快速开始

```python
from asharehub import AShareHub
import os

client = AShareHub(api_key=os.environ["ASHAREHUB_API_KEY"], version="v2")

# 返回 pd.DataFrame
df = client.market_daily(symbol="000001.SZ", start_date="20240101", end_date="20240131")
print(df[["trade_date", "open", "high", "low", "close", "vol"]])

client.close()
```

## 更新 skill 与 SDK

当用户说「更新 skill / 更新 sdk / 更新一下 / update / 拉最新版」时，直接执行下面的命令即可，无需额外确认：

- **同时更新两者（推荐，一句话搞定）**：

  ```bash
  curl -fsSL "https://asharehub.com/skill/install?lang=zh" | bash && pip install -U asharehub
  ```

- 只更新本 skill（覆盖式拉取最新接口文档到 `.claude/skills/asharehub/`）：

  ```bash
  curl -fsSL "https://asharehub.com/skill/install?lang=zh" | bash
  ```

- 只更新 Python SDK 到最新版：

  ```bash
  pip install -U asharehub
  ```

更新完成后，提示用户重新输入 `/asharehub` 以加载最新文档。

## 使用示例

### 查看估值

```python
df = client.fundamentals(symbol="600519.SH", start_date="20240101")
print(df[["trade_date", "pe_ttm", "pb", "total_mv"]])
```

### 沪深港通资金

```python
df = client.moneyflow_hsgt(start_date="20240301", end_date="20240315")
print(df[["trade_date", "north_money", "south_money"]])
```

### 财务指标

```python
df = client.financial_indicators(symbol="000001.SZ")
print(df[["end_date", "roe", "eps", "netprofit_margin"]])
```
