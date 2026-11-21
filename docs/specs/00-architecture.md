# 00 · Architecture

**Done when:** every component below exists as a directory with its own tests, the data flow runs
end-to-end on illouminus for the wave-1 services, and no component calls an LLM.

## Components

```
                    ┌──────────────────────────┐
  agents / tests ──▶│  check() service (FastAPI)│──▶ observations.sqlite
  (pytest plugin,   │  POST /v0/check           │
   curl, MCP later) │  GET  /v0/facts/{service} │◀── facts/ (YAML, git)
                    └──────────────────────────┘
                                 │ quorum job (hourly)
                                 ▼
                    ┌──────────────────────────┐      ┌───────────────┐
                    │  probe runner (timer)     │◀────▶│ target APIs    │
                    │  probes/*.yaml, budgets   │      │ (prod/sandbox) │
                    └──────────────────────────┘      └───────────────┘
                                 │ results.jsonl
                                 ▼
                    ┌──────────────────────────┐
                    │  bot: facts → PR → merge  │──▶ pages/ (markdown) → github.com / Pages
                    └──────────────────────────┘
```

| Component | Package / path | Runs where | Wave |
|-----------|----------------|------------|------|
| Schemas + validator | `apifacts/schema`, `schema/*.json`, CLI `apifacts validate` | CI, dev | W1 |
| Probe runner | `apifacts/probe`, `probes/<service>/*.yaml` | illouminus timer (later prod-VPS, Freebox) | W2 |
| check() service | `apifacts/api` (FastAPI + uvicorn) | illouminus, behind Caddy | W3 |
| Quorum + bot | `apifacts/quorum`, `apifacts/bot` | illouminus timer | W4 |
| Pages generator | `apifacts/pages` → `pages/` | CI on merge | W5 |
| pytest plugin | `plugins/pytest/` (package `apifacts-pytest`) | user's test run | W6 |
| Seed content | `services/*.yaml`, `facts/*/*.yaml`, `probes/*/*.yaml` | git | W7 |
| Ops | `ops/systemd/*`, `ops/digest.py`, `ops/deploy.sh` | illouminus | W8 |
| MCP server | `apifacts/mcp_server.py` (`apifacts mcp`, extra `apifacts[mcp]`) | agent host | W9 |
| jest plugin | planned, not in this repository yet | user's test run | W9 |

## Repository layout

```
apifacts/
  README.md            # public English README (the Russian idea doc lives in apifacts-internal)
  LICENSE (MIT) · LICENSE-DATA (CC BY 4.0)
  pyproject.toml       # package apifacts, uv-managed, Python 3.12
  apifacts/          # library + CLI (typer)
  schema/              # JSON Schema 2020-12: fact, service, probe, observation, fix
  services/<service>.yaml
  facts/<service>/<slug>.yaml
  probes/<service>/<slug>.yaml
  pages/               # generated, committed (deterministic output)
  plugins/pytest/
  ops/
  tests/
  docs/                # PROJECT.md (current state), specs/
  .github/workflows/ci.yml
```

## Stack and why

- **Python 3.12 + uv + pytest + ruff + typer + pydantic v2 + httpx + FastAPI + sqlite.** One language for
  runner, API, bot, pages and the pytest plugin; the team is one agent, so no polyglot core. TypeScript only
  for the jest plugin and the MCP server (W9).
- **YAML in git is the ledger.** One fact per file, deterministic key order (ruamel round-trip), so diffs
  are reviewable and the bot's PRs are small. sqlite holds only transient state (observations, probe
  results, budgets); losing it loses nothing verified.
- **GitHub Actions for CI only** (lint, tests, schema validation, pages build). Repo goes public at the
  end of W7 `[tap]`: public repos have free minutes; until then CI stays under ~2 min per run (D-076).
- **Deploy to illouminus** with the portfolio's `vps-auto-deploy` pattern minus the image (W8): git checkout at the merged sha + `uv sync --frozen`, forced-command SSH → `ops/deploy.sh` with health check and rollback. API behind Caddy at `apifacts.dev` (domain `[tap]`).

## Invariants (enforced in code, tested)

1. No LLM call in any verification path: the runner, API, quorum and bot have no model API keys in their
   environment; a test asserts no `openai|anthropic|google-genai` import in those packages.
2. Fixes are enum members from `02-fix-vocabulary.md`; schema validation rejects anything else.
3. Ingestion is default-deny: a request whose `target` does not match a registered service template is
   answered with facts (if any) but **not stored**.
4. Probe keys are injected by name from `~/.private_keys/<name>.key` into the runner only; never into
   repository files, logs, pages or contributor sandboxes. Secret-shaped strings are redacted by a
   filter before any write.
5. A probe in a different `env` or `account_state` never refutes a fact; it adds a dimension row.
6. Budgets: ≤ 1 request / 5 min per (service, endpoint template, vantage); global kill switch
   `ops/KILL` file or `APIFACTS_KILL=1` stops the runner and the bot within one tick.
7. Published aggregates only at k ≥ 3 distinct reporter networks (/16) per observation key.

## Data flow in one paragraph

A probe runs on a timer, records a result (status, headers whitelist, body fingerprint, latency, error
string if any) and, where a fact already references that probe, confirms or marks it stale. A `check()`
call from any agent returns the matching facts and typed fixes and, if the target matches a template,
stores a normalized observation. The hourly quorum job groups observations; a group that meets quorum
becomes a `reported` fact draft and, if a probe template exists for that endpoint and signal, schedules a
probe; a confirming probe upgrades the draft to `verified:server:<env>`. The bot opens one PR per batch of
new or changed facts; CI validates schemas and regenerates pages; the merge bot merges when green. The
weekly digest proposes outward publications in one batch for one tap.
