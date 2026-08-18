<div align="center">

# AShareHub Skills

**AI-powered access to Chinese A-share and ETF market data**

[![PyPI](https://img.shields.io/pypi/v/asharehub.svg)](https://pypi.org/project/asharehub/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Skill Website](https://asharehub.com/en/skill) · [API Docs](https://asharehub.com/en/docs) · [Get API Key](https://asharehub.com/en/console/register)

**English** | [中文](README_ZH.md)

</div>

---

## Overview

Official skills and reference docs for querying Chinese A-share market data via [AShareHub](https://asharehub.com). Compatible with Claude Code, Cursor, Windsurf, Cline, and any AI coding assistant.

### Related AShareHub resources

- [China stock MCP server](https://asharehub.com/en/docs/mcp-setup) for hosted, tool-based access from AI agents
- [China stock API for AI agents](https://asharehub.com/en/skill) with reusable Agent Skill instructions
- [China stock data Python SDK](https://asharehub.com/en/docs/sdk-install) for notebooks, research and backend services
- [A-share market data API](https://asharehub.com/en/docs/market-daily), [China ETF data API](https://asharehub.com/en/docs/etf-basic) and [China financial data API](https://asharehub.com/en/docs/financials)
- [China stock API pricing](https://asharehub.com/en/console/pricing), [authentication](https://asharehub.com/en/docs#authentication) and [rate limits](https://asharehub.com/en/docs#rate-limits)

## Prerequisites

```bash
pip install asharehub
export ASHAREHUB_API_KEY="ash_your_key_here"
```

Get your free API key at [asharehub.com/en/console/register](https://asharehub.com/en/console/register).

## Available Data

| Skill | Description | Data Range |
|-------|-------------|------------|
| [Market Daily](skills/en/market-daily.md) | Daily OHLC prices, volume, returns | 2020+ |
| [Market Fundamentals](skills/en/market-fundamentals.md) | PE, PB, turnover rate, market cap | 2010+ |
| [HSGT Capital Flows](skills/en/moneyflow-hsgt.md) | Stock Connect capital flows | 2014+ |
| [Chip Distribution](skills/en/chip-distribution.md) | Cost basis percentiles, winner rate | 2020+ |
| [FX Daily](skills/en/fx-daily.md) | Foreign exchange rates (USD/CNH) | 2012+ |
| [Index Daily](skills/en/index-daily.md) | SSE Composite, CSI 300, ChiNext | 2010+ |
| [Financial Indicators](skills/en/financial-indicators.md) | ROE, EPS, margins, 50+ metrics | Quarterly |

## Installation

### Claude Code

```bash
git clone https://github.com/ChuYiCui1/asharehub-skills.git
cp -r asharehub-skills/skills/en/ /path/to/your/project/.claude/skills/asharehub/
```

Then invoke with `/asharehub` in Claude Code.

### Other AI Assistants

Each `.md` file is a self-contained reference with SDK method signature, parameters, and response fields. Paste into your assistant's context or reference directly.
Use [`api-contract.md`](skills/en/api-contract.md) for the generated, exact contract covering all 47 interfaces and every response field.

## Project Structure

```
skills/
├── en/                         # English
│   ├── SKILL.md                # Main entry point
│   ├── api-contract.md         # Generated exact 47-interface contract
│   ├── market-daily.md
│   ├── market-fundamentals.md
│   ├── moneyflow-hsgt.md
│   ├── chip-distribution.md
│   ├── fx-daily.md
│   ├── index-daily.md
│   └── financial-indicators.md
└── zh/                         # 中文
    ├── SKILL.md
    └── ...
```

## All Access Methods

| Method | Description |
|--------|-------------|
| **Python SDK** | `pip install asharehub` — [Documentation](https://asharehub.com/en/docs) |
| **MCP Server** | [Cloud setup](https://asharehub.com/en/docs#mcp-setup) — Claude Desktop, Cursor, etc. |
| **REST API** | 47 endpoints — [API documentation](https://asharehub.com/en/docs) |
| **Skills** | This repository — [official skill page](https://asharehub.com/en/skill) |

## License

[MIT](LICENSE)
