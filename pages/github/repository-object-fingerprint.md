# On 2026-10-20 the repository object of GET /repos/{owner}/{repo} at API version 2022-11-28 had 84 top-level keys, schema fingerprint 4ca5975282230619.

**GitHub REST API · GET /repos/{owner}/{repo}**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-02 · 69 confirmations from 2 vantages

## What to do

1. Send header X-GitHub-Api-Version = 2022-11-28.

## Example

What probe [`af:github:probe:repo-schema-fingerprint`](../../probes/github/repo-schema-fingerprint.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/Hello-World?cb=<run_uuid>
X-GitHub-Api-Version: 2022-11-28
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
X-GitHub-Api-Version-Selected: 2022-11-28
```

## In your code

Fix 1:

```python
headers["X-GitHub-Api-Version"] = "2022-11-28"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-schema-fingerprint` (declarative, [source](../../probes/github/repo-schema-fingerprint.yaml))

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

YAML: [facts/github/repository-object-fingerprint.yaml](../../facts/github/repository-object-fingerprint.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
