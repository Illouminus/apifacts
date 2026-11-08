# `Keys for idempotent requests can only be used with the same parameters they were first used with. Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request.`

**Stripe API · POST /v1/payment_intents · HTTP 400 `idempotency_error`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-07 · 30 confirmations from 2 vantages

> Reusing an Idempotency-Key with a different request body returns HTTP 400 with error type idempotency_error.

## What to do

1. Send header Idempotency-Key = new UUID per distinct request.

## Example

What probe [`af:stripe:probe:idempotency-key-reuse`](../../probes/stripe/idempotency-key-reuse.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
POST https://api.stripe.com/v1/payment_intents
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

amount=100&currency=usd
```

Step 2 → HTTP 400:

```http
POST https://api.stripe.com/v1/payment_intents
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

amount=200&currency=usd
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "type": "idempotency_error",
    "message": "Keys for idempotent requests can only be used with the same parameters they were first used with. Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.IdempotencyError` | `e.http_status == 400` · `e.error.type == "idempotency_error"` |
| Node `stripe` | `Stripe.errors.StripeIdempotencyError` | `err.statusCode === 400` · `err.rawType === "idempotency_error"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

Fix 1:

```python
import uuid
headers["Idempotency-Key"] = str(uuid.uuid4())  # a new value per distinct request; reuse it only to retry
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:idempotency-key-reuse` (declarative, [source](../../probes/stripe/idempotency-key-reuse.yaml))

Observations: none from reporters yet.

## Related errors

- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`
- [``The `payment_method_types` parameter is no longer supported. Payment methods are now managed from your Dashboard settings (https://dashboard.stripe.com/settings/payment_methods). For migration guidance, see https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.``](payment-method-types-removed.md) · POST /v1/payment_intents · HTTP 400
- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Idempotent key length is 256 characters long, which is outside accepted lengths. Idempotent Keys must be 1-255 characters long. If you're looking for a decent generator, try using a UUID defined by IETF RFC 4122.`](idempotency-key-too-long.md) · POST /v1/customers · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): `keys for idempotent requests can only be used with the same parameters they were first used with. try using a key other than '<id>' if you meant to execute a different request.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/payment_intents"},"error":{"status":400,"body_excerpt":"keys for idempotent requests can only be used with the same parameters they were first used with. try using a key other than '\''<id>'\'' if you meant to execute a different request."}}'
```

YAML: [facts/stripe/idempotency-key-reuse-different-params.yaml](../../facts/stripe/idempotency-key-reuse-different-params.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
