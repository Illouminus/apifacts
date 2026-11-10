# GET /pypi/{project}/{version}/json no longer has the releases key; the files of every release are only on /pypi/{project}/json and the Index API.

**PyPI (Python Package Index) · GET /pypi/{project}/{version}/json**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 830 confirmations from 2 vantages

## What to do

1. Call GET /simple/{project}/ instead.

## Example

What probe [`af:pypi:probe:json-release`](../../probes/pypi/json-release.yaml) sends (prod) and what it checks in the answer.

```http
GET https://pypi.org/pypi/requests/2.31.0/json
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "info": {
    "version": "2.31.0"
  },
  "urls": "…"
}
```

## In your code

Fix 1:

```python
response = client.request("GET", f"/simple/{project}/")
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:pypi:probe:json-release` (declarative, [source](../../probes/pypi/json-release.yaml)) · official doc: <https://docs.pypi.org/api/json/#get-a-release>

Observations: none from reporters yet.

## Related errors

- [`Not Found`](release-not-found-404.md) · GET /pypi/{project}/{version}/json · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/pypi/{project}/{version}/json"}}'
```

YAML: [facts/pypi/release-json-has-no-releases-key.yaml](../../facts/pypi/release-json-has-no-releases-key.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
