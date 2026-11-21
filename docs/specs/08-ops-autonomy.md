# 08 · Operations and autonomy

**Done when:** the four timers below run on illouminus as user units, `state/projects/agent-facts.md`
receives the weekly journal line automatically, the Monday digest arrives in Telegram with a single
"✅ Publish batch" tap for outward publications, and the kill switch stops runner + bot within one tick
(tested on the host with a dry run).

## Timers (systemd user units, `ops/systemd/`)

| Unit | Schedule | Does |
|------|----------|------|
| `agentfacts-probe.timer` | every 15 min | `apifacts probe run --due --max 50` |
| `agentfacts-quorum.timer` | hourly | `apifacts quorum run && apifacts bot publish` |
| `agentfacts-refresh.timer` | daily 03:00 Europe/Paris | `apifacts probe run --refresh-evidence` (counters → facts/, added 24.10.2026) |
| `agentfacts-pages.timer` | on merge (CI) | pages build in CI, not on the host |
| `agentfacts-digest.timer` | Mon 08:00 Europe/Paris | `ops/digest.py` → Telegram (question class, D-062) |
| `agentfacts-indexnow.timer` | daily 05:00 Europe/Paris | `ops/indexnow.py` → IndexNow ping for changed pages (after the 03:00 refresh and its deploy) |

Deploy: git checkout on the host, no image — `ops/deploy.sh` behind a forced-command SSH key: detached checkout of the merged sha, `uv sync --frozen --no-dev`, restart `agentfacts-api`, poll `/healthz`, roll back on failure.

GitHub access on the host: the bot uses only its own token `agent-facts-bot` (repo-scoped PAT, D-089);
`deploy.sh` fetches the public repo anonymously. Units carry the seccomp/prctl hardening that works for
user units; mount-namespace confinement (read-only system, per-unit key access) is impossible in user
units on illouminus and needs system units under a dedicated user (`ops/README.md` → Hardening).
API behind Caddy at `apifacts.dev` `[tap: DNS record once]`.

## Weekly digest (one message, one tap)

```
apifacts · week 44
facts: 112 (+9) · verified 71 · reported 31 · stale 4 · retracted 0
check(): 143 calls from 27 networks · 11 unregistered targets (top: api.notion.com; hosts known only for seed candidates, the rest is "other")
probes: 1 840 runs · 0 budget violations · keys missing: [hubspot-test]
needs a probe (agent-hours): 6 reported facts  → card created
quorum: 3 drafts this week → one needs-review PR at the start of the next (D-093)
publications proposed (batch #7, 4 items):
  1. stripe/stripe-python#1234 — issue: idempotency error string changed in 12.2.0 (verified prod)
  2. SO 79xxxxxx — answer: Slack "invalid_blocks" when text > 3000 (verified prod)
  3. …
[✅ Publish batch #7]  [⏭ Skip this week]
```

The report behind the ping (`state/reviews/agent-facts-<date>.md`) carries the detail: adoption
(D-092), «Читатели» — requests to `apifacts.dev` by User-Agent family over the week's UTC days,
grouped as AI agents (live fetch: ChatGPT-User, Claude-User, Perplexity-User…), AI crawlers, search
engines, scripts, browsers, our own clients, with the path-class split per family (spec 03,
«Readers»; no paths are kept, so no per-page top) — dogfooding, check(), probes. The ping stays at
8 lines; readers are in the report only.

Rules for the batch (decision 2026-10-20): templates and the vendor list are pre-approved in
`ops/publish-policy.yaml`; every item links a `verified:*` fact; no vendor opinions, no vulnerabilities;
the tap publishes all items, a skip keeps them for the next batch; nothing is ever published without
the tap.

## Autonomy split (decision 2026-10-20)

| Agent decides alone | Needs Edouard's tap | Message only (no question) |
|---------------------|---------------------|----------------------------|
| new facts and statuses, probe schedules, pages, plugin releases, keyless services, kill switch, "needs a probe" cards | money (any paid resource, budget overrun), new accounts/keys on third-party services, changes to ingestion rules (`03`, `05` thresholds), the weekly publication batch | account ban / ToS change, key rotation needed, vendor complaint, kill switch triggered |

## Budgets

| Budget | Value |
|--------|-------|
| Edouard | 2–3 h once (seed list, accounts via `keyput`, repo public, DNS); then ~10–15 min/week |
| Agent | W0–W8 ≈ 2–3 sessions; run ≈ 1 agent-hour/week (unmeasured estimate) |
| Money | $0 target for wave 1: free tiers and sandboxes; CI minutes on the private repo until public |

## Megabrain state

`projects/agent-facts.md` journal (newest first) gets a line per merged W-package and per weekly digest;
cards in `state/tasks/` for "needs a probe" (machine: vps) and for the taps (waiting_edouard). Commits
only via `bin/state-commit --as agent-facts <paths>`.
