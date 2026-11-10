# `Only the first 1000 search results are available`

**GitHub REST API · GET /search/repositories · HTTP 422**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 335 confirmations from 2 vantages

> Search returns at most 1,000 results per query: a page past them (per_page 100, page 11) returns HTTP 422 Only the first 1000 search results are available.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:github:probe:search-beyond-1000`](../../probes/github/search-beyond-1000.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/search/repositories?q=stars:>1&per_page=100&page=11
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 422

{
  "message": "Only the first 1000 search results are available"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `PyGithub` (community) | `github.GithubException` | `e.status == 422` |
| Node `@octokit/request` | `RequestError` | `err.status === 422` |

Read from the SDK source: PyGithub 2.10.0: github/Requester.py Requester.createException; @octokit/request 10.0.16: dist-bundle/index.js fetchWrapper; @octokit/request-error 7.1.2.

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:search-beyond-1000` (declarative, [source](../../probes/github/search-beyond-1000.yaml)) · official doc: <https://docs.github.com/en/rest/search/search#about-search>

Observations: none from reporters yet.

## Related errors

- [`The search is longer than 256 characters.`](search-query-longer-than-256.md) · GET /search/repositories · HTTP 422 `invalid`

## Machine access

Match signature (what `check()` matches): `only the first #### search results are available`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/search/repositories"},"error":{"status":422,"body_excerpt":"only the first #### search results are available"}}'
```

YAML: [facts/github/search-first-1000-results.yaml](../../facts/github/search-first-1000-results.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
