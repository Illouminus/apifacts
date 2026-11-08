# `Missing API Key`

**Resend · GET /emails/{email_id} · HTTP 401 `missing_api_key`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-08 · 133 confirmations from 2 vantages

> GET /emails/{email_id} without an API key returns HTTP 401 missing_api_key even for an id that does not exist: the key is checked before the email is looked up, so the 401 says nothing about the id.

## What to do

1. Send header Authorization = the account setting bearer_api_key.

## Example

What probe [`af:resend:probe:no-key`](../../probes/resend/no-key.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 401:

```http
GET https://api.resend.com/domains
```

Step 2 → HTTP 401:

```http
GET https://api.resend.com/emails/agent-facts-no-such-email
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "name": "missing_api_key"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `resend` | `resend.exceptions.MissingApiKeyError` | `e.code == 401` · `e.error_type == "missing_api_key"` |
| Node `resend` | returns `{ data: null, error }` | `error.statusCode === 401` · `error.name === "missing_api_key"` |

Read from the SDK source: resend 2.50.1: resend/request.py Request.perform, resend/exceptions.py ERRORS; resend 6.37.0: dist/index.cjs Resend.fetchRequest.

Fix 1:

```python
headers["Authorization"] = YOUR_BEARER_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:resend:probe:no-key` (declarative, [source](../../probes/resend/no-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`Missing API Key`](missing-api-key-401.md) · GET /domains · HTTP 401 `missing_api_key`
- [`API key is invalid`](invalid-api-key-before-lookup.md) · GET /emails/{email_id} · HTTP 400 `validation_error`

## Machine access

Match signature (what `check()` matches): `missing api key`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.resend.com/emails/{email_id}"},"error":{"status":401,"body_excerpt":"missing api key"}}'
```

YAML: [facts/resend/missing-api-key-before-lookup.yaml](../../facts/resend/missing-api-key-before-lookup.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
