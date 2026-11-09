# `Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`

**Stripe API · POST /v1/payment_intents · HTTP 400 `amount_too_small`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-09 · 36 confirmations from 2 vantages

> A PaymentIntent with amount 10 and currency usd (10 cents) returns HTTP 400 amount_too_small: the amount must convert to at least 50 cents; on a test account settling in EUR the message also gives the converted amount (€0.09).

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:amount-too-small`](../../probes/stripe/amount-too-small.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
POST https://api.stripe.com/v1/payment_intents
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

amount=10&currency=usd
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "type": "invalid_request_error",
    "code": "amount_too_small",
    "message": "Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.InvalidRequestError` | `e.http_status == 400` · `e.code == "amount_too_small"` |
| Node `stripe` | `Stripe.errors.StripeInvalidRequestError` | `err.statusCode === 400` · `err.code === "amount_too_small"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:amount-too-small` (declarative, [source](../../probes/stripe/amount-too-small.yaml))

Observations: none from reporters yet.

## Related errors

- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`
- [`Keys for idempotent requests can only be used with the same parameters they were first used with. Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request.`](idempotency-key-reuse-different-params.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`
- [``The `payment_method_types` parameter is no longer supported. Payment methods are now managed from your Dashboard settings (https://dashboard.stripe.com/settings/payment_methods). For migration guidance, see https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.``](payment-method-types-removed.md) · POST /v1/payment_intents · HTTP 400
- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Idempotent key length is 256 characters long, which is outside accepted lengths. Idempotent Keys must be 1-255 characters long. If you're looking for a decent generator, try using a UUID defined by IETF RFC 4122.`](idempotency-key-too-long.md) · POST /v1/customers · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): `amount must convert to at least ## cents. $#.## converts to approximately €#.##.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/payment_intents"},"error":{"status":400,"body_excerpt":"amount must convert to at least ## cents. $#.## converts to approximately €#.##."}}'
```

YAML: [facts/stripe/amount-too-small.yaml](../../facts/stripe/amount-too-small.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
