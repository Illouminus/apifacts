# `Model is not found: models/gemini-flash-latest for api version v1`

**Gemini API · GET /v1/models/{model} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-01 · 149 confirmations from 2 vantages

> The alias gemini-flash-latest and preview models such as gemini-3-flash-preview answer on v1beta but return HTTP 404 NOT_FOUND on v1.

## What to do

1. Call GET /v1beta/models/{model} instead.

## Example

What probe [`af:google-gemini:probe:latest-alias-v1beta-only`](../../probes/google-gemini/latest-alias-v1beta-only.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest
x-goog-api-key: <key>
```

Step 2 → HTTP 404:

```http
GET https://generativelanguage.googleapis.com/v1/models/gemini-flash-latest
x-goog-api-key: <key>
```

Step 3 → HTTP 404:

```http
GET https://generativelanguage.googleapis.com/v1/models/gemini-3-flash-preview
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
response = client.request("GET", f"/v1beta/models/{model}")
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:latest-alias-v1beta-only` (declarative, [source](../../probes/google-gemini/latest-alias-v1beta-only.yaml))

Observations: none from reporters yet.

## Related errors

- [`Model is not found: models/gemini-1.5-flash for api version v1beta`](gemini-1-5-models-retired.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`
- [`Model is not found: models/gemini-agent-facts-nosuch for api version v1beta`](model-not-found-404.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`

## Machine access

Match signature (what `check()` matches): `model is not found: models/gemini-flash-latest for api version v#`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1/models/{model}"},"error":{"status":404,"body_excerpt":"model is not found: models/gemini-flash-latest for api version v#"}}'
```

YAML: [facts/google-gemini/latest-aliases-v1beta-only.yaml](../../facts/google-gemini/latest-aliases-v1beta-only.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
