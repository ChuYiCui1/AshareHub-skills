# Broker monthly stock picks

每行对应月份、券商、股票的唯一组合。月度金股区别于 analyst_reports 的券商盈利预测。支持 month（YYYYMM）、精确 broker、symbol 筛选；省略 month 查询全部已存月份。默认 limit=100、offset=0，上限1000；按月份降序、券商和代码升序分页。递增 offset 直到返回行数少于 limit。非法月份和不带交易所后缀的代码返回422。仅支持 V2。

## Example

```python
offset = 0
while True:
    page = client.broker_recommendations(month="202611", limit=100, offset=offset)
    print(page)
    if len(page) < 100:
        break
    offset += len(page)
```

Read `api-contract.md` for all request parameters and response fields. MCP tool: `get_broker_recommendations`.
