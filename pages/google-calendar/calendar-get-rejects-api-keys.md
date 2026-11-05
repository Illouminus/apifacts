# `API keys are not supported by this API. Expected OAuth2 access token or other authentication credentials that assert a principal. See https://cloud.google.com/docs/authentication`

**Google Calendar API · GET /calendar/v3/calendars/{calendar_id} · HTTP 401 `UNAUTHENTICATED`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-05 · 1036 confirmations from 2 vantages

> The API key that lists a public calendar's events gets HTTP 401 UNAUTHENTICATED ("API keys are not supported by this API") on calendars.get and users/me/calendarList.

## What to do

1. Request OAuth scope https://www.googleapis.com/auth/calendar.readonly.

## Example

What probe [`af:google-calendar:probe:calendar-get-needs-oauth`](../../probes/google-calendar/calendar-get-needs-oauth.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://www.googleapis.com/calendar/v3/calendars/916ea40bea99d99c310e2aab42492c44500629a59cd44e4f50a73d08a15b3c9a@group.calendar.google.com?key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "error": {
    "status": "UNAUTHENTICATED",
    "message": "API keys are not supported by this API. Expected OAuth2 access token or other authentication credentials that assert a principal. See https://cloud.google.com/docs/authentication"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `google-api-python-client` | `googleapiclient.errors.HttpError` | `e.status_code == 401` |
| Node `googleapis` | `GaxiosError` | `err.status === 401` |

Read from the SDK source: google-api-python-client 2.201.0: googleapiclient/http.py HttpRequest.execute; googleapis 189.0.0 → googleapis-common 9 → gaxios 8.3.2: build/cjs/src/gaxios.js, common.js GaxiosError.

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-calendar:probe:calendar-get-needs-oauth` (declarative, [source](../../probes/google-calendar/calendar-get-needs-oauth.yaml))

Observations: none from reporters yet.

## Machine access

Match signature (what `check()` matches): `api keys are not supported by this api. expected oauth# access token or other authentication credentials that assert a principal. see <url>`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://www.googleapis.com/calendar/v3/calendars/{calendar_id}"},"error":{"status":401,"body_excerpt":"api keys are not supported by this api. expected oauth# access token or other authentication credentials that assert a principal. see <url>"}}'
```

YAML: [facts/google-calendar/calendar-get-rejects-api-keys.yaml](../../facts/google-calendar/calendar-get-rejects-api-keys.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
