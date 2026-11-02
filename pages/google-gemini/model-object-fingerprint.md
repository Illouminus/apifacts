# A model object from GET /v1beta/models/{model} has 12 top-level keys (description, displayName, inputTokenLimit, maxTemperature, name, outputTokenLimit, supportedGenerationMethods, temperature, thinking, topK, topP, version).

**Gemini API · GET /v1beta/models/{model} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-02 · 168 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-gemini:probe:model-schema-fingerprint`](../../probes/google-gemini/model-schema-fingerprint.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:model-schema-fingerprint` (declarative, [source](../../probes/google-gemini/model-schema-fingerprint.yaml))

Observations: none from reporters yet.

## Related errors

- [`Model is not found: models/gemini-1.5-flash for api version v1beta`](gemini-1-5-models-retired.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`
- [`Model is not found: models/gemini-agent-facts-nosuch for api version v1beta`](model-not-found-404.md) · GET /v1beta/models/{model} · HTTP 404 `NOT_FOUND`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models/{model}"},"error":{"status":200}}'
```

YAML: [facts/google-gemini/model-object-fingerprint.yaml](../../facts/google-gemini/model-object-fingerprint.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
