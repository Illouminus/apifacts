# maxResults=5000, above the documented page maximum of 2500, is accepted with HTTP 200 rather than refused (the error message for 0 even gives the range as \[1, ∞)).

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 153 confirmations from 2 vantages

## What to do

1. Paginate by nextPageToken via pageToken, ≤ 2500 per page.

## Example

What probe [`af:google-calendar:probe:max-results-bounds`](../../probes/google-calendar/max-results-bounds.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 400:

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?maxResults=0&key=<key>
```

Step 2 → HTTP 200:

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?maxResults=5000&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:max-results-bounds` (declarative, [source](../../probes/google-calendar/max-results-bounds.yaml)) · official doc: <https://developers.google.com/workspace/calendar/api/v3/reference/events/list>

Observations: none from reporters yet.

## Related errors

- [`Not Found`](calendar-not-found-404.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404
- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Invalid value '0'. Values must be within the range: [1, ∞)`](max-results-zero-refused.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [Rate limiting shows up as HTTP 403 with reason rateLimitExceeded or userRateLimitExceeded (domain usageLimits) or as HTTP 429 rateLimitExceeded; a 403 is not always a permission problem.](rate-limit-403-or-429.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":200}}'
```

YAML: [facts/google-calendar/max-results-above-2500-accepted.yaml](../../facts/google-calendar/max-results-above-2500-accepted.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
