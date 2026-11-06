# `Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`

**Gemini API · GET /v1beta/models · HTTP 403 `PERMISSION_DENIED`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 153 confirmations from 2 vantages

> A request with no API key returns HTTP 403 PERMISSION_DENIED ("Method doesn't allow unregistered callers"), not 401.

## What to do

1. Send header x-goog-api-key = the account setting api_key.

## Example

What probe [`af:google-gemini:probe:models-no-key`](../../probes/google-gemini/models-no-key.yaml) sends (prod) and what it checks in the answer.

```http
GET https://generativelanguage.googleapis.com/v1beta/models
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 403

{
  "error": {
    "status": "PERMISSION_DENIED",
    "message": "Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-genai` | `google.genai.errors.ClientError` | `e.code == 403` · `e.status == "PERMISSION_DENIED"` |
| Node `@google/genai` | `ApiError` | `err.status === 403` |

Read from the SDK source: google-genai 2.34.0: google/genai/errors.py APIError.raise_error; @google/genai 2.32.0: dist/node/index.cjs throwErrorIfNotOK, class ApiError.

Fix 1:

```python
headers["x-goog-api-key"] = YOUR_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:models-no-key` (declarative, [source](../../probes/google-gemini/models-no-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`Your API key was reported as leaked. Please use another API key.`](leaked-key-403.md) · POST /v1beta/models/{model_and_method} · HTTP 403 `PERMISSION_DENIED`
- [Errors carry the google.rpc envelope: error.code is the HTTP status as a number, error.status a name such as INVALID_ARGUMENT, and error.details\[\] holds objects typed by @type (e.g. google.rpc.BadRequest).](errors-use-google-rpc-envelope.md) · GET /v1beta/models · HTTP 400
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid page_token.`](invalid-page-token-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`* ListModelsRequest.page_size: page_size must be positive`](page-size-negative-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid JSON payload received. Unknown name "agent_facts_unknown": Cannot bind query parameter. Field 'agent_facts_unknown' could not be found in request message.`](unknown-query-parameter-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`

## Machine access

Match signature (what `check()` matches): `method doesn't allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models"},"error":{"status":403,"body_excerpt":"method doesn'\''t allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api."}}'
```

YAML: [facts/google-gemini/missing-api-key-403.yaml](../../facts/google-gemini/missing-api-key-403.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
