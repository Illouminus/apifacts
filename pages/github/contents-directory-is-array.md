# GET /repos/{owner}/{repo}/contents on a directory returns a JSON array of entries, while a file path returns one object with type file and base64-encoded content (encoding: base64).

**GitHub REST API · GET /repos/{owner}/{repo}/contents · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-01 · 7 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:github:probe:contents-directory-vs-file`](../../probes/github/contents-directory-vs-file.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/repos/octocat/Hello-World/contents
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

[
  {
    "path": "README",
    "type": "file"
  }
]
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:contents-directory-vs-file` (declarative, [source](../../probes/github/contents-directory-vs-file.yaml))

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/repos/{owner}/{repo}/contents"},"error":{"status":200}}'
```

YAML: [facts/github/contents-directory-is-array.yaml](../../facts/github/contents-directory-is-array.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
