# `Session expired or invalid`

**Salesforce Platform REST API · GET /services/data/{version}/limits · HTTP 401 `INVALID_SESSION_ID`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-04 · 285 confirmations from 2 vantages

> A REST call with no access token returns HTTP 401 \[{errorCode: INVALID_SESSION_ID, message: "Session expired or invalid"}\].

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:versions-without-session`](../../probes/salesforce/versions-without-session.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/limits
Authorization: Bearer <access token>
```

Step 2 → HTTP 200:

```http
GET https://login.salesforce.com/services/data
```

Step 3 → HTTP 401:

```http
GET https://login.salesforce.com/services/data/v62.0/limits
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

[
  {
    "errorCode": "INVALID_SESSION_ID",
    "message": "Session expired or invalid"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:versions-without-session` (declarative, [source](../../probes/salesforce/versions-without-session.yaml))

Observations: none from reporters yet.

## Related errors

- [`Destination URL not reset. The URL returned from login must be set`](rest-on-login-host-url-not-reset.md) · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`
- [`The requested resource no longer exists.`](retired-api-version-410.md) · GET /services/data/{version}/limits · HTTP 410

## Machine access

Match signature (what `check()` matches): `session expired or invalid`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/limits"},"error":{"status":401,"body_excerpt":"session expired or invalid"}}'
```

YAML: [facts/salesforce/missing-session-401.yaml](../../facts/salesforce/missing-session-401.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
