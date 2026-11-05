# `Model is not found: models/gemini-1.5-flash for api version v1beta`

**Gemini API · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-05 · 226 confirmations from 2 vantages

> The model names gemini-1.5-flash, gemini-1.5-pro and gemini-pro return HTTP 404 NOT_FOUND on GET /v1beta/models/\<name\>.

## What to do

1. Call GET /v1beta/models instead.

## Example

What probe [`af:google-gemini:probe:gemini-1-5-retired`](../../probes/google-gemini/gemini-1-5-retired.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 404:

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash
x-goog-api-key: <key>
```

Step 2 → HTTP 404:

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro
x-goog-api-key: <key>
```

Step 3 → HTTP 404:

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-pro
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404
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

Probe `af:google-gemini:probe:gemini-1-5-retired` (declarative, [source](../../probes/google-gemini/gemini-1-5-retired.yaml))

Observations: none from reporters yet.

## Related errors

- [`Model is not found: models/gemini-agent-facts-nosuch for api version v1beta`](model-not-found-404.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`
- [`Model is not found: models/gemini-flash-latest for api version v1`](latest-aliases-v1beta-only.md) · GET /v1/models/{model} · HTTP 404 `NOT_FOUND`

## Machine access

Match signature (what `check()` matches): `model is not found: models/gemini-#.#-flash for api version v#beta`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models/{model}"},"error":{"status":404,"body_excerpt":"model is not found: models/gemini-#.#-flash for api version v#beta"}}'
```

YAML: [facts/google-gemini/gemini-1-5-models-retired.yaml](../../facts/google-gemini/gemini-1-5-models-retired.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
