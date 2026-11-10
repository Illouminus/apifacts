# `Invalid page_token.`

**Gemini API · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 201 confirmations from 2 vantages

> A pageToken that the API did not issue returns HTTP 400 INVALID_ARGUMENT "Invalid page_token.".

## What to do

1. Paginate by nextPageToken via pageToken, ≤ 1000 per page.

## Example

What probe [`af:google-gemini:probe:models-invalid-page-token`](../../probes/google-gemini/models-invalid-page-token.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models?pageToken=apifacts
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "status": "INVALID_ARGUMENT",
    "message": "Invalid page_token."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-genai` | `google.genai.errors.ClientError` | `e.code == 400` · `e.status == "INVALID_ARGUMENT"` |
| Node `@google/genai` | `ApiError` | `err.status === 400` |

Read from the SDK source: google-genai 2.34.0: google/genai/errors.py APIError.raise_error; @google/genai 2.32.0: dist/node/index.cjs throwErrorIfNotOK, class ApiError.

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:models-invalid-page-token` (declarative, [source](../../probes/google-gemini/models-invalid-page-token.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors carry the google.rpc envelope: error.code is the HTTP status as a number, error.status a name such as INVALID_ARGUMENT, and error.details\[\] holds objects typed by @type (e.g. google.rpc.BadRequest).](errors-use-google-rpc-envelope.md) · GET /v1beta/models · HTTP 400
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`* ListModelsRequest.page_size: page_size must be positive`](page-size-negative-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid JSON payload received. Unknown name "agent_facts_unknown": Cannot bind query parameter. Field 'agent_facts_unknown' could not be found in request message.`](unknown-query-parameter-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v1beta/models · HTTP 403 `PERMISSION_DENIED`

## Machine access

Match signature (what `check()` matches): `invalid page_token.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models"},"error":{"status":400,"body_excerpt":"invalid page_token."}}'
```

YAML: [facts/google-gemini/invalid-page-token-400.yaml](../../facts/google-gemini/invalid-page-token-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
