# With valueRenderOption=FORMULA formulas come back as text in the spreadsheet locale's syntax: =DATE(2026;10;24) with semicolons on a fr_FR file, while plain numbers and booleans stay typed.

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 101 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-sheets:probe:fixture-formula-values`](../../probes/google-sheets/fixture-formula-values.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1KQGUVQhCtk9f6Cy8vnTefNWJw_eKvtowwjA3vL0qR7I/values/A1:E5?valueRenderOption=FORMULA&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

$.values[1][2] = "=B2*2"
$.values[1][3] = "=DATE(2026;10;24)"
$.values[1][1] = 3.14159
$.values[1][4] = true
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-sheets:probe:fixture-formula-values` (declarative, [source](../../probes/google-sheets/fixture-formula-values.yaml))

Observations: none from reporters yet.

## Related errors

- [`Unable to parse range: Sheet1!A1`](default-sheet-name-follows-locale.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid value at 'value_render_option' (type.googleapis.com/google.apps.sheets.v4.ValueRenderOption), "PRETTY"`](invalid-value-render-option-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`](missing-api-key-403.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 403 `PERMISSION_DENIED`
- [Read and write requests are each limited to 300 per minute per project and 60 per minute per user per project, refilled every minute; going over returns HTTP 429.](quota-per-project-and-user.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 429
- [`Requested entity was not found.`](spreadsheet-not-found-404.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 404 `NOT_FOUND`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"},"error":{"status":200}}'
```

YAML: [facts/google-sheets/formulas-in-locale-syntax.yaml](../../facts/google-sheets/formulas-in-locale-syntax.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
