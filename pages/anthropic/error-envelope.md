# Errors are a JSON object {type: "error", error: {type, message}, request_id}; the vendor code is error.type (e.g. authentication_error) and the request id also comes in the request-id header.

**Claude API (Anthropic) · GET /v1/models · HTTP 401**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-07 · 116 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:anthropic:probe:no-key`](../../probes/anthropic/no-key.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.anthropic.com/v1/models
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401
request-id: …
x-should-retry: false

{
  "type": "error",
  "error": {
    "type": "authentication_error",
    "message": "x-api-key header is required"
  },
  "request_id": "…"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `anthropic` | `anthropic.AuthenticationError` | `e.status_code == 401` |
| Node `@anthropic-ai/sdk` | `Anthropic.AuthenticationError` | `err.status === 401` |

Read from the SDK source: anthropic 2.3.0: anthropic/\_client.py Anthropic.\_make_status_error; @anthropic-ai/sdk 1.3.0: core/error.js APIError.generate.

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:anthropic:probe:no-key` (declarative, [source](../../probes/anthropic/no-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`invalid x-api-key`](invalid-api-key-401.md) · GET /v1/models · HTTP 401 `authentication_error`
- [`x-api-key header is required`](missing-api-key-401.md) · GET /v1/models · HTTP 401 `authentication_error`
- [`invalid x-api-key`](invalid-api-key-before-model-lookup.md) · GET /v1/models/{model_id} · HTTP 401 `authentication_error`
- [`x-api-key header is required`](missing-api-key-before-model-lookup.md) · GET /v1/models/{model_id} · HTTP 401 `authentication_error`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.anthropic.com/v1/models"},"error":{"status":401}}'
```

YAML: [facts/anthropic/error-envelope.yaml](../../facts/anthropic/error-envelope.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
