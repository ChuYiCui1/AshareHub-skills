# AShareHub Prompt Templates

Universal prompt templates for querying Chinese A-share market data via [AShareHub](https://asharehub.com). Works with any AI coding assistant — Claude Code, Cursor, Windsurf, Cline, and more.

## Prerequisites

```bash
pip install asharehub
export ASHAREHUB_API_KEY="ash_your_key_here"
```

Get your free API key at [asharehub.com/console/register](https://asharehub.com/console/register).

## Available Templates

| Template | Description | Data Range |
|----------|-------------|------------|
| [Market Daily](skills/market-daily.md) | Daily OHLC price data | 2020+, 7.3M records |
| [Market Fundamentals](skills/market-fundamentals.md) | PE, PB, turnover, market cap | 2010+, 13.6M records |
| [Northbound Flows](skills/northbound-flows.md) | Stock Connect capital flows | 2014+ |
| [Chip Distribution](skills/chip-distribution.md) | Cost basis & winner rate | 2020+, 7.3M records |
| [FX Daily](skills/fx-daily.md) | Foreign exchange rates (USD/CNH) | 2012+ |
| [Index Daily](skills/index-daily.md) | Major index OHLC (SSE, CSI 300, ChiNext) | 2010+ |
| [Financial Indicators](skills/financial-indicators.md) | 50+ quarterly metrics (ROE, EPS, margins) | Quarterly |

## How to Use

### With any AI assistant

Each template contains ready-to-use Python code. Simply paste the code into your AI assistant's context or ask it to reference the template.

### As Claude Code skills

```bash
# Copy to your project's skills directory
cp skills/*.md /path/to/your/project/.claude/skills/
```

### As Cursor/Windsurf rules

Reference the templates in your `.cursorrules` or `.windsurfrules` file, or paste the content directly.

## All Access Methods

| Method | How to Connect |
|--------|---------------|
| **Python SDK** | `pip install asharehub` — [Docs](https://asharehub.com/docs) |
| **MCP Server** | `https://asharehub.com/mcp/sse` — works with Claude Desktop, Cursor, etc. |
| **REST API** | 7 endpoints at `https://asharehub.com/v1/` |
| **Prompt Templates** | This repo |

## License

MIT
