# `Model is not found: models/gemini-agent-facts-nosuch for api version v1beta`

**Gemini API · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 321 confirmations from 2 vantages

> An unknown model name returns HTTP 404 NOT_FOUND with the message "Model is not found: models/\<name\> for api version v1beta".

## What to do

1. Call GET /v1beta/models instead.

## Example

What probe [`af:google-gemini:probe:model-not-found`](../../probes/google-gemini/model-not-found.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-agent-facts-nosuch
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": {
    "status": "NOT_FOUND",
    "message": "Model is not found: models/gemini-agent-facts-nosuch for api version v1beta"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-genai` | `google.genai.errors.ClientError` | `e.code == 404` · `e.status == "NOT_FOUND"` |
| Node `@google/genai` | `ApiError` | `err.status === 404` |

Read from the SDK source: google-genai 2.34.0: google/genai/errors.py APIError.raise_error; @google/genai 2.32.0: dist/node/index.cjs throwErrorIfNotOK, class ApiError.

Fix 1:

```python
response = client.request("GET", "/v1beta/models")
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:model-not-found` (declarative, [source](../../probes/google-gemini/model-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Model is not found: models/gemini-1.5-flash for api version v1beta`](gemini-1-5-models-retired.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`
- [`Model is not found: models/gemini-flash-latest for api version v1`](latest-aliases-v1beta-only.md) · GET /v1/models/{model} · HTTP 404 `NOT_FOUND`

## Machine access

Match signature (what `check()` matches): `model is not found: models/gemini-agent-facts-nosuch for api version v#beta`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models/{model}"},"error":{"status":404,"body_excerpt":"model is not found: models/gemini-agent-facts-nosuch for api version v#beta"}}'
```

YAML: [facts/google-gemini/model-not-found-404.yaml](../../facts/google-gemini/model-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
