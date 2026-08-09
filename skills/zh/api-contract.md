# AShareHub 精确公开接口契约

本文件由 V2 OpenAPI 契约生成，列出每个 REST 接口、SDK 方法、MCP 工具、请求参数和全部返回字段。

## `market_daily`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/daily`
- SDK: `client.market_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_market_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `fundamentals`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/fundamentals`
- SDK: `client.fundamentals(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_fundamentals(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `close`, `turnover_rate`, `turnover_rate_f`, `volume_ratio`, `pe`, `pe_ttm`, `pb`, `ps`, `ps_ttm`, `dv_ratio`, `dv_ttm`, `total_share`, `float_share`, `free_share`, `total_mv`, `circ_mv`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `moneyflow_hsgt`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/flows/moneyflow-hsgt`
- SDK: `client.moneyflow_hsgt(start_date=None, end_date=None, trade_date=None)`
- MCP: `get_moneyflow_hsgt(start_date=None, end_date=None, trade_date=None)`
- Request parameters: `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `ggt_ss`, `ggt_sz`, `hgt_ss`, `hgt_sz`, `north_money`, `south_money`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `chip_distribution`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/chips/distribution`
- SDK: `client.chip_distribution(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_chip_distribution(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `his_low`, `his_high`, `cost_5pct`, `cost_15pct`, `cost_50pct`, `cost_85pct`, `cost_95pct`, `weight_avg`, `winner_rate`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `fx_daily`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/fx/daily`
- SDK: `client.fx_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_fx_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `bid_open`, `bid_close`, `bid_high`, `bid_low`, `ask_open`, `ask_close`, `ask_high`, `ask_low`, `tick_qty`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `index_daily`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/indices/daily`
- SDK: `client.index_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_index_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `close`, `open`, `high`, `low`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_basic`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/basic`
- SDK: `client.etf_basic(symbol=None, index_symbol=None, list_status=None, exchange=None, manager=None, etf_type=None)`
- MCP: `get_etf_basic(symbol=None, index_symbol=None, list_status=None, exchange=None, manager=None, etf_type=None)`
- Request parameters: `symbol`, `index_symbol`, `list_status`, `exchange`, `manager`, `etf_type`
- Response fields: `symbol`, `csname`, `extname`, `cname`, `index_symbol`, `index_name`, `setup_date`, `list_date`, `list_status`, `exchange`, `mgr_name`, `custod_name`, `mgt_fee`, `etf_type`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_indices`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/indices`
- SDK: `client.etf_indices(symbol=None, pub_date=None, base_date=None)`
- MCP: `get_etf_indices(symbol=None, pub_date=None, base_date=None)`
- Request parameters: `symbol`, `pub_date`, `base_date`
- Response fields: `symbol`, `indx_name`, `indx_csname`, `pub_party_name`, `pub_date`, `base_date`, `bp`, `adj_circle`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_daily`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/daily`
- SDK: `client.etf_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_etf_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `pre_close`, `open`, `high`, `low`, `close`, `change`, `pct_chg`, `vol`, `amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_adj_factor`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/adj-factor`
- SDK: `client.etf_adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_etf_adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `adj_factor`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_share_size`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/share-size`
- SDK: `client.etf_share_size(symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- MCP: `get_etf_share_size(symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`, `exchange`
- Response fields: `trade_date`, `symbol`, `etf_name`, `total_share`, `total_size`, `nav`, `close`, `exchange`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_nav`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/nav`
- SDK: `client.etf_nav(symbol=None, start_date=None, end_date=None, nav_date=None, ann_date=None)`
- MCP: `get_etf_nav(symbol=None, start_date=None, end_date=None, nav_date=None, ann_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `nav_date`, `ann_date`
- Response fields: `symbol`, `ann_date`, `nav_date`, `unit_nav`, `accum_nav`, `accum_div`, `net_asset`, `total_netasset`, `adj_nav`, `update_flag`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_portfolio`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/portfolio`
- SDK: `client.etf_portfolio(symbol=None, con_symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- MCP: `get_etf_portfolio(symbol=None, con_symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- Request parameters: `symbol`, `con_symbol`, `start_date`, `end_date`, `period`, `ann_date`
- Response fields: `symbol`, `ann_date`, `end_date`, `con_symbol`, `mkv`, `amount`, `stk_mkv_ratio`, `stk_float_ratio`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_sh_basket`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/basket/sh`
- SDK: `client.etf_sh_basket(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- MCP: `get_etf_sh_basket(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- Request parameters: `symbol`, `con_symbol`, `start_date`, `end_date`, `trade_date`, `exchange`
- Response fields: `trade_date`, `symbol`, `con_symbol`, `con_name`, `qty`, `sub_flag`, `cpr`, `rdr`, `sca`, `exchange`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `etf_sz_basket`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/etf/basket/sz`
- SDK: `client.etf_sz_basket(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- MCP: `get_etf_sz_basket(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None, exchange=None)`
- Request parameters: `symbol`, `con_symbol`, `start_date`, `end_date`, `trade_date`, `exchange`
- Response fields: `trade_date`, `symbol`, `con_symbol`, `con_name`, `qty`, `sub_flag`, `cpr`, `rdr`, `sub_cc`, `red_cc`, `exchange`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `hk_stock_list`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/hk/basic`
- SDK: `client.hk_stock_list(symbol=None, list_status=None)`
- MCP: `get_hk_stock_list(symbol=None, list_status=None)`
- Request parameters: `symbol`, `list_status`
- Response fields: `symbol`, `name`, `fullname`, `enname`, `cn_spell`, `market`, `list_status`, `list_date`, `delist_date`, `trade_unit`, `isin`, `curr_type`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `hk_daily`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/hk/daily`
- SDK: `client.hk_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_hk_daily(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `hk_trade_calendar`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/hk/trade-calendar`
- SDK: `client.hk_trade_calendar(start_date=None, end_date=None, is_open=None)`
- MCP: `get_hk_trade_calendar(start_date=None, end_date=None, is_open=None)`
- Request parameters: `start_date`, `end_date`, `is_open`
- Response fields: `exchange`, `cal_date`, `is_open`, `pretrade_date`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `financial_indicators`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/indicators`
- SDK: `client.financial_indicators(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- MCP: `get_financial_indicators(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `ann_date`
- Response fields: `symbol`, `ann_date`, `end_date`, `eps`, `dt_eps`, `total_revenue_ps`, `revenue_ps`, `bps`, `ocfps`, `roe`, `roe_waa`, `roe_dt`, `roa`, `gross_margin`, `netprofit_margin`, `grossprofit_margin`, `debt_to_assets`, `current_ratio`, `quick_ratio`, `cash_ratio`, `assets_turn`, `inv_turn`, `ar_turn`, `roic`, `basic_eps_yoy`, `dt_eps_yoy`, `netprofit_yoy`, `dt_netprofit_yoy`, `rd_exp`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `moneyflow`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/flows/moneyflow`
- SDK: `client.moneyflow(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_moneyflow(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `buy_sm_vol`, `buy_sm_amount`, `sell_sm_vol`, `sell_sm_amount`, `buy_md_vol`, `buy_md_amount`, `sell_md_vol`, `sell_md_amount`, `buy_lg_vol`, `buy_lg_amount`, `sell_lg_vol`, `sell_lg_amount`, `buy_elg_vol`, `buy_elg_amount`, `sell_elg_vol`, `sell_elg_amount`, `net_mf_vol`, `net_mf_amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `northbound_holdings`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/flows/northbound-holdings`
- SDK: `client.northbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_northbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `name`, `vol`, `ratio`, `exchange`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `margin`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/margin`
- SDK: `client.margin(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_margin(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `name`, `rzye`, `rqye`, `rzmre`, `rqyl`, `rzche`, `rqchl`, `rqmcl`, `rzrqye`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `block_trade`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/block-trade`
- SDK: `client.block_trade(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_block_trade(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `price`, `vol`, `amount`, `buyer`, `seller`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `top_list`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/top-list`
- SDK: `client.top_list(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_top_list(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `name`, `close`, `pct_change`, `turnover_rate`, `amount`, `l_sell`, `l_buy`, `l_amount`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `shareholders`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/shareholders`
- SDK: `client.shareholders(symbol=None, start_date=None, end_date=None, enddate=None, ann_date=None)`
- MCP: `get_shareholders(symbol=None, start_date=None, end_date=None, enddate=None, ann_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `enddate`, `ann_date`
- Response fields: `symbol`, `ann_date`, `end_date`, `holder_num`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `holder_trade`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/holder-trade`
- SDK: `client.holder_trade(symbol=None, start_date=None, end_date=None, trade_type=None, holder_type=None)`
- MCP: `get_holder_trade(symbol=None, start_date=None, end_date=None, trade_type=None, holder_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_type`, `holder_type`
- Response fields: `symbol`, `ann_date`, `holder_name`, `holder_type`, `in_de`, `change_vol`, `change_ratio`, `after_share`, `after_ratio`, `avg_price`, `total_share`, `begin_date`, `close_date`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `concepts`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/concepts`
- SDK: `client.concepts(symbol=None, start_date=None, end_date=None, trade_date=None, name=None, idx_type=None)`
- MCP: `get_concepts(symbol=None, start_date=None, end_date=None, trade_date=None, name=None, idx_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`, `name`, `idx_type`
- Response fields: `symbol`, `trade_date`, `name`, `leading`, `leading_code`, `pct_change`, `leading_pct`, `total_mv`, `turnover_rate`, `up_num`, `down_num`, `idx_type`, `level`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `concept_members`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/concept-members`
- SDK: `client.concept_members(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_concept_members(symbol=None, con_symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `con_symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `con_symbol`, `name`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `stock_list`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/reference/stocks`
- SDK: `client.stock_list(symbol=None, name=None, market=None, list_status=None, exchange=None, is_hs=None)`
- MCP: `get_stock_list(symbol=None, name=None, market=None, list_status=None, exchange=None, is_hs=None)`
- Request parameters: `symbol`, `name`, `market`, `list_status`, `exchange`, `is_hs`
- Response fields: `symbol`, `name`, `area`, `industry`, `fullname`, `enname`, `cnspell`, `market`, `exchange`, `curr_type`, `list_status`, `list_date`, `delist_date`, `is_hs`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `industry_list`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/reference/industries`
- SDK: `client.industry_list(symbol=None)`
- MCP: `get_industry_list(symbol=None)`
- Request parameters: `symbol`
- Response fields: `symbol`, `name`, `l1_code`, `l1_name`, `l2_code`, `l2_name`, `l3_code`, `l3_name`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `adj_factor`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/adj-factor`
- SDK: `client.adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `adj_factor`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `technical_factors`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/technical-factors`
- SDK: `client.technical_factors(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_technical_factors(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `open_hfq`, `close_hfq`, `high_hfq`, `low_hfq`, `pre_close_hfq`, `open_qfq`, `close_qfq`, `high_qfq`, `low_qfq`, `pre_close_qfq`, `adj_factor`, `macd_dif`, `macd_dea`, `macd`, `kdj_k`, `kdj_d`, `kdj_j`, `rsi_6`, `rsi_12`, `rsi_24`, `boll_upper`, `boll_mid`, `boll_lower`, `cci`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `limit_list`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/limit-list`
- SDK: `client.limit_list(symbol=None, start_date=None, end_date=None, trade_date=None, limit_type=None)`
- MCP: `get_limit_list(symbol=None, start_date=None, end_date=None, trade_date=None, limit_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`, `limit_type`
- Response fields: `trade_date`, `symbol`, `industry`, `name`, `close`, `pct_chg`, `amount`, `limit_amount`, `float_mv`, `total_mv`, `turnover_ratio`, `fd_amount`, `first_time`, `last_time`, `open_times`, `up_stat`, `limit_times`, `limit`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `income`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/income`
- SDK: `client.income(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)`
- MCP: `get_income(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `ann_date`, `f_ann_date`, `report_type`, `comp_type`
- Response fields: `symbol`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `comp_type`, `basic_eps`, `diluted_eps`, `total_revenue`, `revenue`, `total_cogs`, `oper_cost`, `sell_exp`, `admin_exp`, `fin_exp`, `rd_exp`, `operate_profit`, `non_oper_income`, `non_oper_exp`, `total_profit`, `income_tax`, `n_income`, `n_income_attr_p`, `ebit`, `ebitda`, `update_flag`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `balance_sheet`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/balance-sheet`
- SDK: `client.balance_sheet(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, report_type=None, comp_type=None)`
- MCP: `get_balance_sheet(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, report_type=None, comp_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `ann_date`, `report_type`, `comp_type`
- Response fields: `symbol`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `comp_type`, `total_cur_assets`, `money_cap`, `notes_receiv`, `accounts_receiv`, `inventories`, `total_nca`, `fa_avail_for_sale`, `lt_eqt_invest`, `fix_assets`, `cip`, `intan_assets`, `goodwill`, `total_assets`, `total_cur_liab`, `st_borr`, `notes_payable`, `acct_payable`, `total_ncl`, `lt_borr`, `bond_payable`, `total_liab`, `total_hldr_eqy_exc_min_int`, `total_hldr_eqy_inc_min_int`, `minority_int`, `update_flag`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `cash_flow`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/cash-flow`
- SDK: `client.cash_flow(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)`
- MCP: `get_cash_flow(symbol=None, start_date=None, end_date=None, period=None, ann_date=None, f_ann_date=None, report_type=None, comp_type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `ann_date`, `f_ann_date`, `report_type`, `comp_type`
- Response fields: `symbol`, `ann_date`, `f_ann_date`, `end_date`, `report_type`, `comp_type`, `net_profit`, `c_fr_sale_sg`, `c_pay_goods_purch_serv_rec`, `n_cashflow_act`, `c_pay_acq_const_fix_intang_oasset`, `c_fr_disp_fix_intang_oasset`, `n_cashflow_inv_act`, `c_fr_borr`, `c_pay_dist_dpcp_int_exp`, `n_cash_flows_fnc_act`, `n_incr_cash_cash_equ`, `c_cash_equ_beg_period`, `c_cash_equ_end_period`, `free_cashflow`, `update_flag`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `forecast`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/forecast`
- SDK: `client.forecast(symbol=None, start_date=None, end_date=None, period=None, type=None)`
- MCP: `get_forecast(symbol=None, start_date=None, end_date=None, period=None, type=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `type`
- Response fields: `symbol`, `ann_date`, `end_date`, `type`, `p_change_min`, `p_change_max`, `net_profit_min`, `net_profit_max`, `last_parent_net`, `first_ann_date`, `summary`, `change_reason`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `express`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/express`
- SDK: `client.express(symbol=None, start_date=None, end_date=None, period=None)`
- MCP: `get_express(symbol=None, start_date=None, end_date=None, period=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`
- Response fields: `symbol`, `ann_date`, `end_date`, `revenue`, `operate_profit`, `total_profit`, `n_income`, `total_assets`, `total_hldr_eqy_exc_min_int`, `diluted_eps`, `diluted_roe`, `yoy_net_profit`, `bps`, `perf_summary`, `update_flag`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `dividend`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/shareholders/dividend`
- SDK: `client.dividend(symbol=None, start_date=None, end_date=None, record_date=None, ex_date=None, imp_ann_date=None)`
- MCP: `get_dividend(symbol=None, start_date=None, end_date=None, record_date=None, ex_date=None, imp_ann_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `record_date`, `ex_date`, `imp_ann_date`
- Response fields: `symbol`, `end_date`, `ann_date`, `div_proc`, `stk_div`, `stk_bo_rate`, `stk_co_rate`, `cash_div`, `cash_div_tax`, `record_date`, `ex_date`, `pay_date`, `div_listdate`, `imp_ann_date`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `index_weight`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/indices/index-weight`
- SDK: `client.index_weight(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_index_weight(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `con_symbol`, `con_name`, `weight`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `technical_factors_pro`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/technical-factors-pro`
- SDK: `client.technical_factors_pro(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_technical_factors_pro(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `symbol`, `trade_date`, `open`, `open_hfq`, `open_qfq`, `high`, `high_hfq`, `high_qfq`, `low`, `low_hfq`, `low_qfq`, `close`, `close_hfq`, `close_qfq`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`, `turnover_rate`, `turnover_rate_f`, `volume_ratio`, `pe`, `pe_ttm`, `pb`, `ps`, `ps_ttm`, `dv_ratio`, `dv_ttm`, `total_share`, `float_share`, `free_share`, `total_mv`, `circ_mv`, `adj_factor`, `asi_bfq`, `asi_hfq`, `asi_qfq`, `asit_bfq`, `asit_hfq`, `asit_qfq`, `atr_bfq`, `atr_hfq`, `atr_qfq`, `bbi_bfq`, `bbi_hfq`, `bbi_qfq`, `bias1_bfq`, `bias1_hfq`, `bias1_qfq`, `bias2_bfq`, `bias2_hfq`, `bias2_qfq`, `bias3_bfq`, `bias3_hfq`, `bias3_qfq`, `boll_lower_bfq`, `boll_lower_hfq`, `boll_lower_qfq`, `boll_mid_bfq`, `boll_mid_hfq`, `boll_mid_qfq`, `boll_upper_bfq`, `boll_upper_hfq`, `boll_upper_qfq`, `brar_ar_bfq`, `brar_ar_hfq`, `brar_ar_qfq`, `brar_br_bfq`, `brar_br_hfq`, `brar_br_qfq`, `cci_bfq`, `cci_hfq`, `cci_qfq`, `cr_bfq`, `cr_hfq`, `cr_qfq`, `dfma_dif_bfq`, `dfma_dif_hfq`, `dfma_dif_qfq`, `dfma_difma_bfq`, `dfma_difma_hfq`, `dfma_difma_qfq`, `dmi_adx_bfq`, `dmi_adx_hfq`, `dmi_adx_qfq`, `dmi_adxr_bfq`, `dmi_adxr_hfq`, `dmi_adxr_qfq`, `dmi_mdi_bfq`, `dmi_mdi_hfq`, `dmi_mdi_qfq`, `dmi_pdi_bfq`, `dmi_pdi_hfq`, `dmi_pdi_qfq`, `downdays`, `updays`, `dpo_bfq`, `dpo_hfq`, `dpo_qfq`, `madpo_bfq`, `madpo_hfq`, `madpo_qfq`, `ema_bfq_10`, `ema_bfq_20`, `ema_bfq_250`, `ema_bfq_30`, `ema_bfq_5`, `ema_bfq_60`, `ema_bfq_90`, `ema_hfq_10`, `ema_hfq_20`, `ema_hfq_250`, `ema_hfq_30`, `ema_hfq_5`, `ema_hfq_60`, `ema_hfq_90`, `ema_qfq_10`, `ema_qfq_20`, `ema_qfq_250`, `ema_qfq_30`, `ema_qfq_5`, `ema_qfq_60`, `ema_qfq_90`, `emv_bfq`, `emv_hfq`, `emv_qfq`, `maemv_bfq`, `maemv_hfq`, `maemv_qfq`, `expma_12_bfq`, `expma_12_hfq`, `expma_12_qfq`, `expma_50_bfq`, `expma_50_hfq`, `expma_50_qfq`, `kdj_bfq`, `kdj_hfq`, `kdj_qfq`, `kdj_d_bfq`, `kdj_d_hfq`, `kdj_d_qfq`, `kdj_k_bfq`, `kdj_k_hfq`, `kdj_k_qfq`, `ktn_down_bfq`, `ktn_down_hfq`, `ktn_down_qfq`, `ktn_mid_bfq`, `ktn_mid_hfq`, `ktn_mid_qfq`, `ktn_upper_bfq`, `ktn_upper_hfq`, `ktn_upper_qfq`, `lowdays`, `topdays`, `ma_bfq_10`, `ma_bfq_20`, `ma_bfq_250`, `ma_bfq_30`, `ma_bfq_5`, `ma_bfq_60`, `ma_bfq_90`, `ma_hfq_10`, `ma_hfq_20`, `ma_hfq_250`, `ma_hfq_30`, `ma_hfq_5`, `ma_hfq_60`, `ma_hfq_90`, `ma_qfq_10`, `ma_qfq_20`, `ma_qfq_250`, `ma_qfq_30`, `ma_qfq_5`, `ma_qfq_60`, `ma_qfq_90`, `macd_bfq`, `macd_hfq`, `macd_qfq`, `macd_dea_bfq`, `macd_dea_hfq`, `macd_dea_qfq`, `macd_dif_bfq`, `macd_dif_hfq`, `macd_dif_qfq`, `mass_bfq`, `mass_hfq`, `mass_qfq`, `ma_mass_bfq`, `ma_mass_hfq`, `ma_mass_qfq`, `mfi_bfq`, `mfi_hfq`, `mfi_qfq`, `mtm_bfq`, `mtm_hfq`, `mtm_qfq`, `mtmma_bfq`, `mtmma_hfq`, `mtmma_qfq`, `obv_bfq`, `obv_hfq`, `obv_qfq`, `psy_bfq`, `psy_hfq`, `psy_qfq`, `psyma_bfq`, `psyma_hfq`, `psyma_qfq`, `roc_bfq`, `roc_hfq`, `roc_qfq`, `maroc_bfq`, `maroc_hfq`, `maroc_qfq`, `rsi_bfq_12`, `rsi_bfq_24`, `rsi_bfq_6`, `rsi_hfq_12`, `rsi_hfq_24`, `rsi_hfq_6`, `rsi_qfq_12`, `rsi_qfq_24`, `rsi_qfq_6`, `taq_down_bfq`, `taq_down_hfq`, `taq_down_qfq`, `taq_mid_bfq`, `taq_mid_hfq`, `taq_mid_qfq`, `taq_up_bfq`, `taq_up_hfq`, `taq_up_qfq`, `trix_bfq`, `trix_hfq`, `trix_qfq`, `trma_bfq`, `trma_hfq`, `trma_qfq`, `vr_bfq`, `vr_hfq`, `vr_qfq`, `wr_bfq`, `wr_hfq`, `wr_qfq`, `wr1_bfq`, `wr1_hfq`, `wr1_qfq`, `xsii_td1_bfq`, `xsii_td1_hfq`, `xsii_td1_qfq`, `xsii_td2_bfq`, `xsii_td2_hfq`, `xsii_td2_qfq`, `xsii_td3_bfq`, `xsii_td3_hfq`, `xsii_td3_qfq`, `xsii_td4_bfq`, `xsii_td4_hfq`, `xsii_td4_qfq`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `analyst_reports`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/analyst-reports`
- SDK: `client.analyst_reports(symbol=None, start_date=None, end_date=None)`
- MCP: `get_analyst_reports(symbol=None, start_date=None, end_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`
- Response fields: `symbol`, `name`, `report_date`, `report_title`, `report_type`, `classify`, `org_name`, `author_name`, `quarter`, `op_rt`, `op_pr`, `tp`, `np`, `eps`, `pe`, `rd`, `roe`, `ev_ebitda`, `rating`, `max_price`, `min_price`, `imp_dg`, `create_time`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `top_inst`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/top-inst`
- SDK: `client.top_inst(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_top_inst(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `exalter`, `buy`, `buy_rate`, `sell`, `sell_rate`, `net_buy`, `side`, `reason`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `southbound_holdings`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/flows/southbound-holdings`
- SDK: `client.southbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)`
- MCP: `get_southbound_holdings(symbol=None, start_date=None, end_date=None, trade_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `trade_date`
- Response fields: `trade_date`, `symbol`, `name`, `vol`, `ratio`, `exchange`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `audit`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/audit`
- SDK: `client.audit(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- MCP: `get_audit(symbol=None, start_date=None, end_date=None, period=None, ann_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`, `ann_date`
- Response fields: `symbol`, `ann_date`, `end_date`, `audit_result`, `audit_fees`, `audit_agency`, `audit_sign`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `main_business`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/main-business`
- SDK: `client.main_business(symbol=None, start_date=None, end_date=None, period=None)`
- MCP: `get_main_business(symbol=None, start_date=None, end_date=None, period=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `period`
- Response fields: `symbol`, `end_date`, `bz_item`, `bz_sales`, `bz_profit`, `bz_cost`, `curr_type`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `disclosure_date`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/financials/disclosure-date`
- SDK: `client.disclosure_date(symbol=None, start_date=None, end_date=None, pre_date=None, actual_date=None)`
- MCP: `get_disclosure_date(symbol=None, start_date=None, end_date=None, pre_date=None, actual_date=None)`
- Request parameters: `symbol`, `start_date`, `end_date`, `pre_date`, `actual_date`
- Response fields: `symbol`, `ann_date`, `end_date`, `pre_date`, `actual_date`, `modify_date`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `trade_calendar`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/reference/trade-calendar`
- SDK: `client.trade_calendar(exchange=None, start_date=None, end_date=None, is_open=None)`
- MCP: `get_trade_calendar(exchange=None, start_date=None, end_date=None, is_open=None)`
- Request parameters: `exchange`, `start_date`, `end_date`, `is_open`
- Response fields: `exchange`, `cal_date`, `is_open`, `pretrade_date`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `realtime`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/market/realtime`
- SDK: `client.realtime(symbol=None)`
- MCP: `get_realtime(symbol=None)`
- Request parameters: `symbol`
- Response fields: `symbol`, `name`, `price`, `open`, `high`, `low`, `pre_close`, `pct_chg`, `volume`, `amount`, `trade_time`
<!-- END GENERATED ASHAREHUB CONTRACT -->

## `news_flash`

<!-- BEGIN GENERATED ASHAREHUB CONTRACT -->
### Exact public contract

- REST: `GET /v2/news/flash`
- SDK: `client.news_flash(source=None, start_date=None, end_date=None, importance=None)`
- MCP: `get_news_flash(source=None, start_date=None, end_date=None, importance=None)`
- Request parameters: `source`, `start_date`, `end_date`, `importance`
- Response fields: `source`, `publish_time`, `content_cn`, `tags`, `importance`, `url`
<!-- END GENERATED ASHAREHUB CONTRACT -->
