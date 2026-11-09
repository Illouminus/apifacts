# GET /v1beta/models without pageSize returns 50 models and a nextPageToken; the rest of the list is only reachable with pageToken.

**Gemini API · GET /v1beta/models · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 190 confirmations from 2 vantages

## What to do

1. Paginate by nextPageToken via pageToken, ≤ 1000 per page.

## Example

What probe [`af:google-gemini:probe:models-default-page`](../../probes/google-gemini/models-default-page.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://generativelanguage.googleapis.com/v1beta/models
x-goog-api-key: <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "nextPageToken": "…"
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-gemini:probe:models-default-page` (declarative, [source](../../probes/google-gemini/models-default-page.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors carry the google.rpc envelope: error.code is the HTTP status as a number, error.status a name such as INVALID_ARGUMENT, and error.details\[\] holds objects typed by @type (e.g. google.rpc.BadRequest).](errors-use-google-rpc-envelope.md) · GET /v1beta/models · HTTP 400
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid page_token.`](invalid-page-token-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v1beta/models · HTTP 403 `PERMISSION_DENIED`
- [`* ListModelsRequest.page_size: page_size must be positive`](page-size-negative-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid JSON payload received. Unknown name "agent_facts_unknown": Cannot bind query parameter. Field 'agent_facts_unknown' could not be found in request message.`](unknown-query-parameter-400.md) · GET /v1beta/models · HTTP 400 `INVALID_ARGUMENT`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://generativelanguage.googleapis.com/v1beta/models"},"error":{"status":200}}'
```

YAML: [facts/google-gemini/models-list-default-page-50.yaml](../../facts/google-gemini/models-list-default-page-50.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
