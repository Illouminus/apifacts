# `Unable to parse range: AgentFactsNoSuchSheet!A1`

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id}/values:batchGet · HTTP 400 `INVALID_ARGUMENT`**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 1401 confirmations from 2 vantages

> values:batchGet with an unparsable range fails as a whole with HTTP 400 "Unable to parse range"; without any ranges it returns 200 and no valueRanges field.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-sheets:probe:batch-get-one-bad-range`](../../probes/google-sheets/batch-get-one-bad-range.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1KQGUVQhCtk9f6Cy8vnTefNWJw_eKvtowwjA3vL0qR7I/values:batchGet?ranges=AgentFactsNoSuchSheet%21A1&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "message": "Unable to parse range: AgentFactsNoSuchSheet!A1"
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

Probe `af:google-sheets:probe:batch-get-one-bad-range` (declarative, [source](../../probes/google-sheets/batch-get-one-bad-range.yaml))

Observations: none from reporters yet.

## Related errors

- [`Unable to parse range: Sheet1!A1`](default-sheet-name-follows-locale.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`API key not valid. Please pass a valid API key.`](invalid-api-key-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Request contains an invalid argument.`](invalid-fields-mask-generic-400.md) · GET /v4/spreadsheets/{spreadsheet_id} · HTTP 400 `INVALID_ARGUMENT`
- [`Invalid value at 'value_render_option' (type.googleapis.com/google.apps.sheets.v4.ValueRenderOption), "PRETTY"`](invalid-value-render-option-400.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`
- [`Unable to parse range: AgentFactsNoSuchSheet!A1`](unknown-sheet-unable-to-parse.md) · GET /v4/spreadsheets/{spreadsheet_id}/values/{range} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

Match signature (what `check()` matches): `unable to parse range: apifactsnosuchsheet!a#`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values:batchGet"},"error":{"status":400,"body_excerpt":"unable to parse range: apifactsnosuchsheet!a#"}}'
```

YAML: [facts/google-sheets/batch-get-fails-whole.yaml](../../facts/google-sheets/batch-get-fails-whole.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
