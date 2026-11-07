# `The SOQL FIELDS function must have a LIMIT of at most 200`

**Salesforce Platform REST API · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-07 · 220 confirmations from 2 vantages

> SELECT FIELDS(ALL) without a LIMIT returns HTTP 400 MALFORMED_QUERY "The SOQL FIELDS function must have a LIMIT of at most 200".

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:soql-fields-all-needs-limit`](../../probes/salesforce/soql-fields-all-needs-limit.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/query?q=SELECT+FIELDS%28ALL%29+FROM+Account
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

[
  {
    "errorCode": "MALFORMED_QUERY",
    "message": "The SOQL FIELDS function must have a LIMIT of at most 200"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:soql-fields-all-needs-limit` (declarative, [source](../../probes/salesforce/soql-fields-all-needs-limit.yaml))

Observations: none from reporters yet.

## Related errors

- [`unexpected token: 'SELEC'`](soql-malformed-query-400.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`SELECT NoSuchField__c FROM Account ^ ERROR at Row:1:Column:8 No such column 'NoSuchField__c' on entity 'Account'. If you are attempting to use a custom field, be sure to append the '__c' after the custom field name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-field-invalid-field.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_FIELD`
- [`SELECT Id FROM NoSuchObject__c ^ ERROR at Row:1:Column:16 sObject type 'NoSuchObject__c' is not supported. If you are attempting to use a custom object, be sure to append the '__c' after the entity name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-object-invalid-type.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_TYPE`
- [`Destination URL not reset. The URL returned from login must be set`](rest-on-login-host-url-not-reset.md) · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`

## Machine access

Match signature (what `check()` matches): `the soql fields function must have a limit of at most ###`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/query"},"error":{"status":400,"body_excerpt":"the soql fields function must have a limit of at most ###"}}'
```

YAML: [facts/salesforce/soql-fields-all-needs-limit.yaml](../../facts/salesforce/soql-fields-all-needs-limit.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
