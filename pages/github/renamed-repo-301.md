# `Moved Permanently`

**GitHub REST API · GET /repos/{owner}/{repo} · HTTP 301**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 105 confirmations from 2 vantages

> GET /repos/{owner}/{repo} on a renamed or transferred repository returns HTTP 301 Moved Permanently with Location /repositories/{id} instead of the repository object.

## What to do

1. Call GET /repositories/{id} instead.

## Example

What probe [`af:github:probe:repo-renamed`](../../probes/github/repo-renamed.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/twitter/bootstrap
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 301
Location: https://api.github.com/repositories/2126244

{
  "message": "Moved Permanently"
}
```

## In your code

Fix 1:

```python
response = client.request("GET", f"/repositories/{id}")
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-renamed` (declarative, [source](../../probes/github/repo-renamed.yaml)) · official doc: <https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api#follow-redirects>

Observations: none from reporters yet.

## Related errors

- [REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.](error-status-is-a-string.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](missing-repo-404.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](private-repo-404-not-403.md) · GET /repos/{owner}/{repo} · HTTP 404
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit.md) · GET /repos/{owner}/{repo} · HTTP 403
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit-429.md) · GET /repos/{owner}/{repo} · HTTP 429
- [`The version you specified in the "X-GitHub-API-Version" request header, "2021-01-01", is not a supported version. The following versions are currently supported: "2026-03-10" (most recent) and "2022-11-28".`](unsupported-api-version-400.md) · GET /repos/{owner}/{repo} · HTTP 400

## Machine access

Match signature (what `check()` matches): `moved permanently`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}"},"error":{"status":301,"body_excerpt":"moved permanently"}}'
```

YAML: [facts/github/renamed-repo-301.yaml](../../facts/github/renamed-repo-301.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
