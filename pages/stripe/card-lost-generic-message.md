# `Your card was declined.`

**Stripe API · POST /v1/payment_intents · HTTP 402 `card_declined`**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-07 · 33 confirmations from 2 vantages

> For test payment method pm_card_visa_chargeDeclinedLostCard the 402 message is the generic "Your card was declined."; the reason is only in decline_code lost_card, with advice_code do_not_try_again.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:card-lost`](../../probes/stripe/card-lost.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
POST https://api.stripe.com/v1/payment_intents
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

amount=1000&currency=usd&payment_method=pm_card_visa_chargeDeclinedLostCard&confirm=true&automatic_payment_methods[enabled]=true&automatic_payment_methods[allow_redirects]=never
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 402

{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "decline_code": "lost_card",
    "advice_code": "do_not_try_again",
    "message": "Your card was declined."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.CardError` | `e.http_status == 402` · `e.code == "card_declined"` |
| Node `stripe` | `Stripe.errors.StripeCardError` | `err.statusCode === 402` · `err.code === "card_declined"` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:card-lost` (declarative, [source](../../probes/stripe/card-lost.yaml))

Observations: none from reporters yet.

## Related errors

- [`Your card was declined.`](card-declined-generic.md) · POST /v1/payment_intents · HTTP 402 `card_declined`
- [`Your card has expired.`](card-expired.md) · POST /v1/payment_intents · HTTP 402 `expired_card`
- [`Your card's security code is incorrect.`](card-incorrect-cvc.md) · POST /v1/payment_intents · HTTP 402 `incorrect_cvc`
- [`Your card has insufficient funds. Use a different payment method to complete this purchase.`](card-insufficient-funds.md) · POST /v1/payment_intents · HTTP 402 `card_declined`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](amount-too-small.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`
- [`Amount must convert to at least 50 cents. $0.10 converts to approximately €0.09.`](execution-errors-are-replayed.md) · POST /v1/payment_intents · HTTP 400 `amount_too_small`

## Machine access

Match signature (what `check()` matches): `your card was declined.`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/payment_intents"},"error":{"status":402,"body_excerpt":"your card was declined."}}'
```

YAML: [facts/stripe/card-lost-generic-message.yaml](../../facts/stripe/card-lost-generic-message.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
