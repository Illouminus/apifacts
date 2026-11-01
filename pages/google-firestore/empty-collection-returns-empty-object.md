# Listing a collection that has no documents returns HTTP 200 with an empty object {}: no documents field (not documents: \[\]) and no nextPageToken.

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-01 · 206 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:empty-collection-empty-object`](../../probes/google-firestore/empty-collection-empty-object.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts_empty?pageSize=10
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:empty-collection-empty-object` (declarative, [source](../../probes/google-firestore/empty-collection-empty-object.yaml))

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

YAML: [facts/google-firestore/empty-collection-returns-empty-object.yaml](../../facts/google-firestore/empty-collection-returns-empty-object.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
