# Show HN launch package

Status: **draft, not published.** Nothing here goes out before the maintainer's decision on the
adoption gate of 2026-11-30. The post is submitted by the maintainer, from his own account.

Written 2026-11-23 against `main` at `663cc5f`: 15 services, 211 facts (`docs/PROJECT.md`,
"Measured"). External `check()` callers on 2026-11-23: 0 (weekly digest, week 47).

## 1. Registry to ~30 services before the post

The post only works if a reader's first `check()` against an API they use returns a fact. Today the
registry covers 15 services; 11 declare auth and 7 of them need a real key (Stripe, Salesforce,
Google Workspace, ...), which a reader cannot reproduce in 30 seconds. The additions below are all **keyless**: anonymous GETs,
reproducible by anyone with `curl`, probed by the existing runner with `auth: {kind: none}` (same
shape as `services/pypi.yaml` and `services/npm-registry.yaml`).

Selection: public APIs that coding agents call without a key and that answer with traps (redirects,
HTML instead of JSON, silent caps, rate limits reported oddly). The routine dogfood log is not a
source here: its 45 failures of 2026-11-02 were all `api.github.com` contents 404s, closed by #118.

Estimate per service = service YAML with ToS fields + 6–10 probes + facts + `pages build`, measured
against the pypi (10 probes, 16 facts) and npm-registry seeds. Keys follow `apifacts/api/seed_hosts.py`
(`SEED_HOSTS`), where 12 of the 15 are already listed. Three are not — `go-proxy`
(proxy.golang.org, sum.golang.org), `osv` (api.osv.dev), `deps-dev` (api.deps.dev) — and
`tests/api/test_registered_services_hosts_are_listed` fails until they are added there; that step is
in their hours (+0.5 each). `apifacts/api/` is a sensitive zone (`AGENTS.md`): adding seed hosts
goes in the same PR as the service, with the maintainer's go-ahead.

| # | Service (`key`) | Host(s) | Likely facts to probe | ToS / policy to cite | Agent-hours |
|---|-----------------|---------|-----------------------|----------------------|-------------|
| 1 | crates.io (`crates-io`) | crates.io, index.crates.io | 403 without a User-Agent; sparse index vs API; 404 body shape | crates.io data access policy (1 req/s, UA required) | 2 |
| 2 | Docker Hub registry (`docker-hub`) | registry-1.docker.io, auth.docker.io, hub.docker.com | anonymous pull token dance; 401 + `WWW-Authenticate` before any pull; `ratelimit-*` headers; 429 `TOOMANYREQUESTS` | Docker Hub usage and limits | 3 |
| 3 | Hugging Face Hub (`huggingface`) | huggingface.co | gated repo 401 vs 403 vs 404; `resolve/` redirect to CDN; `X-Error-Code` header | Hub API docs, ToS | 3 |
| 4 | Go module proxy (`go-proxy`) | proxy.golang.org, sum.golang.org | case-encoding `!x` in paths; 404 vs 410 for gone versions; `@latest` | proxy.golang.org privacy/policy | 2.5 |
| 5 | Maven Central (`maven-central`) | repo1.maven.org, search.maven.org, central.sonatype.com | search API `rows` cap; metadata XML vs JSON; 404 for missing POM | Sonatype Central terms | 2 |
| 6 | RubyGems (`rubygems`) | rubygems.org | `/api/v1/gems/{name}.json` 404 is plain text; rate limit 429 | RubyGems API docs (rate limits) | 2 |
| 7 | OSV.dev (`osv`) | api.osv.dev | `querybatch` returns ids only; ecosystem name case sensitivity; empty `{}` on no vulns | OSV API docs | 2.5 |
| 8 | deps.dev (`deps-dev`) | api.deps.dev | URL-encoding of package names; 404 vs empty; v3 vs v3alpha | deps.dev API terms | 2.5 |
| 9 | Wikipedia / MediaWiki (`wikipedia`) | en.wikipedia.org | errors are HTTP 200 with `error` in body; `maxlag`; UA policy 403; REST vs Action API | Wikimedia User-Agent policy, API etiquette | 3 |
| 10 | Wikidata SPARQL (`wikidata`) | query.wikidata.org | 60 s timeout returned as 500 with Java stack text; 429 + `Retry-After`; UA required | WDQS user manual, usage policy | 2 |
| 11 | OpenStreetMap Nominatim (`nominatim`) | nominatim.openstreetmap.org | 403 without a valid UA; empty array for no match; `format` default HTML | Nominatim usage policy (1 req/s, no bulk) | 2 |
| 12 | Open-Meteo (`open-meteo`) | api.open-meteo.com | 400 with `{"error":true,"reason":...}`; silent clamp of forecast days; daily-limit 429 | Open-Meteo terms (non-commercial free tier) | 2 |
| 13 | arXiv API (`arxiv`) | export.arxiv.org | Atom XML only; errors as a feed entry with HTTP 200; `max_results` cap; 3 s politeness | arXiv API terms of use | 2 |
| 14 | Crossref (`crossref`) | api.crossref.org | 404 is plain text `Resource not found.`; deep paging needs `cursor`; polite pool via `mailto` | Crossref REST API etiquette | 2 |
| 15 | Hacker News API (`hacker-news`) | hacker-news.firebaseio.com, hn.algolia.com | missing item is HTTP 200 with `null`; Algolia `hitsPerPage` cap 1000 total | HN API README; Algolia HN Search terms | 2 |

Total: about 34.5 agent-hours, no keys, no money. All 15 are new probes ("probe needed"); none exists in
`probes/` today. Order: 9, 4, 1, 2, 3 first (largest agent audiences), the rest as time allows. 25
services is the floor for posting (D-092: 25–30), so the post can go with 10 of the 15.

Out of the list on purpose: APIs that now need a key for any call (CoinGecko, exchangerate.host,
Reddit JSON since 2023 policy changes, Twitter/X).

## 2. Show HN draft

Title (≤ 80 characters; 79):

> Show HN: Apifacts – verified facts about what APIs really do, for coding agents

Alternatives:

- `Show HN: A registry of API behaviour that contradicts the docs, probe-checked` (77)
- `Show HN: Apifacts – when your agent hits a 4xx, ask what the API really does` (76)

URL field: `https://apifacts.dev` (the page lists services and facts; the repository link is in the
comment).

First comment (author), plain text, posted right after submission:

> Hi HN. Coding agents keep paying for the same API surprises: a 404 that means "private repo", a
> trailing slash that turns JSON into a 301 with an HTML body, a per_page that is silently capped
> at 100. The docs either do not say it or say something else, and every session rediscovers it.
>
> apifacts is an open registry of those differences as typed, dated facts. Each fact is produced by
> a deterministic probe (declarative HTTP steps plus assertions, run on a schedule); no language
> model is anywhere in the verification path. A fix is a member of a closed vocabulary rendered to
> one sentence, never free text.
>
> Try it in 30 seconds, no account:
>
>     uvx apifacts check https://pypi.org/pypi/requests/json/ -X GET --status 301
>
> or add it to Claude Code: `claude mcp add apifacts -- uvx --from 'apifacts[mcp]' apifacts mcp`.
> There is also a pytest plugin that prints the known facts when a test fails on an HTTP error, and
> a GitHub Action that does the same for a red CI step.
>
> Calling check() is also how the registry learns: if the target matches a known endpoint template,
> a normalized observation is stored (no bodies, headers, query strings or raw IPs). Enough
> independent observations turn into a draft fact that a probe then has to confirm.
>
> Today: N services (GitHub, PyPI, npm, Stripe, ...) and M facts. Code MIT, data
> CC BY 4.0: https://github.com/Illouminus/apifacts
>
> What I would like to know: which API burns your agent's tokens most often? That decides the
> next probes.

Before posting, replace N and M with `/v0/services` numbers of that day (the named services too:
only those already live there), and run the `uvx` line from
a clean machine: the answer must be the fact `https://apifacts.dev/pypi/json-trailing-slash-301`
(checked 2026-11-23 online and with `uvx --from apifacts==0.3.0 ... --offline`; `--offline` from a
git checkout answers nothing because the packaged snapshot is filled only at wheel build).

Rules the text follows: no superlatives, no "AI-powered", no pricing, no call to star the repo.
HN guidelines for Show HN: the thing must be usable now without signup, and it is.

## 3. Plan

- **Precondition:** maintainer's "yes" on the 2026-11-30 gate; at least 25 services on `main` and
  live on `/v0/services`; repository public (it is: `Illouminus/apifacts`).
- **Date:** Tuesday 2026-12-08 or Wednesday 2026-12-09, submitted between 15:00 and 17:00 UTC
  (US morning, EU afternoon). Fallback: Tuesday–Thursday of the following week. Not on a Monday or
  Friday; not on a day with a large US launch.
- **Who:** the maintainer submits and answers comments; the agent prepares numbers and answers on
  request. No vote solicitation, no second account.
- **Watch for 7 days:** the weekly digest numbers, plus `apifacts stats readers` daily.

**Success (proposed gate for the maintainer's decision):** at least **10 unique external
`POST /v0/check` clients in the salt week that contains the post** — for a post on 08.12 or 09.12,
the week Monday 2026-12-07 00:00 UTC → 2026-12-14, read by the weekly digest of 2026-12-14
(external = not `traffic.own`). The count is per salt week because "distinct networks" is exact only
inside one salt period (`apifacts/api/adoption.py`); a rolling 7 days from the post would cross two
salts. Hence the Tuesday/Wednesday post: it leaves 5–6 days of that week. Below 10, the project
moves to "registry for our own routines" with no further external distribution work.

Secondary signals (do not decide the gate): front page yes/no, points, comments asking for a
specific API, GitHub stars, PyPI downloads net of mirrors.
