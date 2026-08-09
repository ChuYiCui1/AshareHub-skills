# Hong Kong Stocks — Directory, Calendar and Raw Daily Bars

## SDK methods

```python
client.hk_stock_list(symbol=None, list_status=None)
client.hk_daily(symbol=None, start_date=None, end_date=None, trade_date=None)
client.hk_trade_calendar(start_date=None, end_date=None, is_open=None)
```

All methods return `pd.DataFrame`. Hong Kong symbols use five digits plus `.HK`; preserve leading zeroes, for example `00700.HK`.

## Examples

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

## Daily response

`symbol`, `trade_date`, `open`, `high`, `low`, `close`, `pre_close`, `change`, `pct_chg`, `vol`, `amount`.

- Prices and `amount` are in HKD.
- `vol` is shares, not board lots.
- Prices are raw and unadjusted.
- Hong Kong adjustment factors are not currently available. Never substitute the A-share `adj_factor()` result for a `.HK` symbol.

## Stock directory response

`symbol`, `name`, `fullname`, `enname`, `cn_spell`, `market`, `list_status`, `list_date`, `delist_date`, `trade_unit`, `isin`, `curr_type`.

## API paths

- `GET /v2/hk/basic`
- `GET /v2/hk/daily`
- `GET /v2/hk/trade-calendar`
