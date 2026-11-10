# `Missing bearer authentication in header`

**OpenAI API · GET /v1/models/{model} · HTTP 401 `invalid_request_error`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-10 · 166 confirmations from 2 vantages

> GET /v1/models/{model} without an Authorization header returns HTTP 401 "Missing bearer authentication in header" even for a model id that does not exist: the key is checked before the model, so the 401 says nothing about the id.

## What to do

1. Send header Authorization = the account setting bearer_api_key.

## Example

What probe [`af:openai:probe:no-key`](../../probes/openai/no-key.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 401:

```http
GET https://api.openai.com/v1/models
```

Step 2 → HTTP 401:

```http
GET https://api.openai.com/v1/models/gpt-agent-facts-no-such-model
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "error": {
    "message": "Missing bearer authentication in header"
  }
}
```

## In your code

Fix 1:

```python
headers["Authorization"] = YOUR_BEARER_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:openai:probe:no-key` (declarative, [source](../../probes/openai/no-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`Incorrect API key provided: apifacts********-key. You can find your API key at https://platform.openai.com/account/api-keys.`](invalid-api-key-before-model-lookup.md) · GET /v1/models/{model} · HTTP 401 `invalid_api_key`
- [Errors are a JSON object {error: {message, type, param, code}}; code can be null (a missing key), so the vendor code is error.code when set, else error.type, and the request id comes only in the x-request-id header.](error-envelope.md) · GET /v1/models · HTTP 401
- [`Incorrect API key provided: apifacts********-key. You can find your API key at https://platform.openai.com/account/api-keys.`](invalid-api-key-401.md) · GET /v1/models · HTTP 401 `invalid_api_key`
- [`Missing bearer authentication in header`](missing-api-key-401.md) · GET /v1/models · HTTP 401 `invalid_request_error`

## Machine access

Match signature (what `check()` matches): `missing bearer authentication in header`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.openai.com/v1/models/{model}"},"error":{"status":401,"body_excerpt":"missing bearer authentication in header"}}'
```

YAML: [facts/openai/missing-api-key-before-model-lookup.yaml](../../facts/openai/missing-api-key-before-model-lookup.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
