# GET /pypi/{project}/json with a non-normalized name such as Typing_Extensions returns HTTP 200 directly, without a redirect, and info.name is typing-extensions.

**PyPI (Python Package Index) · GET /pypi/{project}/json**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-06 · 228 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:pypi:probe:json-unnormalized-name`](../../probes/pypi/json-unnormalized-name.yaml) sends (prod) and what it checks in the answer.

```http
GET https://pypi.org/pypi/Typing_Extensions/json
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "info": {
    "name": "typing-extensions"
  }
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:json-unnormalized-name` (declarative, [source](../../probes/pypi/json-unnormalized-name.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](project-not-found-404.md) · GET /pypi/{project}/json · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/pypi/{project}/json"}}'
```

YAML: [facts/pypi/json-api-accepts-unnormalized-name.yaml](../../facts/pypi/json-api-accepts-unnormalized-name.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
