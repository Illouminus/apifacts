# `Invalid integer: abc`

**Stripe API · GET /v1/customers · HTTP 400 `parameter_invalid_integer`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-02 · 33 confirmations from 2 vantages

> A non-numeric list limit returns HTTP 400 parameter_invalid_integer with error.param limit.

## What to do

1. Set query parameter limit to 100.

## Example

What probe [`af:stripe:probe:limit-not-an-integer`](../../probes/stripe/limit-not-an-integer.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://api.stripe.com/v1/customers?limit=abc
Authorization: Bearer <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "code": "parameter_invalid_integer",
    "param": "limit",
    "message": "Invalid integer: abc"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.InvalidRequestError` | `e.http_status == 400` · `e.code == "parameter_invalid_integer"` |
| Node `stripe` | `Stripe.errors.StripeInvalidRequestError` | `err.statusCode === 400` · `err.code === "parameter_invalid_integer"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

Fix 1:

```python
params["limit"] = "100"
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:limit-not-an-integer` (declarative, [source](../../probes/stripe/limit-not-an-integer.yaml))

Observations: none from reporters yet.

## Related errors

- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Invalid Stripe API version: 2099-01-01`](invalid-api-version-400.md) · GET /v1/customers · HTTP 400
- [`No such customer: 'cus_apifactsnosuch'`](starting-after-missing-object.md) · GET /v1/customers · HTTP 400 `resource_missing`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): `invalid integer: abc`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers"},"error":{"status":400,"body_excerpt":"invalid integer: abc"}}'
```

YAML: [facts/stripe/limit-not-an-integer.yaml](../../facts/stripe/limit-not-an-integer.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
