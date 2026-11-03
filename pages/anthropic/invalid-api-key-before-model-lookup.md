# `invalid x-api-key`

**Claude API (Anthropic) · GET /v1/models/{model_id} · HTTP 401 `authentication_error`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-03 · 46 confirmations from 2 vantages

> GET /v1/models/{model_id} with an invalid x-api-key returns HTTP 401 "invalid x-api-key" even for a model id that does not exist: the key is checked before the model.

## What to do

1. Send header x-api-key = the account setting api_key.

## Example

What probe [`af:anthropic:probe:invalid-key`](../../probes/anthropic/invalid-key.yaml) sends (prod) and what it checks in the answer; `apifacts-invalid-key` is a deliberately wrong key.

Step 1 → HTTP 401:

```http
GET https://api.anthropic.com/v1/models
x-api-key: apifacts-invalid-key
```

Step 2 → HTTP 401:

```http
GET https://api.anthropic.com/v1/models/claude-agent-facts-no-such-model
x-api-key: apifacts-invalid-key
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "error": {
    "message": "invalid x-api-key"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `anthropic` | `anthropic.AuthenticationError` | `e.status_code == 401` · `e.type == "authentication_error"` |
| Node `@anthropic-ai/sdk` | `Anthropic.AuthenticationError` | `err.status === 401` · `err.type === "authentication_error"` |

Read from the SDK source: anthropic 2.3.0: anthropic/\_client.py Anthropic.\_make_status_error; @anthropic-ai/sdk 1.3.0: core/error.js APIError.generate.

Fix 1:

```python
headers["x-api-key"] = YOUR_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:anthropic:probe:invalid-key` (declarative, [source](../../probes/anthropic/invalid-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`x-api-key header is required`](missing-api-key-before-model-lookup.md) · GET /v1/models/{model_id} · HTTP 401 `authentication_error`
- [Errors are a JSON object {type: "error", error: {type, message}, request_id}; the vendor code is error.type (e.g. authentication_error) and the request id also comes in the request-id header.](error-envelope.md) · GET /v1/models · HTTP 401
- [`invalid x-api-key`](invalid-api-key-401.md) · GET /v1/models · HTTP 401 `authentication_error`
- [`x-api-key header is required`](missing-api-key-401.md) · GET /v1/models · HTTP 401 `authentication_error`

## Machine access

Match signature (what `check()` matches): `invalid x-api-key`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.anthropic.com/v1/models/{model_id}"},"error":{"status":401,"body_excerpt":"invalid x-api-key"}}'
```

YAML: [facts/anthropic/invalid-api-key-before-model-lookup.yaml](../../facts/anthropic/invalid-api-key-before-model-lookup.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
