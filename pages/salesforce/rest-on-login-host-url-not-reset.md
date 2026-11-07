# `Destination URL not reset. The URL returned from login must be set`

**Salesforce Platform REST API · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-07 · 365 confirmations from 2 vantages

> REST calls sent to login.salesforce.com instead of the org's instance return HTTP 400 URL_NOT_RESET "Destination URL not reset. The URL returned from login must be set", even /services/data.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:rest-on-login-host`](../../probes/salesforce/rest-on-login-host.yaml) sends (sandbox) and what it checks in the answer.

```http
GET https://login.salesforce.com/services/data/v62.0/limits
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

[
  {
    "errorCode": "URL_NOT_RESET",
    "message": "Destination URL not reset. The URL returned from login must be set"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:rest-on-login-host` (declarative, [source](../../probes/salesforce/rest-on-login-host.yaml))

Observations: none from reporters yet.

## Related errors

- [`The SOQL FIELDS function must have a LIMIT of at most 200`](soql-fields-all-needs-limit.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`unexpected token: 'SELEC'`](soql-malformed-query-400.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`SELECT NoSuchField__c FROM Account ^ ERROR at Row:1:Column:8 No such column 'NoSuchField__c' on entity 'Account'. If you are attempting to use a custom field, be sure to append the '__c' after the custom field name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-field-invalid-field.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_FIELD`
- [`SELECT Id FROM NoSuchObject__c ^ ERROR at Row:1:Column:16 sObject type 'NoSuchObject__c' is not supported. If you are attempting to use a custom object, be sure to append the '__c' after the entity name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-object-invalid-type.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_TYPE`
- [`Session expired or invalid`](missing-session-401.md) · GET /services/data/{version}/limits · HTTP 401 `INVALID_SESSION_ID`
- [`The requested resource no longer exists.`](retired-api-version-410.md) · GET /services/data/{version}/limits · HTTP 410

## Machine access

Match signature (what `check()` matches): `destination url not reset. the url returned from login must be set`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/limits"},"error":{"status":400,"body_excerpt":"destination url not reset. the url returned from login must be set"}}'
```

YAML: [facts/salesforce/rest-on-login-host-url-not-reset.yaml](../../facts/salesforce/rest-on-login-host-url-not-reset.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
