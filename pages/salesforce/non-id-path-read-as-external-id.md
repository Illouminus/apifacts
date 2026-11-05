# `Provided external ID field does not exist or is not accessible: notanid`

**Salesforce Platform REST API · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-05 · 558 confirmations from 2 vantages

> A record path whose last segment is not an id (…/sobjects/Account/notanid) is read as an external ID field name: HTTP 404 "Provided external ID field does not exist or is not accessible: notanid".

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:non-id-read-as-external-id`](../../probes/salesforce/non-id-read-as-external-id.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/sobjects/Account/notanid
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

[
  {
    "errorCode": "NOT_FOUND",
    "message": "Provided external ID field does not exist or is not accessible: notanid"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:non-id-read-as-external-id` (declarative, [source](../../probes/salesforce/non-id-read-as-external-id.yaml))

Observations: none from reporters yet.

## Related errors

- [REST errors are a JSON array of objects with errorCode and message (e.g. \[{errorCode: NOT_FOUND, …}\]), not a single error object.](errors-are-a-json-array.md) · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404
- [`The requested resource does not exist`](record-not-found-404.md) · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404 `NOT_FOUND`
- [`The requested resource does not exist`](unknown-sobject-describe-404.md) · GET /services/data/{version}/sobjects/{object}/describe · HTTP 404 `NOT_FOUND`

## Machine access

Match signature (what `check()` matches): `provided external id field does not exist or is not accessible: notanid`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/sobjects/{object}/{id}"},"error":{"status":404,"body_excerpt":"provided external id field does not exist or is not accessible: notanid"}}'
```

YAML: [facts/salesforce/non-id-path-read-as-external-id.yaml](../../facts/salesforce/non-id-path-read-as-external-id.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
