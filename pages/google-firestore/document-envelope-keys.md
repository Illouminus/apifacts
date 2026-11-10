# A REST document has exactly four top-level keys: name (the full resource path), fields, createTime and updateTime.

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 267 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:document-schema-fingerprint`](../../probes/google-firestore/document-schema-fingerprint.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts/typed
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:document-schema-fingerprint` (declarative, [source](../../probes/google-firestore/document-schema-fingerprint.yaml))

Observations: none from reporters yet.

## Related errors

- [`Document "projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch" not found.`](document-not-found-404.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`
- [`Document "projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch" not found.`](unauthenticated-read-under-test-mode.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`
- [`The database agentfacts-nosuch-db does not exist for project agent-facts-probes Please visit https://console.cloud.google.com/datastore/setup?project=agent-facts-probes to add a Cloud Datastore or Cloud Firestore database.`](unknown-database-404.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`
- [`Permission denied on resource project agent-facts-nosuch-project-x.`](unknown-project-403.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 403 `PERMISSION_DENIED`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://firestore.googleapis.com/v1/projects/{project}/databases/{database}/documents/{collection}/{document}"},"error":{"status":200}}'
```

YAML: [facts/google-firestore/document-envelope-keys.yaml](../../facts/google-firestore/document-envelope-keys.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
