# 港股 — 股票列表、交易日历与未复权日线

## SDK 方法

```python
client.hk_stock_list(symbol=None, list_status=None)
client.hk_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
client.hk_trade_calendar(start_date=None, end_date=None, is_open=None)
```

所有方法返回 `pd.DataFrame`。港股代码必须是五位数字加 `.HK` 后缀，并保留前导零，例如 `00700.HK`。

## 示例

```python
stocks = client.hk_stock_list(list_status="L")
daily = client.hk_daily(
    symbol="00700.HK",
    start_date="20260101",
    end_date="20260807",
)
calendar = client.hk_trade_calendar(
    start_date="20260101",
    end_date="20261231",
    is_open=1,
)
```

## 日线字段与单位

`symbol`、`trade_date`、`open`、`high`、`low`、`close`、`pre_close`、`change`、`pct_chg`、`vol`、`amount`。

- 价格和 `amount` 的单位为港元。
- `vol` 的单位为股，不是手。
- 价格为原始未复权行情。
- 当前不提供港股复权因子，不能把 A 股 `adj_factor()` 用到 `.HK` 代码上。

## 股票列表字段

`symbol`、`name`、`fullname`、`enname`、`cn_spell`、`market`、`list_status`、`list_date`、`delist_date`、`trade_unit`、`isin`、`curr_type`。

## 交易日历字段

`exchange`、`cal_date`、`is_open`、`pretrade_date`。

## API 路径

- `GET /v2/hk/basic`
- `GET /v2/hk/daily`
- `GET /v2/hk/trade-calendar`
