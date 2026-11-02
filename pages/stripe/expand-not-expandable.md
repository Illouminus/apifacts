# `This property cannot be expanded (data.agent_facts).`

**Stripe API · GET /v1/customers · HTTP 400**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-01 · 30 confirmations from 2 vantages

> An expand\[\] path that is not expandable returns HTTP 400 invalid_request_error without an error code; the message quotes the path.

## What to do

1. Omit query parameter expand.

## Example

What probe [`af:stripe:probe:expand-not-expandable`](../../probes/stripe/expand-not-expandable.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
GET https://api.stripe.com/v1/customers?limit=1&expand%5B0%5D=data.agent_facts
Authorization: Bearer <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "type": "invalid_request_error",
    "message": "This property cannot be expanded (data.agent_facts)."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.InvalidRequestError` | `e.http_status == 400` |
| Node `stripe` | `Stripe.errors.StripeInvalidRequestError` | `err.statusCode === 400` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

Fix 1:

```python
params.pop("expand", None)
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:expand-not-expandable` (declarative, [source](../../probes/stripe/expand-not-expandable.yaml))

Observations: none from reporters yet.

## Related errors

- [`Invalid Stripe API version: 2099-01-01`](invalid-api-version-400.md) · GET /v1/customers · HTTP 400
- [`Invalid integer: abc`](limit-not-an-integer.md) · GET /v1/customers · HTTP 400 `parameter_invalid_integer`
- [`No such customer: 'cus_apifactsnosuch'`](starting-after-missing-object.md) · GET /v1/customers · HTTP 400 `resource_missing`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): `this property cannot be expanded (data.agent_facts).`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers"},"error":{"status":400,"body_excerpt":"this property cannot be expanded (data.agent_facts)."}}'
```

YAML: [facts/stripe/expand-not-expandable.yaml](../../facts/stripe/expand-not-expandable.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
