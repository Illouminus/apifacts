# `Not Found`

**PyPI (Python Package Index) · GET /pypi/{project}/{version}/json · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-02 · 169 confirmations from 2 vantages

> GET /pypi/{project}/{version}/json for an unknown version of an existing project returns the same HTTP 404 {"message": "Not Found"} as a missing project.

## What to do

1. Call GET /pypi/{project}/json instead.

## Example

What probe [`af:pypi:probe:json-not-found`](../../probes/pypi/json-not-found.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 404:

```http
GET https://pypi.org/pypi/agent-facts-probe-no-such-project/json
```

Step 2 → HTTP 404:

```http
GET https://pypi.org/pypi/requests/0.0.0.999/json
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "message": "Not Found"
}
```

## In your code

Fix 1:

```python
response = client.request("GET", f"/pypi/{project}/json")
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:json-not-found` (declarative, [source](../../probes/pypi/json-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](project-not-found-404.md) · GET /pypi/{project}/json · HTTP 404
- [`404 Not Found`](simple-not-found-404.md) · GET /simple/{project}/ · HTTP 404

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/pypi/{project}/{version}/json"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/pypi/release-not-found-404.yaml](../../facts/pypi/release-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
