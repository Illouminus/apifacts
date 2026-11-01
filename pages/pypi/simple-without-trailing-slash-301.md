# GET /simple/{project} without the trailing slash returns HTTP 301 to /simple/{project}/ instead of the project page.

**PyPI (Python Package Index) · GET /simple/{project} · HTTP 301**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-01 · 620 confirmations from 2 vantages

## What to do

1. Call GET /simple/{project}/ instead.

## Example

What probe [`af:pypi:probe:simple-no-trailing-slash`](../../probes/pypi/simple-no-trailing-slash.yaml) sends (prod) and what it checks in the answer.

```http
GET https://pypi.org/simple/requests
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 301
Location: https://pypi.org/simple/requests/
```

## In your code

Fix 1:

```python
response = client.request("GET", f"/simple/{project}/")
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:simple-no-trailing-slash` (declarative, [source](../../probes/pypi/simple-no-trailing-slash.yaml))

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/simple/{project}"},"error":{"status":301}}'
```

YAML: [facts/pypi/simple-without-trailing-slash-301.yaml](../../facts/pypi/simple-without-trailing-slash-301.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
