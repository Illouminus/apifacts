# `Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-01 · 93 confirmations from 2 vantages

> events.list on a public calendar with no API key or token returns HTTP 403 ("Method doesn't allow unregistered callers").

## What to do

1. Set query parameter key to the account setting api_key.

## Example

What probe [`af:google-calendar:probe:no-api-key`](../../probes/google-calendar/no-api-key.yaml) sends (prod) and what it checks in the answer.

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 403

{
  "error": {
    "message": "Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-api-python-client` | `googleapiclient.errors.HttpError` | `e.status_code == 403` |
| Node `googleapis` | `GaxiosError` | `err.status === 403` |

Read from the SDK source: google-api-python-client 2.201.0: googleapiclient/http.py HttpRequest.execute; googleapis 189.0.0 → googleapis-common 9 → gaxios 8.3.2: build/cjs/src/gaxios.js, common.js GaxiosError.

Fix 1:

```python
params["key"] = YOUR_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:google-calendar:probe:no-api-key` (declarative, [source](../../probes/google-calendar/no-api-key.yaml))

Observations: none from reporters yet.

## Related errors

- [Rate limiting shows up as HTTP 403 with reason rateLimitExceeded or userRateLimitExceeded (domain usageLimits) or as HTTP 429 rateLimitExceeded; a 403 is not always a permission problem.](rate-limit-403-or-429.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403
- [`Not Found`](calendar-not-found-404.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404
- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Invalid value '0'. Values must be within the range: [1, ∞)`](max-results-zero-refused.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Sync token cannot be used with other request restrictions.`](sync-token-with-time-min-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400

## Machine access

Match signature (what `check()` matches): `method doesn't allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":403,"body_excerpt":"method doesn'\''t allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api."}}'
```

YAML: [facts/google-calendar/missing-api-key-403.yaml](../../facts/google-calendar/missing-api-key-403.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
