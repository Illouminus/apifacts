# `Received unknown parameter: agent_facts_unknown`

**Stripe API · POST /v1/customers · HTTP 400 `parameter_unknown`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-01 · 28 confirmations from 2 vantages

> A 400 for a parameter that fails validation, such as parameter_unknown, is not saved under its Idempotency-Key: a retry with the same key is executed again and has no Idempotent-Replayed header.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:validation-error-not-replayed`](../../probes/stripe/validation-error-not-replayed.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 400:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

agent_facts_unknown=1
```

Step 2 → HTTP 400:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

agent_facts_unknown=1
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "error": {
    "code": "parameter_unknown"
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.InvalidRequestError` | `e.http_status == 400` · `e.code == "parameter_unknown"` |
| Node `stripe` | `Stripe.errors.StripeInvalidRequestError` | `err.statusCode === 400` · `err.code === "parameter_unknown"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:validation-error-not-replayed` (declarative, [source](../../probes/stripe/validation-error-not-replayed.yaml))

Observations: none from reporters yet.

## Related errors

- [`Idempotent key length is 256 characters long, which is outside accepted lengths. Idempotent Keys must be 1-255 characters long. If you're looking for a decent generator, try using a UUID defined by IETF RFC 4122.`](idempotency-key-too-long.md) · POST /v1/customers · HTTP 400 `idempotency_error`
- [`Received unknown parameter: agent_facts_unknown`](parameter-unknown.md) · POST /v1/customers · HTTP 400 `parameter_unknown`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Keys for idempotent requests can only be used for the same endpoint they were first used for ('/v1/payment_intents' vs '/v1/customers'). Try using a key other than '3f1e9c2a-7b4d-4e8f-9a6c-1d2b3c4d5e6f' if you meant to execute a different request."`](idempotency-key-other-endpoint.md) · POST /v1/payment_intents · HTTP 400 `idempotency_error`

## Machine access

Match signature (what `check()` matches): `received unknown parameter: agent_facts_unknown`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/customers"},"error":{"status":400,"body_excerpt":"received unknown parameter: agent_facts_unknown"}}'
```

YAML: [facts/stripe/validation-errors-are-not-replayed.yaml](../../facts/stripe/validation-errors-are-not-replayed.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
