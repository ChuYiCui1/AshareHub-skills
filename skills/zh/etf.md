# ETF 数据链路

ETF 接口覆盖产品档案、跟踪指数、日线、复权、份额规模、净值、定期持仓和申赎篮子。所有方法返回 `pd.DataFrame`，无数据时返回空 DataFrame。

## 数据与服务对应

| Tushare 端点 | RDS 表 | REST 路径（v1/v2） | SDK 方法 | MCP 工具 | 刷新频率 |
|---|---|---|---|---|---|
| `etf_basic` | `tushare_etf_basic` | `/etf/basic` | `client.etf_basic()` | `get_etf_basic` | 每周一 |
| `etf_index` | `tushare_etf_index` | `/etf/indices` | `client.etf_indices()` | `get_etf_indices` | 每周一 |
| `fund_daily` | `tushare_etf_daily` | `/etf/daily` | `client.etf_daily()` | `get_etf_daily` | 工作日多次 |
| `fund_adj` | `tushare_etf_adj` | `/etf/adj-factor` | `client.etf_adj_factor()` | `get_etf_adj_factor` | 工作日多次 |
| `etf_share_size` | `tushare_etf_share_size` | `/etf/share-size` | `client.etf_share_size()` | `get_etf_share_size` | 工作日多次 |
| `fund_nav` | `tushare_etf_nav` | `/etf/nav` | `client.etf_nav()` | `get_etf_nav` | 工作日多次 |
| `fund_portfolio` | `tushare_etf_portfolio` | `/etf/portfolio` | `client.etf_portfolio()` | `get_etf_portfolio` | 每周日 |

REST 路径需要加 `/v1` 或 `/v2` 前缀。SDK 方法始终使用 `symbol` / `con_symbol` 并默认调用 v2；直接调用 REST v1 时才使用 `ts_code` / `con_code` 和 `YYYY-MM-DD` 日期。

## SDK 方法与参数

```python
client.etf_basic(symbol=None, index_symbol=None, list_status=None,
                 exchange=None, manager=None, etf_type=None)
client.etf_indices(symbol=None, pub_date=None, base_date=None)
client.etf_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
client.etf_adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)
client.etf_share_size(symbol=None, start_date=None, end_date=None,
                      trade_date=None, exchange=None)
client.etf_nav(symbol=None, start_date=None, end_date=None,
               nav_date=None, ann_date=None)
client.etf_portfolio(symbol=None, con_symbol=None, start_date=None,
                     end_date=None, period=None, ann_date=None)
```

| 参数 | 说明 |
|---|---|
| `symbol` | ETF 或指数代码，如 `510300.SH`、`159919.SZ`、`000300.SH` |
| `index_symbol` | ETF 跟踪指数代码 |
| `con_symbol` | 持仓证券代码 |
| `start_date` / `end_date` | 日期范围，`YYYYMMDD` |
| `trade_date` / `nav_date` / `ann_date` | 单个交易日、净值日或公告日，`YYYYMMDD` |
| `period` | 持仓报告期，如 `20260331` |
| `list_status` | `L` 上市、`D` 退市、`P` 待上市 |
| `exchange` / `manager` / `etf_type` | 交易所、管理人、ETF 类型精确过滤 |
| `pub_date` / `base_date` | 指数发布日或基日，`YYYYMMDD` |

## 返回字段

### ETF 基础资料 `etf_basic`

`symbol`、`csname`、`extname`、`cname`、`index_symbol`、`index_name`、`setup_date`、`list_date`、`list_status`、`exchange`、`mgr_name`、`custod_name`、`mgt_fee`、`etf_type`。

### ETF 跟踪指数 `etf_index`

`symbol`、`indx_name`、`indx_csname`、`pub_party_name`、`pub_date`、`base_date`、`bp`、`adj_circle`。

### ETF 日行情 `fund_daily`

`symbol`、`trade_date`、`pre_close`、`open`、`high`、`low`、`close`、`change`、`pct_chg`、`vol`（手）、`amount`（千元）。

### ETF 复权因子 `fund_adj`

`symbol`、`trade_date`、`adj_factor`。

### ETF 份额与规模 `etf_share_size`

`trade_date`、`symbol`、`etf_name`、`total_share`（万份）、`total_size`（万元）、`nav`、`close`、`exchange`。

### ETF 净值 `fund_nav`

`symbol`、`ann_date`、`nav_date`、`unit_nav`、`accum_nav`、`accum_div`、`net_asset`、`total_netasset`、`adj_nav`、`update_flag`。

### ETF 季度持仓 `fund_portfolio`

`symbol`、`ann_date`、`end_date`、`con_symbol`、`mkv`、`amount`、`stk_mkv_ratio`、`stk_float_ratio`。

## 示例

```python
# 当前上市 ETF
etfs = client.etf_basic(list_status="L")

# 沪深300ETF华泰柏瑞行情、规模和净值
price = client.etf_daily(symbol="510300.SH", start_date="20260101")
size = client.etf_share_size(symbol="510300.SH", start_date="20260101")
nav = client.etf_nav(symbol="510300.SH", start_date="20260101")

# 最近披露的一季度持仓
holdings = client.etf_portfolio(symbol="510300.SH", period="20260331")
```

## 申赎篮子（PCF）

`client.etf_sh_basket()` / `get_etf_sh_basket` 查询上交所 PCF，`client.etf_sz_basket()` / `get_etf_sz_basket` 查询深交所 PCF。两者支持 `symbol`、`con_symbol`、`start_date`、`end_date`、`trade_date`、`exchange`。

## 注意事项

- `share_size` 和部分境外 ETF 净值通常 T+1 更新。
- `portfolio` 是定期披露持仓，不等于每日申赎篮子。
- PCF 数据量很大，查询时应提供 `symbol` 和较窄日期范围。
