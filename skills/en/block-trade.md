# Block Trade — Off-Exchange Large Deals

## SDK Method

```python
client.block_trade(symbol=None, start_date=None, end_date=None, trade_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: symbol, trade_date, price, vol, amount, buyer, seller. Returns empty DataFrame if no data.

## Example

```python
df = client.block_trade(symbol="000001.SZ", limit=3)
print(df[["trade_date", "price", "vol", "buyer", "seller"]])
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
| `symbol` | Stock code |
| `trade_date` | Trading date |
| `price` | Trade price (CNY) |
| `vol` | Volume (10k shares) |
| `amount` | Amount (10k CNY) |
| `buyer` | Buyer broker name |
| `seller` | Seller broker name |

## Data Coverage

- From: 20100104
- Large institutional transactions above regular trading limits
- API path: `GET /v2/market/block-trade`
