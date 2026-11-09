# `Requested entity was not found.`

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 404 `NOT_FOUND`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 118 confirmations from 2 vantages

> A spreadsheet id that does not exist returns HTTP 404 NOT_FOUND "Requested entity was not found.".

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-sheets:probe:spreadsheet-not-found`](../../probes/google-sheets/spreadsheet-not-found.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1AgentFactsNoSuchSpreadsheetIdAgentFactsXyz00/values/A1?key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": {
    "status": "NOT_FOUND",
    "message": "Requested entity was not found."
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

Probe `af:google-sheets:probe:spreadsheet-not-found` (declarative, [source](../../probes/google-sheets/spreadsheet-not-found.yaml))

Observations: none from reporters yet.

## Related errors

- [`Unable to parse range: Sheet1!A1`](default-sheet-name-follows-locale.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid value at 'value_render_option' (type.googleapis.com/google.apps.sheets.v4.ValueRenderOption), "PRETTY"`](invalid-value-render-option-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 403 `PERMISSION_DENIED`
- [Read and write requests are each limited to 300 per minute per project and 60 per minute per user per project, refilled every minute; going over returns HTTP 429.](quota-per-project-and-user.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 429
- [`Unable to parse range: AgentFactsNoSuchSheet!A1`](unknown-sheet-unable-to-parse.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

Match signature (what `check()` matches): `requested entity was not found.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"},"error":{"status":404,"body_excerpt":"requested entity was not found."}}'
```

YAML: [facts/google-sheets/spreadsheet-not-found-404.yaml](../../facts/google-sheets/spreadsheet-not-found-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
