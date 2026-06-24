# Concept Members — Concept Index Constituents

## Background

This endpoint returns **which specific stocks belong to a given concept**. See the `concepts` endpoint for a full explanation of how Chinese theme/concept indices work and why they're important in the A-share market.

### When to use this endpoint
- **Find tradable members**: Once you identify a hot concept (via `concepts`), use this endpoint to get its constituent stocks for deeper analysis or filtering.
- **Cross-membership analysis**: Find stocks that belong to multiple hot concepts simultaneously — these often outperform during rotation.
- **Membership changes**: Concepts add/remove stocks over time as relevance shifts. Track changes to identify stocks newly designated as "concept members".

### Key fields explained
- **`symbol`**: The concept index code (parent).
- **`con_symbol`**: The constituent stock code (member).
- **`name`**: Constituent stock name (Chinese).
- **`trade_date`**: The date this membership was recorded — important since memberships can change over time.

### Caveats
- A single stock can be a member of dozens of concepts simultaneously.
- Membership is decided by the data vendor (Eastmoney) based on their own rules — not all concepts are equally "pure".


## SDK Method

```python
client.concept_members(symbol=None, con_symbol=None, start_date=None, end_date=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: trade_date, symbol, con_symbol, name. Returns empty DataFrame if no data.

## Example

```python
df = client.concept_members(symbol="TS2", limit=5)
print(df[["con_symbol", "name"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Concept index code, e.g. `BK0425.DC` |
| `con_symbol` | str | None | Stock code filter, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYY-MM-DD |
| `end_date` | str | None | End date, YYYY-MM-DD |
| `limit` | int | 100 | Max rows, up to 5000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `trade_date` | Trading date |
| `symbol` | Concept index code |
| `con_symbol` | Constituent stock code |
| `name` | Stock name |

## Data Coverage

- From: 2025-04-28
- Use concepts endpoint first to find concept codes, then query members here
- API path: `GET /v2/market/concept-members`
