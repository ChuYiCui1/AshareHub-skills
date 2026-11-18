# Research participant records

每行是关联事件的一条参与记录，不是一场独立调研，也不代表一个去重机构。用 institutional_surveys 查询事件数与正文。支持 symbol、起止日期 YYYYMMDD、event_id、精确 rece_org 和 org_type 筛选。默认 limit=100、offset=0，上限1000；按调研日期降序、event_id 和 participant_id 升序分页。正文不会在机构行中重复返回。递增 offset 直到返回行数少于 limit；上游更新期间建议缩小日期范围。仅支持 V2。

## 时点回测限制

两类接口均不提供可靠的公开发布时间。month 只是推荐月份；surv_date 是调研发生日期，不等于纪要公开时间。不能仅凭这些日期进行严格时点回测，否则可能引入未来信息偏差。严格回测还需要独立核实的公开/可用时间及历史版本。

## Example

```python
participants = client.survey_participants(start_date="20261101", limit=100, offset=0)
print(participants.head())
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_survey_participants`.
