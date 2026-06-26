# News Flash — Real-time Financial News

## SDK Method

```python
client.news_flash(source, start_date=None, end_date=None, importance=None, limit=100, offset=0)
```

## Returns

`pd.DataFrame` — columns: source, publish_time, content_cn, tags, importance, url. Returns empty DataFrame if no data.

## Example

```python
# Important 财联社 flashes only
df = client.news_flash(source="cls", importance=1, limit=10)
print(df[["publish_time", "content_cn"]])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| source | str | **Yes** | Feed: `cls` (财联社, A-share focused), `jin10` (金十, global macro), `sina` (新浪, mixed). One source per call. |
| start_date | str | No | YYYYMMDD, filters publish_time |
| end_date | str | No | YYYYMMDD |
| importance | int | No | Only items with importance >= this value (e.g. `1` = important only) |
| limit | int | No | Max rows (default 100, max 5000) |
| offset | int | No | Pagination offset |

## Response Fields

| Field | Description |
|-------|-------------|
| source | News source (cls / jin10 / sina) |
| publish_time | Publish timestamp |
| content_cn | Flash content — **Chinese** |
| tags | Category tags (nullable) |
| importance | Importance flag, 0 / 1 (nullable) |
| url | Source article URL (nullable) |

## Notes

- Content is **Chinese only** (`content_cn`); there is no English translation field.
- `source` is required. The three sources report the same events independently, so query
  one source at a time — merging them would produce near-duplicate news.
- Ordered newest first. Continuously updated during (and around) market hours.
