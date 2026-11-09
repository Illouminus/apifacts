# gemini-2.0-flash, whose earliest shutdown date on the deprecations page is June 1, 2026, still answers GET /v1beta/models/gemini-2.0-flash with HTTP 200 and version 2.0.

**Gemini API · GET /v1beta/models/{model} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 302 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-gemini:probe:gemini-2-0-flash-served`](../../probes/google-gemini/gemini-2-0-flash-served.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "name": "models/gemini-2.0-flash",
  "version": "2.0"
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:gemini-2-0-flash-served` (declarative, [source](../../probes/google-gemini/gemini-2-0-flash-served.yaml)) · official doc: <https://ai.google.dev/gemini-api/docs/deprecations>

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

YAML: [facts/google-gemini/gemini-2-0-flash-served-past-shutdown-date.yaml](../../facts/google-gemini/gemini-2-0-flash-served-past-shutdown-date.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
