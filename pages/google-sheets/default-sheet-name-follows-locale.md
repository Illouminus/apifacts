# `Unable to parse range: Sheet1!A1`

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 125 confirmations from 2 vantages

> The first sheet is not always Sheet1: on this French-locale spreadsheet it is Feuille 1, and Sheet1!A1 returns HTTP 400 "Unable to parse range: Sheet1!A1"; a range without a sheet name reads the first sheet.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-sheets:probe:default-sheet-name-localized`](../../probes/google-sheets/default-sheet-name-localized.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1KQGUVQhCtk9f6Cy8vnTefNWJw_eKvtowwjA3vL0qR7I/values/Sheet1!A1?key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "status": "INVALID_ARGUMENT",
    "message": "Unable to parse range: Sheet1!A1"
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

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-sheets:probe:default-sheet-name-localized` (declarative, [source](../../probes/google-sheets/default-sheet-name-localized.yaml))

Observations: none from reporters yet.

## Related errors

- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid value at 'value_render_option' (type.googleapis.com/google.apps.sheets.v4.ValueRenderOption), "PRETTY"`](invalid-value-render-option-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Unable to parse range: AgentFactsNoSuchSheet!A1`](unknown-sheet-unable-to-parse.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Unable to parse range: AgentFactsNoSuchSheet!A1`](batch-get-fails-whole.md) · GET /v4/spreadsheets/{spreadsheet_id}/values:batchGet · HTTP 400 `INVALID_ARGUMENT`
- [`Request contains an invalid argument.`](invalid-fields-mask-generic-400.md) · GET /v4/spreadsheets/{spreadsheet_id} · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 403 `PERMISSION_DENIED`

## Machine access

Match signature (what `check()` matches): `unable to parse range: sheet#!a#`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"},"error":{"status":400,"body_excerpt":"unable to parse range: sheet#!a#"}}'
```

YAML: [facts/google-sheets/default-sheet-name-follows-locale.yaml](../../facts/google-sheets/default-sheet-name-follows-locale.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
