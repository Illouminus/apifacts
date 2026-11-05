# The releases key of GET /pypi/{project}/json is deprecated and may be removed; projects should get release files from the Index API instead.

**PyPI (Python Package Index) · GET /pypi/{project}/json**

Status: 🔵 official · first seen 2026-10-20

## What to do

1. Call GET /simple/{project}/ instead.

## In your code

Fix 1:

```python
response = client.request("GET", f"/simple/{project}/")
```

## Dimensions

env: prod · plan: any · region: any · account_state: any · also seen: [anonymous](downloads-always-minus-one.md) (verified 2026-11-05)

## Evidence

official doc: <https://docs.pypi.org/api/json/#get-a-project>

Observations: none from reporters yet.

## Related errors

- [`Not Found`](project-not-found-404.md) · GET /pypi/{project}/json · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://pypi.org/pypi/{project}/json"}}'
```

YAML: [facts/pypi/releases-key-deprecated.yaml](../../facts/pypi/releases-key-deprecated.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
