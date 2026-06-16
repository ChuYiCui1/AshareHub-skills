# 财经快讯 — 实时新闻快讯

## SDK 方法

```python
client.news_flash(source, start_date=None, end_date=None, importance=None, limit=100, offset=0)
```

## 返回

`pd.DataFrame` — 列：source, publish_time, content_cn, tags, importance, url。无数据时返回空 DataFrame。

## 示例

```python
# 只看财联社的重要快讯
df = client.news_flash(source="cls", importance=1, limit=10)
print(df[["publish_time", "content_cn"]])
```

## 参数

| 名称 | 类型 | 必填 | 说明 |
|------|------|------|------|
| source | str | **是** | 来源：`cls`(财联社，偏 A 股)、`jin10`(金十，偏全球宏观)、`sina`(新浪，综合)。每次查一个源。 |
| start_date | str | 否 | YYYY-MM-DD，按 publish_time 过滤 |
| end_date | str | 否 | YYYY-MM-DD |
| importance | int | 否 | 只看重要度 ≥ 该值(如 `1` = 只看重要) |
| limit | int | 否 | 最大行数(默认 100，最大 5000) |
| offset | int | 否 | 分页偏移 |

## 返回字段

| 字段 | 说明 |
|------|------|
| source | 来源(cls / jin10 / sina) |
| publish_time | 发布时间 |
| content_cn | 快讯正文 —— **中文** |
| tags | 分类标签(可空) |
| importance | 重要度 0 / 1(可空) |
| url | 原文链接(可空) |

## 说明

- 正文**仅中文**(`content_cn`)，无英文翻译字段。
- `source` 必填。三个源会各自独立报道同一事件，所以每次只查一个源——合并会产生大量近重复。
- 按时间倒序(最新在前)，盘中及前后持续更新。
