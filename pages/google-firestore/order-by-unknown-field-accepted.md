# orderBy on a field that no document has is accepted with HTTP 200 instead of being refused.

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 339 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:order-by-unknown-field`](../../probes/google-firestore/order-by-unknown-field.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts?orderBy=agent_facts_no_such_field+desc
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:order-by-unknown-field` (declarative, [source](../../probes/google-firestore/order-by-unknown-field.yaml))

Observations: none from reporters yet.

## Related errors

- [``Invalid property path "a b". Unquoted property paths must match regex ([a-zA-Z_][a-zA-Z_0-9]*), and quoted property paths must match regex (`(?:[^`\\]|(?:\\.))+`)``](invalid-field-path-400.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`
- [`invalid page token`](invalid-page-token-400.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`
- [`Page size must be nonnegative.`](negative-page-size-400.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://firestore.googleapis.com/v1/projects/{project}/databases/{database}/documents/{collection}"},"error":{"status":200}}'
```

YAML: [facts/google-firestore/order-by-unknown-field-accepted.yaml](../../facts/google-firestore/order-by-unknown-field-accepted.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
