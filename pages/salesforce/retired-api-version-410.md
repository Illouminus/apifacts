# `The requested resource no longer exists.`

**Salesforce Platform REST API · GET /services/data/{version}/limits · HTTP 410**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-05 · 312 confirmations from 2 vantages

> A retired REST API version (v30.0) returns HTTP 410 "The requested resource no longer exists.", while a version that does not exist yet (v99.0) returns 404.

## What to do

1. Call GET /services/data instead.

## Example

What probe [`af:salesforce:probe:api-version-retired-or-unknown`](../../probes/salesforce/api-version-retired-or-unknown.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v30.0/limits
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 410

[
  {
    "message": "The requested resource no longer exists."
  }
]
```

## In your code

Fix 1:

```python
response = client.request("GET", "/services/data")
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:api-version-retired-or-unknown` (declarative, [source](../../probes/salesforce/api-version-retired-or-unknown.yaml))

Observations: none from reporters yet.

## Related errors

- [`Session expired or invalid`](missing-session-401.md) · GET /services/data/{version}/limits · HTTP 401 `INVALID_SESSION_ID`
- [`Destination URL not reset. The URL returned from login must be set`](rest-on-login-host-url-not-reset.md) · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`

## Machine access

Match signature (what `check()` matches): `the requested resource no longer exists.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/limits"},"error":{"status":410,"body_excerpt":"the requested resource no longer exists."}}'
```

YAML: [facts/salesforce/retired-api-version-410.yaml](../../facts/salesforce/retired-api-version-410.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
