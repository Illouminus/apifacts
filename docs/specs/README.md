# Specs (v0.1, 2026-10-20)

Design contracts for the first build. English on purpose: the repository is public and read by
agents and contributors worldwide; the internal history (plan, decisions, panels) stays in Russian.

| # | File | What it fixes |
|---|------|---------------|
| 00 | [00-architecture.md](00-architecture.md) | Components, repo layout, stack, data flow, invariants |
| 01 | [01-fact-schema.md](01-fact-schema.md) | The fact record: identity, kind, dimensions, status, evidence |
| 02 | [02-fix-vocabulary.md](02-fix-vocabulary.md) | Closed enumeration of typed fixes (no free text, no shell) |
| 03 | [03-check-contract.md](03-check-contract.md) | `POST /v0/check`: request = contribution; default-deny ingestion |
| 04 | [04-probe-runner.md](04-probe-runner.md) | Declarative probes, vantage points, budgets, key injection, kill switch |
| 05 | [05-ingestion-quorum-bot.md](05-ingestion-quorum-bot.md) | Observations → quorum → probe → bot commit |
| 06 | [06-pages.md](06-pages.md) | Static fact pages keyed by exact error strings |
| 07 | [07-plugins.md](07-plugins.md) | pytest plugin (wave 1), jest plugin and MCP server (wave 2) |
| 08 | [08-ops-autonomy.md](08-ops-autonomy.md) | Timers on illouminus, weekly digest, what needs a human tap |
| 09 | [09-work-breakdown.md](09-work-breakdown.md) | Work packages W0–W9 with acceptance criteria, branches, order |

Conventions: every spec states **Done when** up front; numbers that are design parameters are listed in
one table per spec so they can be tuned without rewriting prose; anything a human must do is marked
`[tap]`. Decisions these specs implement: `docs/decisions.md` in the private repository apifacts-internal (2026-10-17 … 2026-10-20).
