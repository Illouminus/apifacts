# ``Invalid property path "a b". Unquoted property paths must match regex ([a-zA-Z_][a-zA-Z_0-9]*), and quoted property paths must match regex (`(?:[^`\\]|(?:\\.))+`)``

**Cloud Firestore (Firebase) REST API · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 339 confirmations from 2 vantages

> A mask.fieldPaths entry with a space or other character outside \[a-zA-Z\_\]\[a-zA-Z_0-9\]\* returns HTTP 400 "Invalid property path" unless the path is quoted in backticks.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-firestore:probe:list-parameter-errors`](../../probes/google-firestore/list-parameter-errors.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 400:

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts?pageToken=apifacts
Authorization: Bearer <access token>
```

Step 2 → HTTP 400:

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts?pageSize=-1
Authorization: Bearer <access token>
```

Step 3 → HTTP 400:

```http
GET https://firestore.googleapis.com/v1/projects/agent-facts-probes/databases/(default)/documents/agent_facts?mask.fieldPaths=a+b
Authorization: Bearer <access token>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "message": "Invalid property path \"a b\". Unquoted property paths must match regex ([a-zA-Z_][a-zA-Z_0-9]*), and quoted property paths must match regex (`(?:[^`\\\\]|(?:\\\\.))+`)",
    "status": "INVALID_ARGUMENT"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-cloud-firestore` | `google.api_core.exceptions.InvalidArgument` | `e.code == 400` |
| Node `@google-cloud/firestore` | `Error` | `err.code === 3` |

Read from the SDK source: google-cloud-firestore 2.34.1, google-api-core 2.43.2: exceptions.exception_class_for_grpc_status; google-gax 6.14.0 (dependency of @google-cloud/firestore 9.4.0): build/src/status.js Status.

## Dimensions

env: prod · plan: any · region: any · account_state: service_account

## Evidence

Probe `af:google-firestore:probe:list-parameter-errors` (declarative, [source](../../probes/google-firestore/list-parameter-errors.yaml))

Observations: none from reporters yet.

## Related errors

- [`invalid page token`](invalid-page-token-400.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`
- [`Page size must be nonnegative.`](negative-page-size-400.md) · GET /v1/projects/{project}/databases/{database}/documents/{collection} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

Match signature (what `check()` matches): ``invalid property path "a b". unquoted property paths must match regex ([a-za-z_][a-za-z_#-#]*), and quoted property paths must match regex (`(?:[^`\\]|(?:\\.))+`)``

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://firestore.googleapis.com/v1/projects/{project}/databases/{database}/documents/{collection}"},"error":{"status":400,"body_excerpt":"invalid property path \"a b\". unquoted property paths must match regex ([a-za-z_][a-za-z_#-#]*), and quoted property paths must match regex (`(?:[^`\\\\]|(?:\\\\.))+`)"}}'
```

YAML: [facts/google-firestore/invalid-field-path-400.yaml](../../facts/google-firestore/invalid-field-path-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
