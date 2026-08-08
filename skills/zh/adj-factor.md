# 复权因子

## SDK 方法

```python
client.adj_factor(symbol=None, start_date=None, end_date=None, trade_date=None)
```

## 返回类型

`pd.DataFrame` — 数值列为 `float64`。无数据时返回空 DataFrame。

## 示例

```python
df = client.adj_factor(symbol="000001.SZ")
print(df[["trade_date", "adj_factor"]])
```

## 参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `symbol` | str | None | 股票代码，如 `000001.SZ` |
| `start_date` | str | None | 起始日期，YYYYMMDD |
| `end_date` | str | None | 结束日期，YYYYMMDD |
| `trade_date` | str | None | 交易日期，YYYYMMDD（查单日） |

## 返回字段

| 字段 | 说明 |
|------|------|
| `symbol` | 股票代码 |
| `trade_date` | 交易日期 |
| `adj_factor` | 复权因子 |

## 复权计算

将 `client.market_daily()` 返回的未复权价格记为 `P(t)`，将本接口返回的复权因子记为 `F(t)`。调用方必须选择锚点交易日 `T`：取不晚于目标 `end_date` 的最后一个交易日；未指定 `end_date` 时，取最新可用交易日。

```text
不复权价格 = P(t)
前复权价格 = P(t) × F(t) / F(T)
后复权价格 = P(t) × F(t)
```

前复权满足 `前复权价格(T) = P(T)`。同一历史日期使用不同的锚点 `T`，前复权价格可能不同；后复权价格不依赖查询锚点。

```python
daily = client.market_daily(
    symbol="000001.SZ", start_date="20240101", end_date="20241231"
)
factor = client.adj_factor(
    symbol="000001.SZ", start_date="20240101", end_date="20241231"
)

df = daily.merge(factor, on=["symbol", "trade_date"], how="inner")
anchor_factor = df.sort_values("trade_date").iloc[-1]["adj_factor"]
df["close_qfq"] = df["close"] * df["adj_factor"] / anchor_factor
df["close_hfq"] = df["close"] * df["adj_factor"]
```

## 使用规则

- 对 `open`、`high`、`low`、`close` 使用相同公式；不要复权 `vol` 和 `amount`。
- 不要从被分页或截断的结果中误取“最后一行”作为锚点；应确保已经取得 `T` 当日的 `F(T)`。
- 用户指定“截至某日”时，以该日或该日前最后交易日为锚点，不要擅自改用全局最新交易日。
- `technical_factors()` 中的 `*_qfq` 是数据源在该记录最近刷新时按其最新交易日锚定的预计算快照。需要指定历史锚点或严格复现时，使用日线原始价与本接口因子自行计算。
- 新的除权事件或数据源修订可能更新复权因子；缓存的前复权序列应同步重算。
- API 路径：`GET /v2/market/adj-factor`
