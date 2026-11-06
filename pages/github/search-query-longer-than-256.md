# `The search is longer than 256 characters.`

**GitHub REST API · GET /search/repositories · HTTP 422 `invalid`**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-06 · 274 confirmations from 2 vantages

> A search q parameter longer than 256 characters returns HTTP 422 Validation Failed with errors\[0\] code invalid, field q and message The search is longer than 256 characters.

## What to do

1. Keep q ≤ 256 bytes.

## Example

What probe [`af:github:probe:search-query-too-long`](../../probes/github/search-query-too-long.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/search/repositories?q=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 422
X-RateLimit-Resource: search
X-RateLimit-Limit: 10

{
  "message": "Validation Failed",
  "errors": [
    {
      "message": "The search is longer than 256 characters.",
      "field": "q",
      "code": "invalid"
    }
  ],
  "status": "422"
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

Probe `af:github:probe:search-query-too-long` (declarative, [source](../../probes/github/search-query-too-long.yaml))

Observations: none from reporters yet.

## Related errors

- [`Only the first 1000 search results are available`](search-first-1000-results.md) · GET /search/repositories · HTTP 422

## Machine access

Match signature (what `check()` matches): `the search is longer than ### characters.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/search/repositories"},"error":{"status":422,"body_excerpt":"the search is longer than ### characters."}}'
```

YAML: [facts/github/search-query-longer-than-256.yaml](../../facts/github/search-query-longer-than-256.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
