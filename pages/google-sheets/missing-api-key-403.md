# `Method doesn't allow unregistered callers (callers without established identity). Please use API Key or other form of API consumer identity to call this API.`

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 403 `PERMISSION_DENIED`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 124 confirmations from 2 vantages

> Reading even a public spreadsheet with no API key or token returns HTTP 403 PERMISSION_DENIED; the message varies ("Method doesn't allow unregistered callers" or "Permission denied on the service.").

## What to do

1. Set query parameter key to the account setting api_key.

## Example

What probe [`af:google-sheets:probe:no-api-key`](../../probes/google-sheets/no-api-key.yaml) sends (prod) and what it checks in the answer.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1KQGUVQhCtk9f6Cy8vnTefNWJw_eKvtowwjA3vL0qR7I/values/A1
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 403

{
  "error": {
    "status": "PERMISSION_DENIED"
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

Probe `af:google-sheets:probe:no-api-key` (declarative, [source](../../probes/google-sheets/no-api-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`Unable to parse range: Sheet1!A1`](default-sheet-name-follows-locale.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid value at 'value_render_option' (type.googleapis.com/google.apps.sheets.v4.ValueRenderOption), "PRETTY"`](invalid-value-render-option-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [Read and write requests are each limited to 300 per minute per project and 60 per minute per user per project, refilled every minute; going over returns HTTP 429.](quota-per-project-and-user.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 429
- [`Requested entity was not found.`](spreadsheet-not-found-404.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 404 `NOT_FOUND`
- [`Unable to parse range: AgentFactsNoSuchSheet!A1`](unknown-sheet-unable-to-parse.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

Match signature (what `check()` matches): `method doesn't allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range}"},"error":{"status":403,"body_excerpt":"method doesn'\''t allow unregistered callers (callers without established identity). please use api key or other form of api consumer identity to call this api."}}'
```

YAML: [facts/google-sheets/missing-api-key-403.yaml](../../facts/google-sheets/missing-api-key-403.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
