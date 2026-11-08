# `No such customer: 'cus_apifactsnosuch'`

**Stripe API · GET /v1/customers/{id} · HTTP 404 `resource_missing`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-08 · 274 confirmations from 2 vantages

> Retrieving a customer id that does not exist returns HTTP 404 resource_missing with error.param id and the id quoted in the message.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:customer-not-found`](../../probes/stripe/customer-not-found.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://api.stripe.com/v1/customers/cus_apifactsnosuch
Authorization: Bearer <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error": {
    "type": "invalid_request_error",
    "code": "resource_missing",
    "param": "id",
    "message": "No such customer: 'cus_apifactsnosuch'"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.InvalidRequestError` | `e.http_status == 404` · `e.code == "resource_missing"` |
| Node `stripe` | `Stripe.errors.StripeInvalidRequestError` | `err.statusCode === 404` · `err.code === "resource_missing"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:customer-not-found` (declarative, [source](../../probes/stripe/customer-not-found.yaml))

Observations: none from reporters yet.

## Machine access

Match signature (what `check()` matches): `no such customer: 'cus_apifactsnosuch'`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers/{id}"},"error":{"status":404,"body_excerpt":"no such customer: '\''cus_apifactsnosuch'\''"}}'
```

YAML: [facts/stripe/customer-not-found.yaml](../../facts/stripe/customer-not-found.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
