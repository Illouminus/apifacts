# ops — apifacts on illouminus (W8)

Spec: `docs/specs/08-ops-autonomy.md`. No Docker: a git checkout of this repo at
`~/apps/agent-facts`, detached at the deployed sha, with its own `.venv` (`uv sync --frozen
--no-dev`). Nothing in ops calls an LLM.

| Path on the host | What |
|------------------|------|
| `~/apps/agent-facts/` | checkout (detached HEAD = deployed sha) |
| `var/results.jsonl`, `var/probe-state.sqlite` | probe runs and budgets (spec 04) |
| `var/evidence-pending.sqlite`, `var/evidence-refresh.json` | counters waiting for the daily refresh, its marker |
| `var/bot-state.json` | day and refresh of the last "daily evidence refresh" PR |
| `var/observations.sqlite` | check() observations and counters (spec 03) |
| `var/readers/<day>.json` | requests by User-Agent family × path class × status class (below, «Readers») |
| `var/deploy/` | `deployed` (sha), `deploy.log`, parked `facts-unapplied-*.patch` |
| `var/publications.jsonl` | published items (once the publish policy is approved) |
| `var/sitemap-lastmod.json` | per page: hash of its substance and its sitemap `lastmod` (written by the API at startup) |
| `var/indexnow.json` | URLs and `lastmod` last accepted by IndexNow, the last run's answer |
| `ops/KILL` | kill switch file (gitignored) |
| `~/.config/systemd/user/agentfacts-*` | symlinks to `ops/systemd/` (`systemctl --user link`) |

| Unit | When | Enabled |
|------|------|---------|
| `agentfacts-api.service` | always, `127.0.0.1:8795`, 1 worker, no access log | yes |
| `agentfacts-probe.timer` | every 15 min, `probe run --due --max 50 --vantage illouminus` | yes |
| `agentfacts-digest.timer` | Monday 08:00 Europe/Paris, `ops/digest.py` | yes |
| `agentfacts-refresh.timer` | daily 03:00 Europe/Paris, `probe run --refresh-evidence` | by hand after the deploy that adds it |
| `agentfacts-quorum.timer` | hourly, quorum + bot (own token, verified-only auto-merge) | after the D-089 PR |
| `agentfacts-indexnow.timer` | daily 05:00 Europe/Paris, `ops/indexnow.py` | by hand after the deploy that adds it |

## First install (once)

```bash
gh repo clone Illouminus/apifacts ~/apps/agent-facts      # public repository
cd ~/apps/agent-facts && git checkout --detach origin/main
~/.local/bin/uv sync --frozen --no-dev && mkdir -p var
export XDG_RUNTIME_DIR=/run/user/$(id -u)                     # over non-interactive ssh
for u in ops/systemd/agentfacts-*; do systemctl --user link "$PWD/$u"; done
systemctl --user enable --now agentfacts-api.service
curl -s 127.0.0.1:8795/healthz
.venv/bin/apifacts probe run --all --vantage illouminus --root .   # first run, before the timer
systemctl --user enable --now agentfacts-probe.timer          # one call per unit
systemctl --user enable --now agentfacts-digest.timer
```

Units are links into the checkout: when `ops/systemd/` changes, `ops/deploy.sh` links unit files
that are not linked yet and runs `daemon-reload`; enabling a new unit stays a deliberate step
(`systemctl --user enable --now agentfacts-refresh.timer`).

## Deploy

On merge, `.github/workflows/deploy.yml` (after CI succeeds on `main`) ssh-es the sha to a forced
command; nothing else can run with that key:

```
command="/home/ubuntu/apps/agent-facts/ops/deploy.sh",restrict ssh-ed25519 AAAA… gha-deploy-agent-facts
```

Test the restriction over the public OpenSSH port (Tailscale SSH on `ssh illouminus` ignores
`authorized_keys`): `ssh -F /dev/null -i <key> -p <port> ubuntu@<public ip> <sha>`.

Over ssh only a sha ahead of the deployed one is accepted (no downgrade with a leaked key). By
hand: `~/apps/agent-facts/ops/deploy.sh <40-hex sha on origin/main>`, any sha on main, so this is
also the rollback. Exit 1 = rolled back (prod alive on the old sha), 3 = rollback failed too.

The API loads `facts/` and `services/` only at startup. A bare `git pull` / `git checkout` in
`~/apps/agent-facts` leaves it answering from the old registry until `systemctl --user restart
agentfacts-api` — `deploy.sh` always restarts, so prefer it. `/healthz` → `registry_version` shows
which registry is served; `probes_last_run` is read from `var/results.jsonl` on each call (no
restart needed after a probe tick).

The probe runner writes `facts/` in place on a status change, a new vantage and the daily refresh;
until the bot publishes those edits, `deploy.sh` carries them across checkouts as a patch, and
parks a patch that no longer applies in `var/deploy/` instead of dropping it. The journal hook
(`ops/state_journal.py --prev`) writes a megabrain line only when a deploy changes what the
registry says (new, removed or re-statused facts, claims), never for counters or code.

## Bot token

The bot (`apifacts bot publish`) talks to GitHub only with its own fine-grained PAT, Contents +
Pull requests on this repository: `keyput agent-facts-bot` → `~/.private_keys/agent-facts-bot.key`
(D-089). `gh` gets it as `GH_TOKEN`; git push/fetch/ls-remote get it through an env-only credential
helper that first resets `~/.gitconfig`'s `gh auth git-credential` (the owner's login, every
repository). Missing file → `error: no bot token …`, exit 1, nothing pushed. `deploy.sh` fetches
the public repo with `-c credential.helper=` (anonymous).

## Hardening

Every `agentfacts-*.service` sets `NoNewPrivileges`, `RestrictSUIDSGID`, `LockPersonality`,
`RestrictRealtime`, `RestrictNamespaces`, `SystemCallArchitectures=native`,
`SystemCallFilter=@system-service` (`EPERM`), `MemoryDenyWriteExecute` and `RestrictAddressFamilies`
(unix, inet, inet6, netlink) — checked on the host 2026-10-24 (`NoNewPrivs: 1`, `Seccomp: 2`; probe,
quorum, bot dry runs, uvicorn, gh, git and HTTPS work under it). No `UMask`: the digest writes into
the megabrain state, whose files other readers expect group/world-readable.

Impossible in user units on illouminus (Ubuntu 24.04, systemd 255,
`kernel.apparmor_restrict_unprivileged_userns=1`): the user manager's user namespace lands in the
`unprivileged_userns` AppArmor profile without `CAP_SYS_ADMIN`, so there is no mount namespace.
`ProtectSystem`, `ProtectHome`, `PrivateTmp`, `ReadWritePaths`, `InaccessiblePaths`, `ProtectProc`,
`ProtectKernelTunables`, `ProtectControlGroups` are silently ignored; `PrivateUsers`,
`PrivateDevices`, `TemporaryFileSystem`, `BindReadOnlyPaths`, `ProtectClock` make the unit fail with
`226/NAMESPACE` ("Failed to set up mount namespacing: Operation not supported"). Hence no read-only
filesystem and no per-unit key access: every unit runs as `ubuntu` and could read all of
`~/.private_keys`. Way out (root, Edouard's call): system units with `User=apifacts`, a dedicated
user whose own keys directory holds only the apifacts keys (mount namespaces work for system
units); lifting the AppArmor restriction would weaken the whole host and is not proposed.

Check a property before adding it: `systemd-run --user --pipe --wait -p <Property>=… /bin/sh -c 'grep -E "NoNewPrivs|Seccomp" /proc/self/status'`.

## IndexNow

Changed pages go to IndexNow (Bing and the engines that share its submissions) once a day; the
sitemap's `lastmod` moves only on a change of substance (spec 06), so a refresh-only night submits
nothing. After the deploy that adds the units:

```bash
curl -s https://apifacts.dev/robots.txt | tail -1                    # Sitemap: https://apifacts.dev/sitemap.xml
curl -s https://apifacts.dev/sitemap.xml | head -4                   # urlset, one <url> per page
curl -s https://apifacts.dev/$(.venv/bin/python -c 'from apifacts.api.site import INDEXNOW_KEY as k; print(k)').txt
.venv/bin/python ops/indexnow.py --dry-run                           # first run: every page
systemctl --user enable --now agentfacts-indexnow.timer
```

`journalctl --user -u agentfacts-indexnow` shows `submitted N URLs (HTTP 200|202)`; 202 = key
validation pending, 403 = the key file is not reachable at `https://apifacts.dev/<key>.txt`
(check Caddy), 422 = a URL outside the host. `var/indexnow.json` → `last_run` keeps the answer.
Resubmit everything: move `var/indexnow.json` away. Optionally add the sitemap in Bing Webmaster
Tools (import from Google Search Console) to see crawl stats; not needed for IndexNow.

## Kill switch

```bash
touch ~/apps/agent-facts/ops/KILL     # next probe tick exits before its first request
rm ~/apps/agent-facts/ops/KILL
```

`APIFACTS_KILL=1` in a unit's environment does the same. The API keeps answering.

## Digest

```bash
.venv/bin/python ops/digest.py --dry-run             # last complete week, print only
.venv/bin/python ops/digest.py --dry-run --current   # this week so far
```

A real run writes `~/claude-hub/state/reviews/agent-facts-<date>.md`, a journal entry and (if
reported facts lack a probe) a card, commits them with `bin/state-commit --as agent-facts`, and
pings Telegram through the gateway (`send_telegram`, class `digest`, `X-Routine:
agent-facts-digest`). Publications stay "policy not approved" until `ops/publish-policy.yaml`
says `approved: true` (Edouard's tap). The report also carries the adoption line (below) and
PyPI downloads without mirrors for `apifacts` and `apifacts-pytest` over the same week
(pypistats `overall`; its newest day lags, so a Monday run may miss Sunday).

## Adoption

The gate number of D-092 (gate 30.11: ≥ 10 external clients in 23–29.11, or ≥ 1 external stored
observation):

```bash
.venv/bin/apifacts stats adoption --db var/observations.sqlite   # last complete salt period
# external_clients=N calls=M reported_external=K   (exit 1: the db has no traffic table yet)
```

- **External** = the caller's IP is not ours. Ours = loopback, private ranges, and the nets in
  `APIFACTS_OWN_NETS` (comma-separated) or `var/own-nets.txt` (one IP/CIDR per line, `#`
  comments; outside git, the addresses are private): the VPS public address, the home exit,
  a dev machine. Decided **at request time**: raw IPs are never kept and last week's salt is
  deleted on rotation, so "ours" cannot be subtracted afterwards. The file is read at startup.
- Not by User-Agent: our skill and plugins send the same UA as everyone's. GitHub Actions is
  not excluded either (its nets are shared with every outside CI); our CI tests never call the
  live API.
- **Client** = a network (/16, IPv6 /32) within one salt period; **calls** = every answered
  `POST /v0/check`, pre-flight included (a count per network, no target — Q5 still keeps
  pre-flight out of `observations`); **reported_external** = observations stored from them.
- Table `traffic`, one row per network per period; rows older than the previous period go at
  the salt rotation.

## Readers

Who reads `apifacts.dev` (site and API), by User-Agent family — the only trace, since there is no
access log (spec 03, «Readers»):

```bash
.venv/bin/apifacts stats readers --dir var/readers --days 7   # today included, partial
```

- `var/readers/<YYYY-MM-DD>.json` (UTC day): `{family: {path_class: {status_class: n}}}`, merged
  by the API every 5 minutes and at shutdown (lock + temp file + rename). A file that does not
  parse is set aside as `<day>.json.bad`. `APIFACTS_READERS_DIR` overrides the place.
- Families are a fixed ordered table in `apifacts/api/readers.py` (`FAMILIES`): a new bot is one
  row. A UA is a claim, not verified (no IP is kept). `apifacts-*` = our client software,
  whoever runs it — not our hosts (that is adoption's job, above).
- The weekly digest has the «Читатели» section (report only; the ping is full).

## Caddy

`ops/Caddyfile.facts` is appended to `/etc/caddy/Caddyfile`. Check with `caddy adapt`, not `caddy
validate` (validate instantiates log files as root and breaks the next reload), then
`sudo systemctl reload caddy`. `apifacts.dev` and `www` have A records to the host (OVH DNS);
`facts.baillot.dev` (the `*.baillot.dev` wildcard) is a 308 redirect to it. Certificates come on the
first reload: `curl -s https://apifacts.dev/healthz`.

## Release to PyPI

`apifacts` (this repository's root) and `apifacts-pytest` (`plugins/pytest`) carry the same version
and ship together from one tag. No PyPI token exists anywhere: `.github/workflows/release.yml`
exchanges the job's GitHub OIDC token for a short-lived upload token at PyPI (trusted publishing).
Each project on PyPI needs that publisher registered once, by the account owner, with exactly these
values (for a project that does not exist yet: "Add a pending publisher"). The environment differs
per package because PyPI binds one pending publisher per (owner, repository, workflow, environment)
to a single project name:

| Field | `apifacts` | `apifacts-pytest` |
|-------|------------|-------------------|
| PyPI project name | `apifacts` | `apifacts-pytest` |
| Owner | `Illouminus` | `Illouminus` |
| Repository name | `apifacts` | `apifacts` |
| Workflow name | `release.yml` | `release.yml` |
| Environment name | `pypi` | `pypi-pytest` |

Cutting a release:

1. Set the same `__version__` in `apifacts/__init__.py` and `plugins/pytest/apifacts_pytest/__init__.py`
   (`tests/ops/test_release_workflow.py` keeps them equal), PR, merge.
2. `git tag vX.Y.Z <merge commit> && git push origin vX.Y.Z`. The workflow refuses a tag whose commit is
   not on `main` or whose version differs from either package; then one job per package builds it (the
   `apifacts` wheel carries the offline snapshot: `services/` and `facts/` as of that commit), runs
   `twine check` and uploads. Re-running a half-done release is safe (PyPI ignores files it already has).
3. Check https://pypi.org/project/apifacts/ and https://pypi.org/project/apifacts-pytest/;
   `uvx apifacts version` prints the new version.
