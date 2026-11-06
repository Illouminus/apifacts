# ``The `payment_method_types` parameter is no longer supported. Payment methods are now managed from your Dashboard settings (https://dashboard.stripe.com/settings/payment_methods). For migration guidance, see https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.``

**Stripe API · POST /v1/payment_intents · HTTP 400**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-05 · 26 confirmations from 2 vantages

> On API version 2026-09-30.endive, creating a PaymentIntent with payment_method_types returns HTTP 400 (no error code, parameter no longer supported); the same request on version 2024-06-20 succeeds.

## What to do

1. Omit body parameter payment_method_types.

## Example

What probe [`af:stripe:probe:payment-method-types-removed`](../../probes/stripe/payment-method-types-removed.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
POST https://api.stripe.com/v1/payment_intents
Authorization: Bearer <key>
Stripe-Version: 2026-09-30.endive
Content-Type: application/x-www-form-urlencoded

amount=100&currency=usd&payment_method_types[0]=card
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400
Stripe-Version: 2026-09-30.endive

{
  "error": {
    "type": "invalid_request_error",
    "message": "The `payment_method_types` parameter is no longer supported. Payment methods are now managed from your Dashboard settings (https://dashboard.stripe.com/settings/payment_methods). For migration guidance, see https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods."
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
body.pop("payment_method_types", None)
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:payment-method-types-removed` (declarative, [source](../../probes/stripe/payment-method-types-removed.yaml))

Observations: none from reporters yet.

## Related errors

- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`
- [`Keys for idempotent requests can only be used with the same parameters they were first used with. Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request.`](idempotency-key-reuse-different-params.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`
- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Idempotent key length is 256 characters long, which is outside accepted lengths. Idempotent Keys must be 1-255 characters long. If you're looking for a decent generator, try using a UUID defined by IETF RFC 4122.`](idempotency-key-too-long.md) · POST /v1/customers · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): ``the `payment_method_types` parameter is no longer supported. payment methods are now managed from your dashboard settings (<url>). for migration guidance, see <url>``

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/payment_intents"},"error":{"status":400,"body_excerpt":"the `payment_method_types` parameter is no longer supported. payment methods are now managed from your dashboard settings (<url>). for migration guidance, see <url>"}}'
```

YAML: [facts/stripe/payment-method-types-removed.yaml](../../facts/stripe/payment-method-types-removed.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
