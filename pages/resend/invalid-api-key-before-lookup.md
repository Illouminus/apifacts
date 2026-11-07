# `API key is invalid`

**Resend · GET /emails/{email_id} · HTTP 400 `validation_error`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-07 · 116 confirmations from 2 vantages

> GET /emails/{email_id} with an invalid API key returns HTTP 400 validation_error "API key is invalid" even for an id that does not exist: the key is checked before the email is looked up, so the 400 says nothing about the id.

## What to do

1. Send header Authorization = the account setting bearer_api_key.

## Example

What probe [`af:resend:probe:invalid-key`](../../probes/resend/invalid-key.yaml) sends (prod) and what it checks in the answer; `apifacts-invalid-key` is a deliberately wrong key.

Step 1 → HTTP 400:

```http
GET https://api.resend.com/domains
Authorization: Bearer apifacts-invalid-key
```

Step 2 → HTTP 400:

```http
GET https://api.resend.com/emails/agent-facts-no-such-email
Authorization: Bearer apifacts-invalid-key
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "name": "validation_error",
  "message": "API key is invalid"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `resend` | `resend.exceptions.ValidationError` | `e.code == 400` · `e.error_type == "validation_error"` |
| Node `resend` | returns `{ data: null, error }` | `error.statusCode === 400` · `error.name === "validation_error"` |

Read from the SDK source: resend 2.50.1: resend/request.py Request.perform, resend/exceptions.py ERRORS; resend 6.37.0: dist/index.cjs Resend.fetchRequest.

Fix 1:

```python
headers["Authorization"] = YOUR_BEARER_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:resend:probe:invalid-key` (declarative, [source](../../probes/resend/invalid-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`API key is invalid`](invalid-api-key-400.md) · GET /domains · HTTP 400 `validation_error`
- [`Missing API Key`](missing-api-key-before-lookup.md) · GET /emails/{email_id} · HTTP 401 `missing_api_key`

## Machine access

Match signature (what `check()` matches): `api key is invalid`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.resend.com/emails/{email_id}"},"error":{"status":400,"body_excerpt":"api key is invalid"}}'
```

YAML: [facts/resend/invalid-api-key-before-lookup.yaml](../../facts/resend/invalid-api-key-before-lookup.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
