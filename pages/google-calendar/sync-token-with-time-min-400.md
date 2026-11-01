# `Sync token cannot be used with other request restrictions.`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-01 · 93 confirmations from 2 vantages

> A syncToken combined with timeMin returns HTTP 400 "Sync token cannot be used with other request restrictions.".

## What to do

1. Omit query parameter timeMin.

## Example

What probe [`af:google-calendar:probe:sync-token-errors`](../../probes/google-calendar/sync-token-errors.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 410:

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?syncToken=apifacts&key=<key>
```

Step 2:

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?maxResults=1&key=<key>
```

Step 3 → HTTP 400:

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?syncToken=<step%5B2%5D.json.nextSyncToken>&timeMin=<now_rfc3339>&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "message": "Sync token cannot be used with other request restrictions."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-api-python-client` | `googleapiclient.errors.HttpError` | `e.status_code == 400` |
| Node `googleapis` | `GaxiosError` | `err.status === 400` |

Read from the SDK source: google-api-python-client 2.201.0: googleapiclient/http.py HttpRequest.execute; googleapis 189.0.0 → googleapis-common 9 → gaxios 8.3.2: build/cjs/src/gaxios.js, common.js GaxiosError.

Fix 1:

```python
params.pop("timeMin", None)
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:sync-token-errors` (declarative, [source](../../probes/google-calendar/sync-token-errors.yaml))

Observations: none from reporters yet.

## Related errors

- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Invalid value '0'. Values must be within the range: [1, ∞)`](max-results-zero-refused.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Bad Request`](time-min-without-offset-bad-request.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Not Found`](calendar-not-found-404.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403

## Machine access

Match signature (what `check()` matches): `sync token cannot be used with other request restrictions.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":400,"body_excerpt":"sync token cannot be used with other request restrictions."}}'
```

YAML: [facts/google-calendar/sync-token-with-time-min-400.yaml](../../facts/google-calendar/sync-token-with-time-min-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
