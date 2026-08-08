# Adjustment Factor — Forward/Backward Price Restoration

## SDK Method

```python
client.adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, adj_factor. Returns empty DataFrame if no data.

## Example

```python
df = client.adj_factor(symbol="000001.SZ")
print(df[["trade_date", "adj_factor"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock code |
| `trade_date` | Trading date |
| `adj_factor` | Adjustment factor |

## Adjustment formulas

Let `P(t)` be an unadjusted price returned by `client.market_daily()` and `F(t)` the adjustment factor returned by this endpoint. The caller must choose an anchor trading date `T`: use the last trading day on or before the target `end_date`; when `end_date` is omitted, use the latest available trading day.

```text
Unadjusted price = P(t)
Forward-adjusted price = P(t) × F(t) / F(T)
Backward-adjusted price = P(t) × F(t)
```

Forward adjustment guarantees `adjusted_price(T) = P(T)`. The same historical date can therefore have different forward-adjusted prices under different anchors, while backward-adjusted prices do not depend on the query anchor.

```python
daily = client.market_daily(
    symbol="000001.SZ", start_date="20240101", end_date="20241231"
)
factor = client.adj_factor(
    symbol="000001.SZ", start_date="20240101", end_date="20241231"
)

df = daily.merge(factor, on=["symbol", "trade_date"], how="inner")
anchor_factor = df.sort_values("trade_date").iloc[-1]["adj_factor"]
df["close_qfq"] = df["close"] * df["adj_factor"] / anchor_factor
df["close_hfq"] = df["close"] * df["adj_factor"]
```

## Usage rules

- Apply the same formulas to `open`, `high`, `low`, and `close`; do not adjust `vol` or `amount`.
- Do not mistake the last row of a paginated or truncated response for the anchor. Ensure that `F(T)` for the chosen anchor date was fetched.
- When the user asks for data "as of" a date, anchor to that date or the preceding trading day instead of silently using the global latest date.
- The `*_qfq` fields from `technical_factors()` are source-precomputed snapshots using the latest trading-day anchor available at the record's last refresh. For a historical anchor or strict reproducibility, calculate from raw daily prices and this endpoint's factors.
- A new corporate action or a source correction can revise adjustment factors; recompute cached forward-adjusted series accordingly.
- API path: `GET /v2/market/adj-factor`
