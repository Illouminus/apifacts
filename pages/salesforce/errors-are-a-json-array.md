# REST errors are a JSON array of objects with errorCode and message (e.g. \[{errorCode: NOT_FOUND, …}\]), not a single error object.

**Salesforce Platform REST API · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-03 · 463 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:record-not-found`](../../probes/salesforce/record-not-found.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/sobjects/Account/001000000000000AAA
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

[
  {
    "errorCode": "NOT_FOUND",
    "message": "The requested resource does not exist"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:record-not-found` (declarative, [source](../../probes/salesforce/record-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Provided external ID field does not exist or is not accessible: notanid`](non-id-path-read-as-external-id.md) · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404 `NOT_FOUND`
- [`The requested resource does not exist`](record-not-found-404.md) · GET /services/data/{version}/sobjects/{object}/{id} · HTTP 404 `NOT_FOUND`
- [`The requested resource does not exist`](unknown-sobject-describe-404.md) · GET /services/data/{version}/sobjects/{object}/describe · HTTP 404 `NOT_FOUND`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/sobjects/{object}/{id}"},"error":{"status":404}}'
```

YAML: [facts/salesforce/errors-are-a-json-array.yaml](../../facts/salesforce/errors-are-a-json-array.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
