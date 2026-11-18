# Research participant records

Each row represents one stored participant record associated with an event. Multiple rows can belong to the same institution or event. Do not present row counts as research event counts or unique institution counts. Query `institutional_surveys` for event-level counts and transcripts.

Filter by `symbol`, `start_date`, `end_date` (YYYYMMDD), `event_id`, exact `rece_org`, or exact `org_type`. Defaults: `limit=100`, `offset=0`; maximum limit 1000. Order: research date descending, event id ascending, participant id ascending. Increment offset until fewer than limit rows are returned. No transcript is duplicated into participant responses. Use narrow date windows for reproducible paging across source updates. V2 only.

## Point-in-time limitations

Neither dataset exposes a reliable public release timestamp. `month` labels a recommendation month; `surv_date` records the meeting date, not when its transcript became public. Do not use either date alone for strict point-in-time backtests: doing so can introduce look-ahead bias. Such backtests require independently verified publication/availability timestamps and historical source versions.

## Example

```python
participants = client.survey_participants(start_date="20261101", limit=100, offset=0)
print(participants.head())
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_survey_participants`.
