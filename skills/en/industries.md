# Industry Classification — Shenwan Industries

## SDK Method

```python
client.industry_list(symbol=None)
```

## Returns

`pd.DataFrame` — columns: symbol, name, l1_code, l1_name, l2_code, l2_name, l3_code, l3_name. Returns empty DataFrame if no data.

## Example

```python
df = client.industry_list(symbol="000001.SZ")
print(df[["symbol", "l1_name", "l2_name", "l3_name"]])
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `symbol` | str | None | Stock code, e.g. `000001.SZ` |

## Response Fields

| Field | Description |
|-------|-------------|
| `symbol` | Stock ticker |
| `name` | Stock name |
| `l1_code` | L1 industry code |
| `l1_name` | L1 industry name (31 industries) |
| `l2_code` | L2 industry code |
| `l2_name` | L2 industry name |
| `l3_code` | L3 industry code |
| `l3_name` | L3 industry name |

## Data Coverage

- Static reference data (SW2021 standard)
- API path: `GET /v2/reference/industries`
