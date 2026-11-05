# `Sync token is no longer valid, a full sync is required.`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 410**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-05 · 141 confirmations from 2 vantages

> A syncToken the server does not know, even a made-up string, returns HTTP 410 Gone (reason fullSyncRequired), not 400.

## What to do

1. Omit query parameter syncToken.

## Example

What probe [`af:google-calendar:probe:sync-token-errors`](../../probes/google-calendar/sync-token-errors.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?syncToken=apifacts&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 410

{
  "error": {
    "message": "Sync token is no longer valid, a full sync is required.",
    "errors": [
      {
        "reason": "fullSyncRequired"
      }
    ]
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-api-python-client` | `googleapiclient.errors.HttpError` | `e.status_code == 410` |
| Node `googleapis` | `GaxiosError` | `err.status === 410` |

Read from the SDK source: google-api-python-client 2.201.0: googleapiclient/http.py HttpRequest.execute; googleapis 189.0.0 → googleapis-common 9 → gaxios 8.3.2: build/cjs/src/gaxios.js, common.js GaxiosError.

Fix 1:

```python
params.pop("syncToken", None)
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:sync-token-errors` (declarative, [source](../../probes/google-calendar/sync-token-errors.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](calendar-not-found-404.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404
- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Invalid value '0'. Values must be within the range: [1, ∞)`](max-results-zero-refused.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [Rate limiting shows up as HTTP 403 with reason rateLimitExceeded or userRateLimitExceeded (domain usageLimits) or as HTTP 429 rateLimitExceeded; a 403 is not always a permission problem.](rate-limit-403-or-429.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403

## Machine access

Match signature (what `check()` matches): `sync token is no longer valid, a full sync is required.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":410,"body_excerpt":"sync token is no longer valid, a full sync is required."}}'
```

YAML: [facts/google-calendar/unknown-sync-token-410.yaml](../../facts/google-calendar/unknown-sync-token-410.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
