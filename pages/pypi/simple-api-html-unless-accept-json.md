# GET /simple/{project}/ returns HTML unless Accept asks for application/vnd.pypi.simple.v1+json; the JSON form has name, versions and meta.\_last-serial, and Vary lists Accept.

**PyPI (Python Package Index) · GET /simple/{project}/**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 371 confirmations from 2 vantages

## What to do

1. Send header Accept = application/vnd.pypi.simple.v1+json.

## Example

What probe [`af:pypi:probe:simple-content-negotiation`](../../probes/pypi/simple-content-negotiation.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 200:

```http
GET https://pypi.org/simple/requests/
```

Step 2 → HTTP 200:

```http
GET https://pypi.org/simple/requests/
Accept: application/vnd.pypi.simple.v1+json
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Content-Type: application/vnd.pypi.simple.v1+json

{
  "name": "requests",
  "versions": "…2.31.0…",
  "meta": {
    "_last-serial": "…"
  }
}
```

## In your code

Fix 1:

```python
headers["Accept"] = "application/vnd.pypi.simple.v1+json"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:simple-content-negotiation` (declarative, [source](../../probes/pypi/simple-content-negotiation.yaml)) · official doc: <https://docs.pypi.org/api/index-api/>

Observations: none from reporters yet.

## Related errors

- [`404 Not Found`](simple-not-found-404.md) · GET /simple/{project}/ · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/simple/{project}/"}}'
```

YAML: [facts/pypi/simple-api-html-unless-accept-json.yaml](../../facts/pypi/simple-api-html-unless-accept-json.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
