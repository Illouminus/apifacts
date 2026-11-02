# Listing a subcollection under a parent document that does not exist returns HTTP 200 {} rather than 404: the parent's absence is not reported.

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document}/{subcollection} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-02 · 801 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:subcollection-of-missing-document`](../../probes/google-firestore/subcollection-of-missing-document.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts/nosuch/children
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:subcollection-of-missing-document` (declarative, [source](../../probes/google-firestore/subcollection-of-missing-document.yaml))

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://firestore.googleapis.com/v1/projects/{project}/databases/{database}/documents/{collection}/{document}/{subcollection}"},"error":{"status":200}}'
```

YAML: [facts/google-firestore/subcollection-of-missing-document-is-empty.yaml](../../facts/google-firestore/subcollection-of-missing-document-is-empty.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
