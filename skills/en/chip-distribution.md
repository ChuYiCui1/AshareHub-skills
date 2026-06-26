# Chip Distribution — Cost Basis & Winner Rate

## Background — A China-Specific Technical Analysis

**"Chip distribution" (筹码分布)** is a technical analysis concept widely used in China but rare in Western markets. It models how shares are distributed across different cost basis levels among holders, treating each share as a "chip" held at the price it was bought.

### What it tracks
For each stock on each day, it estimates:
- The distribution of historical purchase prices (cost basis) of all current holders
- What percentage of holders are currently in profit vs. loss
- The "average cost" of all holders weighted by holding amount

### Why investors use this
- **Resistance from "trapped" holders**: If many holders bought at a higher price, those price levels become natural resistance — they want to "break even and exit". Use `cost_85pct` (85th percentile cost) to spot resistance.
- **Support at heavy positions**: Densely-held cost levels act as support. The `weight_avg` (volume-weighted average cost) is often watched.
- **Sentiment via winner_rate**: When `winner_rate` is very high (>80%), most holders are profitable — they may take profits. Very low (<20%) means most are underwater — capitulation may be near.

### Key fields explained
- **`weight_avg`**: Volume-weighted average cost of all current holders (CNY).
- **`winner_rate`**: % of total shares currently in profit (0–100).
- **`cost_5pct`, `cost_15pct`, `cost_50pct`, `cost_85pct`, `cost_95pct`**: Percentile cost basis. E.g. `cost_50pct` is the median holder's cost.
- **`his_low` / `his_high`**: Historical lowest/highest cost in the chip distribution.

### Caveats for foreign investors
- This is a **statistical model**, not actual holding records — it's reconstructed from historical volume and price.
- Particularly popular among Chinese retail technical analysts. Less common in institutional research.
- Most useful for understanding short-term sentiment and identifying psychological levels.


## SDK Method

```python
client.chip_distribution(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, weight_avg, winner_rate, cost_5pct, etc. Returns empty DataFrame if no data.

## Example

```python
df = client.chip_distribution(symbol="000001.SZ", limit=3)
print(df[["trade_date", "weight_avg", "winner_rate"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol`, `trade_date` | Stock code and date |
| `his_low`, `his_high` | Historical price extremes (CNY) |
| `cost_5pct` | 5th percentile cost basis (CNY) |
| `cost_15pct` | 15th percentile cost basis (CNY) |
| `cost_50pct` | Median cost basis (CNY) |
| `cost_85pct` | 85th percentile cost basis (CNY) |
| `cost_95pct` | 95th percentile cost basis (CNY) |
| `weight_avg` | Weighted average cost of all holders (CNY) |
| `winner_rate` | % of holders in profit (0-100). Values > 80 suggest strong bullish momentum |

## Data Coverage

- From: 20200102
- China-specific metric for analyzing shareholder cost structure
- API path: `GET /v2/chips/distribution`
