# AShareHub Skills for Claude Code

Official Claude Code skills for querying Chinese A-share market data via [AShareHub](https://asharehub.com).

## Prerequisites

```bash
pip install asharehub
export ASHAREHUB_API_KEY="ash_your_key_here"
```

Get your free API key at [asharehub.com/console/register](https://asharehub.com/console/register).

## Installation

Copy the skills into your project's `.claude/skills/` directory:

```bash
# Clone this repo
git clone https://github.com/ChuYiCui1/asharehub-skills.git

# Copy skills to your project
cp asharehub-skills/skills/*.md /path/to/your/project/.claude/skills/
```

## Available Skills

| Skill | Command | Description |
|-------|---------|-------------|
| Market Daily | `/market-daily` | Daily OHLC price data (2020+, 7.3M records) |
| Market Fundamentals | `/market-fundamentals` | PE, PB, turnover, market cap (2010+, 13.6M records) |
| Northbound Flows | `/northbound-flows` | Stock Connect capital flows (2014+) |
| Chip Distribution | `/chip-distribution` | Cost basis & winner rate analysis |
| FX Daily | `/fx-daily` | Foreign exchange rates (default USD/CNH) |
| Index Daily | `/index-daily` | Major index OHLC (SSE, CSI 300, ChiNext) |
| Financial Indicators | `/financial-indicators` | 50+ quarterly metrics (ROE, EPS, margins) |

## Usage

In Claude Code, type a slash command:

```
/market-daily 000001.SZ 2024-01-01 2024-12-31
/northbound-flows 2024-01-01 2024-03-31
/index-daily 000300.SH
```

## Also Available

- **Python SDK**: `pip install asharehub` — [Documentation](https://asharehub.com/docs)
- **MCP Server**: Connect AI assistants via `https://asharehub.com/mcp/sse`
- **REST API**: 7 endpoints at `https://asharehub.com/v1/`

## License

MIT
