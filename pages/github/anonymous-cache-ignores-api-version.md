# Anonymous GET /repos/{owner}/{repo} responses are shared-cacheable for 60 s (public, s-maxage=60) and Vary does not list X-GitHub-Api-Version, so by HTTP caching rules a cache may serve a body of another API version.

**GitHub REST API · GET /repos/{owner}/{repo} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-08 · 95 confirmations from 2 vantages

## What to do

1. Set query parameter cb to new UUID per request.
2. Request OAuth scope public_repo.

## Example

What probe [`af:github:probe:repo-cache-headers`](../../probes/github/repo-cache-headers.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/Hello-World
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Cache-Control: <matches (^|[ ,])public([ ,]|$)>
Cache-Control: <matches s-maxage=60([ ,]|$)>
Vary: <matches ^(?![\s\S]*(?i:x-github-api-version))>
X-GitHub-Api-Version-Selected: …
```

## In your code

Fix 1:

```python
import uuid
params["cb"] = str(uuid.uuid4())  # a new value on every request
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-cache-headers` (declarative, [source](../../probes/github/repo-cache-headers.yaml))

Observations: none from reporters yet.

## Related errors

- [REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.](error-status-is-a-string.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](missing-repo-404.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](private-repo-404-not-403.md) · GET /repos/{owner}/{repo} · HTTP 404
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit.md) · GET /repos/{owner}/{repo} · HTTP 403
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit-429.md) · GET /repos/{owner}/{repo} · HTTP 429
- [`The version you specified in the "X-GitHub-API-Version" request header, "2021-01-01", is not a supported version. The following versions are currently supported: "2026-03-10" (most recent) and "2022-11-28".`](unsupported-api-version-400.md) · GET /repos/{owner}/{repo} · HTTP 400

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}"},"error":{"status":200}}'
```

YAML: [facts/github/anonymous-cache-ignores-api-version.yaml](../../facts/github/anonymous-cache-ignores-api-version.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
