# Gemini API

Hosts: `generativelanguage.googleapis.com` · 17 facts

## Error meanings

- ✅ verified:server:prod · [`Model is not found: models/gemini-agent-facts-nosuch for api version v1beta`](model-not-found-404.md) · GET /v1beta/models/{model} · env prod
- ✅ verified:server:prod · [`* ListModelsRequest.page_size: page_size must be positive`](page-size-negative-400.md) · GET /v1beta/models · env prod
- ✅ verified:server:prod · [`Invalid JSON payload received. Unknown name "agent_facts_unknown": Cannot bind query parameter. Field 'agent_facts_unknown' could not be found in request message.`](unknown-query-parameter-400.md) · GET /v1beta/models · env prod

## Rate limits

- 🔵 official · [Requests-per-day quotas reset at midnight Pacific time, not at midnight UTC.](daily-quota-resets-midnight-pacific.md) · POST /v1beta/models/{model_and_method} · env prod
- 🔵 official · [Rate limits (requests per minute, input tokens per minute, requests per day) apply per Google Cloud project, not per API key: several keys of one project share them.](rate-limits-per-project.md) · POST /v1beta/models/{model_and_method} · env prod
- 🔵 official · [Exceeding a rate limit or quota returns HTTP 429 RESOURCE_EXHAUSTED, a transient error, like 503 UNAVAILABLE; 400, 402 and 403 are client errors that a retry does not fix.](resource-exhausted-429.md) · POST /v1beta/models/{model_and_method} · env prod

## Silent behavior

- ✅ verified:server:prod · [Errors carry the google.rpc envelope: error.code is the HTTP status as a number, error.status a name such as INVALID_ARGUMENT, and error.details\[\] holds objects typed by @type (e.g. google.rpc.BadRequest).](errors-use-google-rpc-envelope.md) · GET /v1beta/models · env prod
- ✅ verified:server:prod · [`Model is not found: models/gemini-flash-latest for api version v1`](latest-aliases-v1beta-only.md) · GET /v1/models/{model} · env prod

## Auth quirks

- ✅ verified:server:prod · [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v1beta/models · env prod
- 🔵 official · [`Your API key was reported as leaked. Please use another API key.`](leaked-key-403.md) · POST /v1beta/models/{model_and_method} · env prod
- ⚪ stale · [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v1beta/models · env prod

## Pagination

- ✅ verified:server:prod · [`Invalid page_token.`](invalid-page-token-400.md) · GET /v1beta/models · env prod
- ✅ verified:server:prod · [GET /v1beta/models without pageSize returns 50 models and a nextPageToken; the rest of the list is only reachable with pageToken.](models-list-default-page-50.md) · GET /v1beta/models · env prod
- ✅ verified:server:prod · [pageSize=0 on GET /v1beta/models is not refused: it returns the default page of 50 models with a nextPageToken.](page-size-zero-means-default.md) · GET /v1beta/models · env prod

## Deprecations

- ✅ verified:server:prod · [`Model is not found: models/gemini-1.5-flash for api version v1beta`](gemini-1-5-models-retired.md) · GET /v1beta/models/{model} · env prod
- ✅ verified:server:prod · [gemini-2.0-flash, whose earliest shutdown date on the deprecations page is June 1, 2026, still answers GET /v1beta/models/gemini-2.0-flash with HTTP 200 and version 2.0.](gemini-2-0-flash-served-past-shutdown-date.md) · GET /v1beta/models/{model} · env prod

## Schema drift

- ✅ verified:server:prod · [A model object from GET /v1beta/models/{model} has 12 top-level keys (description, displayName, inputTokenLimit, maxTemperature, name, outputTokenLimit, supportedGenerationMethods, temperature, thinking, topK, topP, version).](model-object-fingerprint.md) · GET /v1beta/models/{model} · env prod

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
