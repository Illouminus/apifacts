# `Not Found`

**npm registry · GET /{package}/{version} · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-10 · 167 confirmations from 2 vantages

> GET /{package}/{version} for a package that does not exist returns HTTP 404 with the bare JSON string "Not Found"; an unencoded scoped name (/@scope/name) lands on the same path shape and returns {"error": "Not found"}.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:npm-registry:probe:missing-package-two-segments`](../../probes/npm-registry/missing-package-two-segments.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 404:

```http
GET https://registry.npmjs.org/agent-facts-probe-no-such-package/latest
```

Step 2 → HTTP 404:

```http
GET https://registry.npmjs.org/@agent-facts-probe/no-such-package
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": "Not found"
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:npm-registry:probe:missing-package-two-segments` (declarative, [source](../../probes/npm-registry/missing-package-two-segments.yaml))

Observations: none from reporters yet.

## Related errors

- [`version not found: 0.0.99`](version-not-found-404.md) · GET /{package}/{version} · HTTP 404
- [`Not Found`](dist-tags-not-found-404.md) · GET /-/package/{package}/dist-tags · HTTP 404
- [`Not found`](package-not-found-404.md) · GET /{package} · HTTP 404

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://registry.npmjs.org/{package}/{version}"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/npm-registry/missing-package-version-path-404.yaml](../../facts/npm-registry/missing-package-version-path-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
