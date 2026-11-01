# GET /simple/{project}/ with a non-normalized name such as Typing_Extensions returns HTTP 301 to the PEP 503 normalized URL /simple/typing-extensions/.

**PyPI (Python Package Index) · GET /simple/{project}/ · HTTP 301**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-01 · 208 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:pypi:probe:simple-unnormalized-name`](../../probes/pypi/simple-unnormalized-name.yaml) sends (prod) and what it checks in the answer.

```http
GET https://pypi.org/simple/Typing_Extensions/
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 301
Location: https://pypi.org/simple/typing-extensions/
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:simple-unnormalized-name` (declarative, [source](../../probes/pypi/simple-unnormalized-name.yaml)) · official doc: <https://docs.pypi.org/api/index-api/>

Observations: none from reporters yet.

## Related errors

- [`404 Not Found`](simple-not-found-404.md) · GET /simple/{project}/ · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/simple/{project}/"},"error":{"status":301}}'
```

YAML: [facts/pypi/simple-unnormalized-name-301.yaml](../../facts/pypi/simple-unnormalized-name-301.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
