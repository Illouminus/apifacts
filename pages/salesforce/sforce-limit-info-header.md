# Authenticated REST responses such as /limits and a SOQL query carry Sforce-Limit-Info: api-usage=\<used\>/\<daily limit\> (…/15000 on a Developer Edition org).

**Salesforce Platform REST API · GET /services/data/{version}/limits · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-06 · 205 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:daily-api-limit`](../../probes/salesforce/daily-api-limit.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/limits
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Sforce-Limit-Info: <matches ^api-usage=[0-9]+/15000$>

{
  "DailyApiRequests": {
    "Max": 15000,
    "Remaining": "…"
  }
}
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:daily-api-limit` (declarative, [source](../../probes/salesforce/daily-api-limit.yaml))

Observations: none from reporters yet.

## Related errors

- [`Session expired or invalid`](missing-session-401.md) · GET /services/data/{version}/limits · HTTP 401 `INVALID_SESSION_ID`
- [`Destination URL not reset. The URL returned from login must be set`](rest-on-login-host-url-not-reset.md) · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`
- [`The requested resource no longer exists.`](retired-api-version-410.md) · GET /services/data/{version}/limits · HTTP 410

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/limits"},"error":{"status":200}}'
```

YAML: [facts/salesforce/sforce-limit-info-header.yaml](../../facts/salesforce/sforce-limit-info-header.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
