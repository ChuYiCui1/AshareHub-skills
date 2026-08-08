# ETF Data Chain

The ETF endpoints cover product reference data, benchmark indices, daily prices,
adjustment factors, shares/assets, NAV, disclosed holdings and daily
creation/redemption baskets. Every method returns a `pd.DataFrame`; an empty
result is returned as an empty DataFrame.

## Data and service mapping

| Tushare endpoint | RDS table | REST path (v1/v2) | SDK method | MCP tool | Refresh |
|---|---|---|---|---|---|
| `etf_basic` | `tushare_etf_basic` | `/etf/basic` | `client.etf_basic()` | `get_etf_basic` | Monday |
| `etf_index` | `tushare_etf_index` | `/etf/indices` | `client.etf_indices()` | `get_etf_indices` | Monday |
| `fund_daily` | `tushare_etf_daily` | `/etf/daily` | `client.etf_daily()` | `get_etf_daily` | Multiple times per business day |
| `fund_adj` | `tushare_etf_adj` | `/etf/adj-factor` | `client.etf_adj_factor()` | `get_etf_adj_factor` | Multiple times per business day |
| `etf_share_size` | `tushare_etf_share_size` | `/etf/share-size` | `client.etf_share_size()` | `get_etf_share_size` | Multiple times per business day |
| `fund_nav` | `tushare_etf_nav` | `/etf/nav` | `client.etf_nav()` | `get_etf_nav` | Multiple times per business day |
| `fund_portfolio` | `tushare_etf_portfolio` | `/etf/portfolio` | `client.etf_portfolio()` | `get_etf_portfolio` | Sunday |

Prefix each REST path with `/v1` or `/v2`. SDK methods always use `symbol` /
`con_symbol` and target v2 by default. Direct REST v1 calls use `ts_code` /
`con_code` and `YYYY-MM-DD` dates instead.

## SDK methods and parameters

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

| Parameter | Description |
|---|---|
| `symbol` | ETF or index code, such as `510300.SH`, `159919.SZ`, or `000300.SH` |
| `index_symbol` | Tracked-index code used to filter the ETF directory |
| `con_symbol` | Portfolio constituent security code |
| `start_date` / `end_date` | Date range in `YYYYMMDD` format |
| `trade_date` / `nav_date` / `ann_date` | A single trading, NAV, or announcement date in `YYYYMMDD` format |
| `period` | Portfolio reporting period, such as `20260331` |
| `list_status` | `L` listed, `D` delisted, or `P` pending listing |
| `exchange` / `manager` / `etf_type` | Exact exchange, manager, or ETF-type filters |
| `pub_date` / `base_date` | Index publication or base date in `YYYYMMDD` format |

## Response fields

### ETF directory `etf_basic`

`symbol`, `csname`, `extname`, `cname`, `index_symbol`, `index_name`,
`setup_date`, `list_date`, `list_status`, `exchange`, `mgr_name`, `custod_name`,
`mgt_fee`, `etf_type`.

### ETF index directory `etf_index`

`symbol`, `indx_name`, `indx_csname`, `pub_party_name`, `pub_date`, `base_date`,
`bp`, `adj_circle`.

### ETF daily prices `fund_daily`

`symbol`, `trade_date`, `pre_close`, `open`, `high`, `low`, `close`, `change`,
`pct_chg`, `vol` (lots), `amount` (CNY thousands).

### ETF adjustment factors `fund_adj`

`symbol`, `trade_date`, `adj_factor`.

### ETF shares and assets `etf_share_size`

`trade_date`, `symbol`, `etf_name`, `total_share` (10,000 shares), `total_size`
(CNY 10,000), `nav`, `close`, `exchange`.

### ETF NAV `fund_nav`

`symbol`, `ann_date`, `nav_date`, `unit_nav`, `accum_nav`, `accum_div`,
`net_asset`, `total_netasset`, `adj_nav`, `update_flag`.

### ETF disclosed holdings `fund_portfolio`

`symbol`, `ann_date`, `end_date`, `con_symbol`, `mkv`, `amount`,
`stk_mkv_ratio`, `stk_float_ratio`.

## Example

```python
etfs = client.etf_basic(list_status="L")
prices = client.etf_daily(symbol="510300.SH", start_date="20260101")
size = client.etf_share_size(symbol="510300.SH", start_date="20260101")
nav = client.etf_nav(symbol="510300.SH", start_date="20260101")
holdings = client.etf_portfolio(symbol="510300.SH", period="20260331")
```

## Creation/redemption baskets (PCF)

Use `client.etf_sh_basket()` / `get_etf_sh_basket` for Shanghai PCF data and
`client.etf_sz_basket()` / `get_etf_sz_basket` for Shenzhen PCF data. Both
accept `symbol`, `con_symbol`, `start_date`, `end_date`, `trade_date`, and
`exchange`.

## Notes

- Shares/assets and some overseas ETF NAV values are generally available T+1.
- Disclosed portfolio holdings are not the same as the daily PCF basket.
- PCF data is large; always narrow it with `symbol` and a short date range.
