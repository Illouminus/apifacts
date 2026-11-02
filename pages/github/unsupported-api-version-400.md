# `The version you specified in the "X-GitHub-API-Version" request header, "2021-01-01", is not a supported version. The following versions are currently supported: "2026-03-10" (most recent) and "2022-11-28".`

**GitHub REST API · GET /repos/{owner}/{repo} · HTTP 400**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-02 · 66 confirmations from 2 vantages

> An X-GitHub-Api-Version that is not a supported version, such as 2021-01-01, returns HTTP 400 Bad Request whose errors field is a string naming the supported versions.

## What to do

1. Send header X-GitHub-Api-Version = 2026-03-10.

## Example

What probe [`af:github:probe:repo-api-version-unsupported`](../../probes/github/repo-api-version-unsupported.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/Hello-World?cb=<run_uuid>
X-GitHub-Api-Version: 2021-01-01
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "message": "Bad Request",
  "errors": "The version you specified in the \"X-GitHub-API-Version\" request header, \"2021-01-01\", is not a supported version. The following versions are currently supported: \"2026-03-10\" (most recent) and \"2022-11-28\".",
  "status": "400"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `PyGithub` (community) | `github.GithubException` | `e.status == 400` |
| Node `@octokit/request` | `RequestError` | `err.status === 400` |

Read from the SDK source: PyGithub 2.10.0: github/Requester.py Requester.createException; @octokit/request 10.0.16: dist-bundle/index.js fetchWrapper; @octokit/request-error 7.1.2.

Fix 1:

```python
headers["X-GitHub-Api-Version"] = "2026-03-10"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-api-version-unsupported` (declarative, [source](../../probes/github/repo-api-version-unsupported.yaml)) · official doc: <https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api#not-a-supported-version>

Observations: none from reporters yet.

## Related errors

- [REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.](error-status-is-a-string.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](missing-repo-404.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](private-repo-404-not-403.md) · GET /repos/{owner}/{repo} · HTTP 404
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit.md) · GET /repos/{owner}/{repo} · HTTP 403
- [Exceeding a secondary rate limit returns HTTP 403 or 429 with a message saying so; retry-after, when present, gives the seconds to wait, otherwise the wait is at least one minute.](secondary-rate-limit-429.md) · GET /repos/{owner}/{repo} · HTTP 429
- [REST API requests without a User-Agent header are rejected, and a request with an invalid User-Agent header receives HTTP 403 Forbidden.](user-agent-required.md) · GET /repos/{owner}/{repo} · HTTP 403

## Machine access

Match signature (what `check()` matches): `the version you specified in the "x-github-api-version" request header, "####-##-##", is not a supported version. the following versions are currently supported: "####-##-##" (most recent) and "####-##-##".`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}"},"error":{"status":400,"body_excerpt":"the version you specified in the \"x-github-api-version\" request header, \"####-##-##\", is not a supported version. the following versions are currently supported: \"####-##-##\" (most recent) and \"####-##-##\"."}}'
```

YAML: [facts/github/unsupported-api-version-400.yaml](../../facts/github/unsupported-api-version-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
