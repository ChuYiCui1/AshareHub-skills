# Institutional research events

Count research events with `institutional_surveys`, not participant rows. Each event has an `event_id` and `participant_count`; the count includes all stored participant records, not unique institutions. `rece_org` selects events with that exact participant institution and does not change the count.

Use `symbol`, `start_date` and `end_date` (YYYYMMDD), or `event_id` to narrow results. Defaults: `limit=100`, `offset=0`; maximum limit 500. Order: research date descending, event id ascending. Increment offset by the number of returned rows until a page has fewer than limit rows. Concurrent source revisions can change offset pages; use narrow date windows and deduplicate by event id. Event ids may change after source transcript revisions.

`content` is null by default and is not loaded from storage. Request `include_content=True, limit=20` or less for full transcripts. A larger limit with content returns 422. Empty results return `[]` (an empty SDK DataFrame). These are V2-only endpoints; SDK `version="v1"` rejects these new methods.

## Point-in-time limitations

Neither dataset exposes a reliable public release timestamp. `month` labels a recommendation month; `surv_date` records the meeting date, not when its transcript became public. Do not use either date alone for strict point-in-time backtests: doing so can introduce look-ahead bias. Such backtests require independently verified publication/availability timestamps and historical source versions.

## Example

```python
events = client.institutional_surveys(start_date="20261101", limit=20)
if not events.empty:
    event_id = events.iloc[0]["event_id"]
    transcript = client.institutional_surveys(event_id=event_id, include_content=True, limit=1)
    participants = client.survey_participants(event_id=event_id, limit=1000)
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_institutional_surveys`.
