# A SOQL query that matches nothing returns HTTP 200 with totalSize 0, done true and an empty records array, and no nextRecordsUrl.

**Salesforce Platform REST API · GET /services/data/{version}/query · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-03 · 157 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:soql-empty-result`](../../probes/salesforce/soql-empty-result.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/query?q=SELECT+Id+FROM+Account+WHERE+Name+%3D+%27agent-facts-no-such-account%27
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "totalSize": 0,
  "done": true
}
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:soql-empty-result` (declarative, [source](../../probes/salesforce/soql-empty-result.yaml))

Observations: none from reporters yet.

## Related errors

- [`The SOQL FIELDS function must have a LIMIT of at most 200`](soql-fields-all-needs-limit.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`unexpected token: 'SELEC'`](soql-malformed-query-400.md) · GET /services/data/{version}/query · HTTP 400 `MALFORMED_QUERY`
- [`SELECT NoSuchField__c FROM Account ^ ERROR at Row:1:Column:8 No such column 'NoSuchField__c' on entity 'Account'. If you are attempting to use a custom field, be sure to append the '__c' after the custom field name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-field-invalid-field.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_FIELD`
- [`SELECT Id FROM NoSuchObject__c ^ ERROR at Row:1:Column:16 sObject type 'NoSuchObject__c' is not supported. If you are attempting to use a custom object, be sure to append the '__c' after the entity name. Please reference your WSDL or the describe call for the appropriate names.`](soql-unknown-object-invalid-type.md) · GET /services/data/{version}/query · HTTP 400 `INVALID_TYPE`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data/{version}/query"},"error":{"status":200}}'
```

YAML: [facts/salesforce/empty-query-result-shape.yaml](../../facts/salesforce/empty-query-result-shape.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
