# A timestamp field comes back as timestampValue, an RFC 3339 string in UTC with a Z suffix ("2026-10-24T00:00:00Z").

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection}/{document} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-07 · 218 confirmations from 2 vantages

## What to do

1. Encode timestampValue as an RFC 3339 timestamp.

## Example

What probe [`af:google-firestore:probe:typed-document`](../../probes/google-firestore/typed-document.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts/typed
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "fields": {
    "int": {
      "integerValue": "42"
    },
    "dbl": {
      "doubleValue": 3.5
    },
    "ts": {
      "timestampValue": "2026-10-24T00:00:00Z"
    },
    "flag": {
      "booleanValue": true
    },
    "tags": {
      "arrayValue": {
        "values": [
          {
            "stringValue": "a"
          }
        ]
      }
    },
    "nested": {
      "mapValue": {
        "fields": {
          "k": {
            "stringValue": "v"
          }
        }
      }
    }
  },
  "name": "projects/agent-facts-probes/databases/(default)/documents/agent_facts/typed"
}
```

## In your code

Fix 1:

```python
from datetime import UTC, datetime
params["timestampValue"] = moment.astimezone(UTC).isoformat()
```

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:typed-document` (declarative, [source](../../probes/google-firestore/typed-document.yaml))

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

YAML: [facts/google-firestore/timestamp-value-rfc3339-utc.yaml](../../facts/google-firestore/timestamp-value-rfc3339-utc.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
