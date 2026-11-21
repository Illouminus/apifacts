# apifacts — agent rules

Rules for coding agents working in this repository, read before the first edit. Inside this
repository this file takes precedence over generic conventions. Contributor rules live in
`CONTRIBUTING.md` and are not repeated here.

## What this is

An open registry of typed, dated facts about what third-party HTTP APIs, SDKs and CLIs actually do,
as opposed to what their docs say. Truth comes only from deterministic probes; no language model
runs in the verification path. Agents ask through `check()` (HTTP API, CLI, MCP server, pytest
plugin, GitHub Action), and the request itself is the contribution. Code MIT, data CC BY 4.0.

## Where the truth is

- `docs/PROJECT.md` — what is true now: what ships, how it runs, measured numbers with dates. Read
  it first. When it disagrees with the code or the live API (`https://apifacts.dev/healthz`,
  `/v0/services`), the code and the live API win, and you fix `PROJECT.md` in the same PR.
- `docs/specs/` — design contracts (index `docs/specs/README.md`). A behaviour change updates its
  spec in the same PR. Where a spec lags the code, the code wins; known gaps are listed in
  `docs/PROJECT.md`.
- `CONTRIBUTING.md` — fact PR rules and dev setup. `ops/README.md` — host layout, deploy, release,
  digest, kill switch. `action/README.md`, `plugins/pytest/README.md`, `skills/apifacts/SKILL.md` —
  the client surfaces.

## Stack and production

- Python 3.12 with uv; FastAPI, typer, pydantic v2, httpx, sqlite. YAML in git is the ledger:
  `services/`, `facts/`, `probes/`. `pages/` is generated and committed.
- Production: the API at `https://apifacts.dev`, served from a git checkout on one host by systemd
  user units (`ops/systemd/`), no Docker. The API reads `facts/` and `services/` only at startup.
- Merge to `main` = deployed: `.github/workflows/deploy.yml` runs after green CI on `main` and calls
  `ops/deploy.sh` (checkout, sync, restart, `/healthz`, rollback).
- Release: a tag `vX.Y.Z` on `main` publishes `apifacts` and `apifacts-pytest` to PyPI
  (`.github/workflows/release.yml`); both `__version__` values must be equal first.

## Checks

Green before a PR, the same steps as `.github/workflows/ci.yml`:

```bash
uv sync --locked
uv run ruff check .
uv run pytest -q
uv run apifacts validate
uv run apifacts pages build --check
(cd plugins/pytest && uv sync --locked && uv run pytest -q)
```

After editing `services/` or `facts/`, run `uv run apifacts pages build` and commit `pages/`. Tests
never call the live API.

## Sensitive zones

A change in these needs a maintainer's go-ahead before code
(`docs/specs/09-work-breakdown.md`, "Process for every package", step 5):

- ingestion rules and thresholds: `apifacts/api/` (`normalize.py`, `match.py`, `ratelimit.py`,
  `store.py`, `schema.sql`) and `apifacts/quorum/`;
- code that reads keys: `apifacts/probe/keys.py`, `apifacts/probe/google_sa.py`,
  `apifacts/probe/oauth_refresh.py`, `apifacts/bot/token.py`;
- `ops/publish-policy.yaml`;
- deploy and release: `.github/workflows/deploy.yml`, `.github/workflows/release.yml`,
  `ops/deploy.sh`, `ops/systemd/`, `ops/Caddyfile.facts`;
- anything that costs money.

The invariants in `docs/specs/00-architecture.md`, "Invariants", are enforced by tests (no LLM in
the verification path: `tests/api/test_no_llm.py`; typed fixes only; default-deny ingestion).
Changing one is a spec change.

## Project rules

The numbers live in these files; read them there.

- What `check()` accepts, stores, drops and rate-limits: `docs/specs/03-check-contract.md`,
  "Server-side processing (default-deny)" and "Design parameters".
- When observations become a `reported` draft, how the bot batches PRs, when it auto-merges:
  `docs/specs/05-ingestion-quorum-bot.md`, "Quorum", "Bot", "Abuse controls".
- What may be published outward: `ops/publish-policy.yaml` (`rules`, `templates`); the batch and
  its single tap: `docs/specs/08-ops-autonomy.md`, "Weekly digest".
- What an agent decides alone, what needs a maintainer's tap, what is message-only:
  `docs/specs/08-ops-autonomy.md`, "Autonomy split".
- Fact content, evidence and scope: `CONTRIBUTING.md`, "Rules for a fact pull request" and
  "Out of scope". Probes, budgets and key injection: `docs/specs/04-probe-runner.md`.

## Maintainers

Repository owner: Illouminus. Maintainer-side agents also follow the private part of this codex:
`AGENTS.md` in the private `apifacts-internal` repository.
