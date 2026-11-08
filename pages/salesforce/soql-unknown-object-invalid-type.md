# `SELECT Id FROM NoSuchObject__c ^ ERROR at Row:1:Column:16 sObject type 'NoSuchObject__c' is not supported. If you are attempting to use a custom object, be sure to append the '__c' after the entity name. Please reference your WSDL or the describe call for the appropriate names.`

**Salesforce Platform REST API · GET /services/data/{version}/query · HTTP 400 `INVALID_TYPE`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-08 · 236 confirmations from 2 vantages

> A SOQL query on an object the org does not have returns HTTP 400 INVALID_TYPE ("sObject type '\<object\>' is not supported").

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:soql-unknown-object`](../../probes/salesforce/soql-unknown-object.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/query?q=SELECT+Id+FROM+NoSuchObject__c
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

[
  {
    "errorCode": "INVALID_TYPE",
    "message": "SELECT Id FROM NoSuchObject__c ^ ERROR at Row:1:Column:16 sObject type 'NoSuchObject__c' is not supported. If you are attempting to use a custom object, be sure to append the '__c' after the entity name. Please reference your WSDL or the describe call for the appropriate names."
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:soql-unknown-object` (declarative, [source](../../probes/salesforce/soql-unknown-object.yaml))

Observations: none from reporters yet.

## Related errors

- [`The SOQL FIELDS function must have a LIMIT of at most 200`](soql-fields-all-needs-limit.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`unexpected token: 'SELEC'`](soql-malformed-query-400.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`SELECT NoSuchField__c FROM Account ^ ERROR at Row:1:Column:8 No such column 'NoSuchField__c' on entity 'Account'. If you are attempting to use a custom field, be sure to append the '__c' after the custom field name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-field-invalid-field.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_FIELD`
- [`Destination URL not reset. The URL returned from login must be set`](rest-on-login-host-url-not-reset.md) · GET /services/data/{version}/limits · HTTP 400 `URL_NOT_RESET`

## Machine access

Match signature (what `check()` matches): `select id from nosuchobject__c ^ error at row:#:column:## sobject type 'nosuchobject__c' is not supported. if you are attempting to use a custom object, be sure to append the '__c' after the entity name. please reference your wsdl or the describe call for the appropriate names.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/query"},"error":{"status":400,"body_excerpt":"select id from nosuchobject__c ^ error at row:#:column:## sobject type '\''nosuchobject__c'\'' is not supported. if you are attempting to use a custom object, be sure to append the '\''__c'\'' after the entity name. please reference your wsdl or the describe call for the appropriate names."}}'
```

YAML: [facts/salesforce/soql-unknown-object-invalid-type.yaml](../../facts/salesforce/soql-unknown-object-invalid-type.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
