# Anonymous REST requests count against the core resource with x-ratelimit-limit 60 per hour, shared by every client behind the same originating IP address.

**GitHub REST API · GET /repos/{owner}/{repo}**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-06 · 91 confirmations from 2 vantages

## What to do

1. Request OAuth scope public_repo.

## Example

What probe [`af:github:probe:repo-anonymous`](../../probes/github/repo-anonymous.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/Hello-World
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
X-RateLimit-Limit: 60
X-RateLimit-Resource: core
X-RateLimit-Remaining: …
X-RateLimit-Used: …
X-RateLimit-Reset: <matches ^[0-9]{10}$>

{
  "full_name": "octocat/Hello-World"
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-anonymous` (declarative, [source](../../probes/github/repo-anonymous.yaml)) · official doc: <https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api#primary-rate-limit-for-unauthenticated-users>

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
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}"}}'
```

YAML: [facts/github/anonymous-core-rate-limit.yaml](../../facts/github/anonymous-core-rate-limit.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
