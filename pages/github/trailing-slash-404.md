# `404 Not Found`

**GitHub REST API · GET /rate_limit/ · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 707 confirmations from 2 vantages

> A REST path with a trailing slash, such as /rate_limit/, returns HTTP 404 with the plain-text body 404 Not Found instead of the endpoint's JSON.

## What to do

1. Call GET /rate_limit instead.

## Example

What probe [`af:github:probe:trailing-slash`](../../probes/github/trailing-slash.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/rate_limit/
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404
Content-Type: <matches ^text/plain>

body contains "404 Not Found"
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `PyGithub` (community) | `github.UnknownObjectException` | `e.status == 404` |
| Node `@octokit/request` | `RequestError` | `err.status === 404` |

Read from the SDK source: PyGithub 2.10.0: github/Requester.py Requester.createException; @octokit/request 10.0.16: dist-bundle/index.js fetchWrapper; @octokit/request-error 7.1.2.

Fix 1:

```python
response = client.request("GET", "/rate_limit")
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:trailing-slash` (declarative, [source](../../probes/github/trailing-slash.yaml)) · official doc: <https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api#404-not-found-for-an-existing-resource>

Observations: none from reporters yet.

## Related errors

- [`Not Found`](contents-missing-path-404.md) · GET /repos/{owner}/{repo}/contents/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-2.md) · GET /repos/{owner}/{repo}/contents/{dir}/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-3.md) · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-4.md) · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{subdir2}/{path} · HTTP 404
- [`No commit found for the ref agent-facts-no-such-ref`](contents-unknown-ref-404.md) · GET /repos/{owner}/{repo}/contents/{path} · HTTP 404
- [REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.](error-status-is-a-string.md) · GET /repos/{owner}/{repo} · HTTP 404

## Machine access

Match signature (what `check()` matches): `### not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/rate_limit/"},"error":{"status":404,"body_excerpt":"### not found"}}'
```

YAML: [facts/github/trailing-slash-404.yaml](../../facts/github/trailing-slash-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
