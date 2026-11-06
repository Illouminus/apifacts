# `Not Found`

**GitHub REST API · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{subdir2}/{path} · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-06 · 66 confirmations from 2 vantages

> An anonymous GET of a four-segment contents path that does not exist returns HTTP 404 Not Found; a missing parent directory gets the same 404, not a separate error.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:github:probe:contents-not-found`](../../probes/github/contents-not-found.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 404:

```http
GET https://api.github.com/repos/octocat/Hello-World/contents/agent-facts-no-such-file
```

Step 2 → HTTP 404:

```http
GET https://api.github.com/repos/octocat/Hello-World/contents/agent-facts-dir/no-such-file
```

Step 3 → HTTP 404:

```http
GET https://api.github.com/repos/octocat/Hello-World/contents/agent-facts-dir/a/no-such-file
```

Step 4 → HTTP 404:

```http
GET https://api.github.com/repos/octocat/Hello-World/contents/agent-facts-dir/a/b/no-such-file
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "message": "Not Found"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `PyGithub` (community) | `github.UnknownObjectException` | `e.status == 404` |
| Node `@octokit/request` | `RequestError` | `err.status === 404` |

Read from the SDK source: PyGithub 2.10.0: github/Requester.py Requester.createException; @octokit/request 10.0.16: dist-bundle/index.js fetchWrapper; @octokit/request-error 7.1.2.

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:contents-not-found` (declarative, [source](../../probes/github/contents-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](contents-missing-path-404.md) · GET /repos/{owner}/{repo}/contents/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-2.md) · GET /repos/{owner}/{repo}/contents/{dir}/{path} · HTTP 404
- [`Not Found`](contents-missing-path-404-depth-3.md) · GET /repos/{owner}/{repo}/contents/{dir}/{subdir}/{path} · HTTP 404
- [`No commit found for the ref agent-facts-no-such-ref`](contents-unknown-ref-404.md) · GET /repos/{owner}/{repo}/contents/{path} · HTTP 404
- [REST error bodies carry a status field holding the HTTP code as a JSON string, such as "404", not as a number.](error-status-is-a-string.md) · GET /repos/{owner}/{repo} · HTTP 404
- [`Not Found`](missing-repo-404.md) · GET /repos/{owner}/{repo} · HTTP 404

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}/contents/{dir}/{subdir}/{subdir2}/{path}"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/github/contents-missing-path-404-depth-4.yaml](../../facts/github/contents-missing-path-404-depth-4.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
