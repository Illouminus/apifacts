# apifacts — what is true now

The one status document of this repository. Every number carries the date it was measured and its
source. Changing what ships, how it runs or a measured number: update this file in the same PR.

## What it is, for whom

An open registry of typed, dated facts about what third-party HTTP APIs, SDKs and CLIs actually do,
verified by deterministic probes. For AI coding agents (and their humans) that hit an API error and
need the verified difference between the docs and reality. Code MIT, data CC BY 4.0.

## What ships

Measured 2026-11-21 on `main` at `34101bd` (source: the repository tree).

| Surface | Where | Version |
|---------|-------|---------|
| `apifacts` library + CLI (`check`, `scan`, `validate`, `pages`, `probe`, `quorum`, `bot`, `stats`, `mcp`) | repository root, PyPI | 0.3.0 (`apifacts/__init__.py`) |
| pytest plugin `apifacts-pytest` | `plugins/pytest/`, PyPI | 0.3.0 |
| MCP server (one tool, `check`, stdio) | `apifacts/mcp_server.py`, `server.json` (`io.github.Illouminus/apifacts`) | 0.3.0 |
| GitHub Action (`apifacts scan` on a failing step) | `action/`, used as `Illouminus/apifacts/action@v0` | tag `v0` |
| Agent skill | `skills/apifacts/SKILL.md` | — |
| HTTP API and fact pages | `https://apifacts.dev` | — |

Release tags in the repository (2026-11-21): `v0.1.0`, `v0.2.0`, `v0.2.1`, `v0.3.0`, `v0`.
Not built: the jest plugin and a client sandbox for `verified:client` facts (spec 07, spec 09 W9).

## How it runs

- Stack: Python 3.12, uv, FastAPI, typer, pydantic v2, httpx, sqlite (`pyproject.toml`).
- Production: a git checkout on one host, systemd user units in `ops/systemd/`: `agentfacts-api`
  (service) and the timers `probe`, `quorum`, `refresh`, `digest`, `indexnow`. No Docker.
  Details: `ops/README.md`.
- Deploy: merge to `main` → CI green → `.github/workflows/deploy.yml` → `ops/deploy.sh`.
- Release: tag `vX.Y.Z` on `main` → `.github/workflows/release.yml` → PyPI (trusted publishing).
- Workflows (2026-11-21): `ci.yml`, `deploy.yml`, `release.yml`.

## Measured

| What | Value | Date | Source |
|------|-------|------|--------|
| Services registered | 15 | 2026-11-21 | `services/*.yaml` |
| Facts | 211 | 2026-11-21 | `facts/**/*.yaml` |
| Facts by status | verified:server:prod 135 · verified:server:sandbox 38 · official 37 · stale 1 · reported 0 | 2026-11-21 | `status:` in `facts/` |
| Facts by kind | error_meaning 69 · silent_behavior 52 · auth_quirk 35 · rate_limit 20 · deprecation 12 · pagination 11 · schema_drift 4 · availability 3 · breaking_change 3 · latency_profile 1 · sandbox_divergence 1 | 2026-11-21 | `kind:` in `facts/` |
| Probe files | 140 in 15 services | 2026-11-21 | `probes/**/*.yaml` |
| Generated pages | 308 Markdown files | 2026-11-21 | `pages/` |
| Test files | 82 | 2026-11-21 | `tests/`, `plugins/pytest/tests/` |
| Live API | `/healthz` ok, `registry_version` 2026-11-15; `/v0/services` 15 services, 211 facts | 2026-11-21 | `https://apifacts.dev` |

Facts per service (2026-11-21, `facts/<service>/`): github 29 · stripe 26 · google-sheets 20 ·
google-firestore 18 · salesforce 18 · google-gemini 17 · pypi 16 · telegram 16 · google-calendar 14 ·
solana 14 · anthropic 5 · npm-registry 5 · openai 5 · linear 4 · resend 4.

Usage (external `check()` callers, downloads, readers): not measured in this repository; the
weekly digest computes it on the host (`ops/README.md`, "Adoption", "Readers").

## Where specs lag the code

Found 2026-11-21; the code is right until the spec is fixed.

- `docs/specs/08-ops-autonomy.md`, "Timers": omits `agentfacts-indexnow.timer`. Its deploy line names a GHCR image; deploy is a git checkout without an image (`ops/README.md`,
  spec 00 "Stack and why").
- `docs/specs/00-architecture.md`, "Repository layout": lists `plugins/jest/` and `docs/` with plan,
  decisions, research and panels; neither is in this repository.
- `docs/specs/07-plugins.md`: the MCP server is `apifacts/mcp_server.py`, not `apifacts/mcp`.
- `CONTRIBUTING.md`, "Development setup": CI already runs `apifacts validate`,
  `apifacts pages build --check` and the pytest plugin's own tests (`.github/workflows/ci.yml`).
- `docs/specs/README.md` says the repository "will be public"; it is public. `ops/README.md`,
  "First install", calls the repository private.
