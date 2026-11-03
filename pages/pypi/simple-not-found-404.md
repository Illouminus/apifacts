# `404 Not Found`

**PyPI (Python Package Index) · GET /simple/{project}/ · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-03 · 244 confirmations from 2 vantages

> GET /simple/{project}/ for a project that does not exist returns HTTP 404 with the plain-text body 404 Not Found, not JSON.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:pypi:probe:simple-not-found`](../../probes/pypi/simple-not-found.yaml) sends (prod) and what it checks in the answer.

```http
GET https://pypi.org/simple/agent-facts-probe-no-such-project/
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404
Content-Type: <matches ^text/plain>

body contains "404 Not Found"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:simple-not-found` (declarative, [source](../../probes/pypi/simple-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](project-not-found-404.md) · GET /pypi/{project}/json · HTTP 404
- [`Not Found`](release-not-found-404.md) · GET /pypi/{project}/{version}/json · HTTP 404

## Machine access

Match signature (what `check()` matches): `### not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/simple/{project}/"},"error":{"status":404,"body_excerpt":"### not found"}}'
```

YAML: [facts/pypi/simple-not-found-404.yaml](../../facts/pypi/simple-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
