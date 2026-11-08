# The untouched first sheet of a new spreadsheet has a grid of 1000 rows by 26 columns (gridProperties.rowCount and columnCount), the bounds ranges are clipped to.

**Google Sheets API · GET /v4/spreadsheets/{spreadsheet_id} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-08 · 699 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:google-sheets:probe:new-sheet-grid`](../../probes/google-sheets/new-sheet-grid.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://sheets.googleapis.com/v4/spreadsheets/1KQGUVQhCtk9f6Cy8vnTefNWJw_eKvtowwjA3vL0qR7I?fields=sheets.properties&key=<key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "sheets": [
    {
      "properties": {
        "gridProperties": {
          "rowCount": 1000,
          "columnCount": 26
        },
        "title": "Feuille 1"
      }
    }
  ]
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: api_key

## Evidence

Probe `af:google-sheets:probe:new-sheet-grid` (declarative, [source](../../probes/google-sheets/new-sheet-grid.yaml))

Observations: none from reporters yet.

## Related errors

- [`Request contains an invalid argument.`](invalid-fields-mask-generic-400.md) · GET /v4/spreadsheets/{spreadsheet_id} · HTTP 400 `INVALID_ARGUMENT`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}"},"error":{"status":200}}'
```

YAML: [facts/google-sheets/new-sheet-grid-1000x26.yaml](../../facts/google-sheets/new-sheet-grid-1000x26.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
