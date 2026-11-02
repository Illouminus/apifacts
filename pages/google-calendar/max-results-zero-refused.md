# `Invalid value '0'. Values must be within the range: [1, ∞)`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-02 · 105 confirmations from 2 vantages

> maxResults=0 returns HTTP 400 "Invalid value '0'. Values must be within the range: \[1, ∞)" (reason invalidParameter).

## What to do

1. Set query parameter maxResults to 250.

## Example

What probe [`af:google-calendar:probe:max-results-bounds`](../../probes/google-calendar/max-results-bounds.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com/events?maxResults=0&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "message": "Invalid value '0'. Values must be within the range: [1, ∞)",
    "errors": [
      {
        "reason": "invalidParameter"
      }
    ]
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
params["maxResults"] = "250"
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:max-results-bounds` (declarative, [source](../../probes/google-calendar/max-results-bounds.yaml))

Observations: none from reporters yet.

## Related errors

- [`Invalid page token value.`](invalid-page-token-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`The requested ordering is not available for the particular query.`](order-by-start-time-needs-single-events.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Sync token cannot be used with other request restrictions.`](sync-token-with-time-min-400.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Bad Request`](time-min-without-offset-bad-request.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 400
- [`Not Found`](calendar-not-found-404.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 404
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /calendar/v3/calendars/{calendar_id}/events · HTTP 403

## Machine access

Match signature (what `check()` matches): `invalid value '#'. values must be within the range: [#, ∞)`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}/events"},"error":{"status":400,"body_excerpt":"invalid value '\''#'\''. values must be within the range: [#, ∞)"}}'
```

YAML: [facts/google-calendar/max-results-zero-refused.yaml](../../facts/google-calendar/max-results-zero-refused.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
