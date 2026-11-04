# `version not found: 0.0.99`

**npm registry · GET /{package}/{version} · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-04 · 63 confirmations from 2 vantages

> GET /{package}/{version} for an existing package with an unknown version or dist-tag returns HTTP 404 whose body is a bare JSON string "version not found: \<version\>", not an object.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:npm-registry:probe:version-not-found`](../../probes/npm-registry/version-not-found.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 404:

```http
GET https://registry.npmjs.org/left-pad/0.0.99
```

Step 2 → HTTP 404:

```http
GET https://registry.npmjs.org/left-pad/agent-facts-no-such-tag
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

$ = "version not found: agent-facts-no-such-tag"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:npm-registry:probe:version-not-found` (declarative, [source](../../probes/npm-registry/version-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](missing-package-version-path-404.md) · GET /{package}/{version} · HTTP 404
- [`Not Found`](dist-tags-not-found-404.md) · GET /-/package/{package}/dist-tags · HTTP 404
- [`Not found`](package-not-found-404.md) · GET /{package} · HTTP 404

## Machine access

Match signature (what `check()` matches): `version not found: #.#.##`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://registry.npmjs.org/{package}/{version}"},"error":{"status":404,"body_excerpt":"version not found: #.#.##"}}'
```

YAML: [facts/npm-registry/version-not-found-404.yaml](../../facts/npm-registry/version-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
