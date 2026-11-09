# `Not Found`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 190 confirmations from 2 vantages

> events.list on a calendar id that does not exist returns HTTP 404 "Not Found" with error.errors\[0\].reason notFound and no error.status.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-calendar:probe:calendar-not-found`](../../probes/google-calendar/calendar-not-found.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://www.googleapis.com/calendar/v3/calendars/agent-facts-no-such-calendar@group.calendar.google.com/events?key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": {
    "message": "Not Found",
    "errors": [
      {
        "reason": "notFound"
      }
    ]
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-api-python-client` | `googleapiclient.errors.HttpError` | `e.status_code == 404` |
| Node `googleapis` | `GaxiosError` | `err.status === 404` |

Read from the SDK source: google-api-python-client 2.201.0: googleapiclient/http.py HttpRequest.execute; googleapis 189.0.0 → googleapis-common 9 → gaxios 8.3.2: build/cjs/src/gaxios.js, common.js GaxiosError.

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:calendar-not-found` (declarative, [source](../../probes/google-calendar/calendar-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Invalid value '0'. Values must be within the range: [1, ∞)`](max-results-zero-refused.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [Rate limiting shows up as HTTP 403 with reason rateLimitExceeded or userRateLimitExceeded (domain usageLimits) or as HTTP 429 rateLimitExceeded; a 403 is not always a permission problem.](rate-limit-403-or-429.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403
- [`Sync token cannot be used with other request restrictions.`](sync-token-with-time-min-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/google-calendar/calendar-not-found-404.yaml](../../facts/google-calendar/calendar-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
