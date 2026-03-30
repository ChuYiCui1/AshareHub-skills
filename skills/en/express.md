# Earnings Express — Flash Reports

## SDK Method

```python
client.express(ts_code=None, start_date=None, end_date=None, limit=50, offset=0)
```

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `ts_code` | str | None | Stock code, e.g. `000001.SZ` |
| `start_date` | str | None | Announcement start date, YYYY-MM-DD |
| `end_date` | str | None | Announcement end date, YYYY-MM-DD |
| `limit` | int | 50 | Max rows, up to 1000 |
| `offset` | int | 0 | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| `ts_code` | Stock code |
| `ann_date` | Announcement date |
| `end_date` | Fiscal period end |
| `revenue` | Revenue (CNY) |
| `operate_profit` | Operating profit (CNY) |
| `total_profit` | Profit before tax (CNY) |
| `n_income` | Net income (CNY) |
| `total_assets` | Total assets (CNY) |
| `diluted_eps` | Diluted EPS (CNY) |
| `diluted_roe` | Diluted ROE % |
| `yoy_net_profit` | Net profit YoY growth % |
| `bps` | Book value per share (CNY) |
| `perf_summary` | Performance summary |

## Notes

- Flash reports are released before formal financial statements
- API path: `GET /v1/financials/express`
