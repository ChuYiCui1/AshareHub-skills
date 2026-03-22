# AShareHub Skills & Prompt Templates

Query Chinese A-share market data via [AShareHub](https://asharehub.com). Works with Claude Code, Cursor, Windsurf, Cline, and any AI coding assistant.

**Languages:** [English](#english) | [中文](#中文)

## Prerequisites

```bash
pip install asharehub
export ASHAREHUB_API_KEY="ash_your_key_here"
```

Get your free API key at [asharehub.com/console/register](https://asharehub.com/console/register).

## Structure

```
skills/
├── en/                         # English
│   ├── SKILL.md                # Main entry — routes to the right data doc
│   ├── market-daily.md         # Daily OHLC prices (2020+, 7.3M records)
│   ├── market-fundamentals.md  # PE, PB, turnover, market cap (2010+, 13.6M records)
│   ├── northbound-flows.md     # Stock Connect capital flows (2014+)
│   ├── chip-distribution.md    # Cost basis & winner rate (2020+, 7.3M records)
│   ├── fx-daily.md             # FX rates, default USD/CNH (2012+)
│   ├── index-daily.md          # Major index OHLC (2010+)
│   └── financial-indicators.md # 50+ quarterly metrics (ROE, EPS, margins)
└── zh/                         # 中文
    ├── SKILL.md
    └── ... (same files in Chinese)
```

## How to Use

### Claude Code

Copy your preferred language into your project:

```bash
# English
cp -r skills/en/ /path/to/your/project/.claude/skills/asharehub/

# 中文
cp -r skills/zh/ /path/to/your/project/.claude/skills/asharehub/
```

Then invoke with `/asharehub` in Claude Code.

### Other AI assistants

Each `.md` file is a self-contained reference doc with SDK method, parameters, and response fields. Paste into your assistant's context or reference directly.

## All Access Methods

| Method | How to Connect |
|--------|---------------|
| **Python SDK** | `pip install asharehub` — [Docs](https://asharehub.com/docs) |
| **MCP Server** | `https://asharehub.com/mcp/sse` — works with Claude Desktop, Cursor, etc. |
| **REST API** | 7 endpoints at `https://asharehub.com/v1/` |
| **Skills** | This repo |

## License

MIT
