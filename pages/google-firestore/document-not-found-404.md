# `Document "projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch" not found.`

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-07 · 221 confirmations from 2 vantages

> Getting a document that does not exist returns HTTP 404 NOT_FOUND with the full document name in the message (Document "projects/…/documents/\<path\>" not found.).

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:document-not-found`](../../probes/google-firestore/document-not-found.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": {
    "status": "NOT_FOUND",
    "message": "Document \"projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch\" not found."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-cloud-firestore` | `google.api_core.exceptions.NotFound` | `e.code == 404` |
| Node `@google-cloud/firestore` | `Error` | `err.code === 5` |

Read from the SDK source: google-cloud-firestore 2.34.1, google-api-core 2.43.2: exceptions.exception_class_for_grpc_status; google-gax 6.14.0 (dependency of @google-cloud/firestore 9.4.0): build/src/status.js Status.

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:document-not-found` (declarative, [source](../../probes/google-firestore/document-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Document "projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch" not found.`](unauthenticated-read-under-test-mode.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`
- [`The database agentfacts-nosuch-db does not exist for project agent-facts-probes Please visit https://console.cloud.google.com/datastore/setup?project=agent-facts-probes to add a Cloud Datastore or Cloud Firestore database.`](unknown-database-404.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 404 `NOT_FOUND`
- [`Permission denied on resource project agent-facts-nosuch-project-x.`](unknown-project-403.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 403 `PERMISSION_DENIED`

## Machine access

Match signature (what `check()` matches): `document "projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch" not found.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://firestore.googleapis.com/v1/projects/{project}/databases/{database}/documents/{collection}/{document}"},"error":{"status":404,"body_excerpt":"document \"projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch\" not found."}}'
```

YAML: [facts/google-firestore/document-not-found-404.yaml](../../facts/google-firestore/document-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
