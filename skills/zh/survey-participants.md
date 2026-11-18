# Research participant records

每行是关联事件的一条参与记录，不是一场独立调研，也不代表一个去重机构。用 institutional_surveys 查询事件数与正文。支持 symbol、起止日期 YYYYMMDD、event_id、精确 rece_org 和 org_type 筛选。默认 limit=100、offset=0，上限1000；按调研日期降序、event_id 和 participant_id 升序分页。正文不会在机构行中重复返回。递增 offset 直到返回行数少于 limit；上游更新期间建议缩小日期范围。仅支持 V2。

## Example

```python
participants = client.survey_participants(start_date="20261101", limit=100, offset=0)
print(participants.head())
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_survey_participants`.
