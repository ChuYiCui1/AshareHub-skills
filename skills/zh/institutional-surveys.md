# Institutional research events

每行是一场调研事件。participant_count 表示该事件保存的参与记录数，不是去重机构数。rece_org 精确筛选包含该机构的事件，不改变完整参与记录数。日期使用 YYYYMMDD，代码使用 symbol。默认 limit=100、offset=0，上限500；按 surv_date 降序、event_id 升序分页。content 默认 null；需要完整正文时显式设置 include_content=True 且 limit≤20，否则返回422。按实际返回行数递增 offset，直到返回行数少于 limit。上游修订会改变事件哈希及分页结果，建议缩小日期区间并按 event_id 去重。新方法仅支持 V2。

## 时点回测限制

两类接口均不提供可靠的公开发布时间。month 只是推荐月份；surv_date 是调研发生日期，不等于纪要公开时间。不能仅凭这些日期进行严格时点回测，否则可能引入未来信息偏差。严格回测还需要独立核实的公开/可用时间及历史版本。

## Example

```python
events = client.institutional_surveys(start_date="20261101", limit=20)
if not events.empty:
    event_id = events.iloc[0]["event_id"]
    transcript = client.institutional_surveys(event_id=event_id, include_content=True, limit=1)
    participants = client.survey_participants(event_id=event_id, limit=1000)
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_institutional_surveys`.
