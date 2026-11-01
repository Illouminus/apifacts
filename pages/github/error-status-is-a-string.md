# REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.

**GitHub REST API · GET /repos/{owner}/{repo} · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-10-31 · 60 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:github:probe:repo-not-found`](../../probes/github/repo-not-found.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/agent-facts-probe-no-such-repo
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "message": "Not Found",
  "status": "404"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `PyGithub` (community) | `github.GithubException` | `e.status == 404` |
| Node `@octokit/request` | `RequestError` | `err.status === 404` |

Read from the SDK source: PyGithub 2.10.0: github/Requester.py Requester.createException; @octokit/request 10.0.16: dist-bundle/index.js fetchWrapper; @octokit/request-error 7.1.2.

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:repo-not-found` (declarative, [source](../../probes/github/repo-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](missing-repo-404.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](private-repo-404-not-403.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](contents-missing-path-404.md) · GET /repos/{owner}/{repo}/contents/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-2.md) · GET /repos/{owner}/{repo}/contents/{dir}/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-3.md) · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-4.md) · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{subdir2}/{path} · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}"},"error":{"status":404}}'
```

YAML: [facts/github/error-status-is-a-string.yaml](../../facts/github/error-status-is-a-string.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
