# Concept Constituents — Concept Sector Constituents

## Background

This endpoint returns **which specific stocks belong to a given concept**. See the `concepts` endpoint for a full explanation of how Chinese theme/concept indices work and why they're important in the A-share market.

### When to use this endpoint
- **Find tradable members**: Once you identify a hot concept (via `concepts`), use this endpoint to get its constituent stocks for deeper analysis or filtering.
- **Cross-membership analysis**: Find stocks that belong to multiple hot concepts simultaneously — these often outperform during rotation.
- **Membership changes**: Concepts add/remove stocks over time as relevance shifts. Track changes to identify stocks newly designated as "concept members".

### Key fields explained
- **`bk_code`**: The Eastmoney concept sector code (parent).
- **`con_code`**: The constituent stock code; this source field name is preserved.
- **`name`**: Constituent stock name (Chinese).
- **`trade_date`**: The date this membership was recorded — important since memberships can change over time.

### Caveats
- A single stock can be a member of dozens of concepts simultaneously.
- Membership is decided by the data vendor (Eastmoney) based on their own rules — not all concepts are equally "pure".


## SDK Method

```python
client.concept_members(bk_code=None, con_code=None, start_date=None, end_date=None, trade_date=None)
```

## Returns

`pd.DataFrame` — columns: trade_date, bk_code, con_code, name. Returns empty DataFrame if no data.

## Example

```python
df = client.concept_members(bk_code="BK0425.DC", con_code="000001.SZ")
print(df[["con_code", "name"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `bk_code` | str | None | Eastmoney concept sector code, e.g. `BK0425.DC` |
| `con_code` | str | None | Constituent stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Start date, YYYYMMDD |
| `end_date` | str | None | End date, YYYYMMDD |
| `trade_date` | str | None | Trading date YYYYMMDD (single day) |

## Response Fields

| Field | Description |
|-------|-------------|
| `trade_date` | Trading date |
| `bk_code` | Eastmoney concept sector code |
| `con_code` | Constituent stock code |
| `name` | Stock name |

## Data Coverage

- From: 20250428
- Use concepts endpoint first to find concept codes, then query members here
- API path: `GET /v2/market/concept-members`
