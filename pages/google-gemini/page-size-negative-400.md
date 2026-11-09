# `* ListModelsRequest.page_size: page_size must be positive`

**Gemini API · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 189 confirmations from 2 vantages

> A negative pageSize returns HTTP 400 INVALID_ARGUMENT "\* ListModelsRequest.page_size: page_size must be positive".

## What to do

1. Omit query parameter pageSize.

## Example

What probe [`af:google-gemini:probe:models-page-size-negative`](../../probes/google-gemini/models-page-size-negative.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models?pageSize=-1
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "status": "INVALID_ARGUMENT",
    "message": "* ListModelsRequest.page_size: page_size must be positive"
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

Fix 1:

```python
params.pop("pageSize", None)
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:models-page-size-negative` (declarative, [source](../../probes/google-gemini/models-page-size-negative.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors carry the google.rpc envelope: error.code is the HTTP status as a number, error.status a name such as INVALID_ARGUMENT, and error.details\[\] holds objects typed by @type (e.g. google.rpc.BadRequest).](errors-use-google-rpc-envelope.md) · GET /v1beta/models · HTTP 400
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid page_token.`](invalid-page-token-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid JSON payload received. Unknown name "agent_facts_unknown": Cannot bind query parameter. Field 'agent_facts_unknown' could not be found in request message.`](unknown-query-parameter-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v1beta/models · HTTP 403 `PERMISSION_DENIED`

## Machine access

Match signature (what `check()` matches): `* listmodelsrequest.page_size: page_size must be positive`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models"},"error":{"status":400,"body_excerpt":"* listmodelsrequest.page_size: page_size must be positive"}}'
```

YAML: [facts/google-gemini/page-size-negative-400.yaml](../../facts/google-gemini/page-size-negative-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
