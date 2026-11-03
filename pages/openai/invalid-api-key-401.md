# `Incorrect API key provided: apifacts********-key. You can find your API key at https://platform.openai.com/account/api-keys.`

**OpenAI API · GET /v1/models · HTTP 401 `invalid_api_key`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-03 · 45 confirmations from 2 vantages

> A request whose Bearer key is not a valid key returns HTTP 401 error.code invalid_api_key "Incorrect API key provided: …"; the message echoes the key masked (first 8 characters, asterisks, last 4), so the message differs per key while the code stays the same.

## What to do

1. Send header Authorization = the account setting bearer_api_key.

## Example

What probe [`af:openai:probe:invalid-key`](../../probes/openai/invalid-key.yaml) sends (prod) and what it checks in the answer; `apifacts-invalid-key` is a deliberately wrong key.

```http
GET https://api.openai.com/v1/models
Authorization: Bearer apifacts-invalid-key
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401
www-authenticate: <matches ^Bearer realm=>

{
  "error": {
    "code": "invalid_api_key",
    "type": "invalid_request_error",
    "message": "Incorrect API key provided: apifacts********-key. You can find your API key at https://platform.openai.com/account/api-keys."
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

Probe `af:openai:probe:invalid-key` (declarative, [source](../../probes/openai/invalid-key.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors are a JSON object {error: {message, type, param, code}}; code can be null (a missing key), so the vendor code is error.code when set, else error.type, and the request id comes only in the x-request-id header.](error-envelope.md) · GET /v1/models · HTTP 401
- [`Missing bearer authentication in header`](missing-api-key-401.md) · GET /v1/models · HTTP 401 `invalid_request_error`
- [`Incorrect API key provided: apifacts********-key. You can find your API key at https://platform.openai.com/account/api-keys.`](invalid-api-key-before-model-lookup.md) · GET /v1/models/{model} · HTTP 401 `invalid_api_key`
- [`Missing bearer authentication in header`](missing-api-key-before-model-lookup.md) · GET /v1/models/{model} · HTTP 401 `invalid_request_error`

## Machine access

Match signature (what `check()` matches): `incorrect api key provided: apifacts********-key. you can find your api key at <url>`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.openai.com/v1/models"},"error":{"status":401,"body_excerpt":"incorrect api key provided: apifacts********-key. you can find your api key at <url>"}}'
```

YAML: [facts/openai/invalid-api-key-401.yaml](../../facts/openai/invalid-api-key-401.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
