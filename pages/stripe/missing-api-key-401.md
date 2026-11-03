# `You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/.`

**Stripe API · GET /v1/customers · HTTP 401**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-03 · 33 confirmations from 2 vantages

> A request without an Authorization header returns HTTP 401 with error type invalid_request_error and no error.code; the message says no API key was provided.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:no-api-key`](../../probes/stripe/no-api-key.yaml) sends (sandbox) and what it checks in the answer.

```http
GET https://api.stripe.com/v1/customers
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "error": {
    "type": "invalid_request_error",
    "message": "You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/."
  }
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `stripe` | `stripe.AuthenticationError` | `e.http_status == 401` |
| Node `stripe` | `Stripe.errors.StripeAuthenticationError` | `err.statusCode === 401` |

Read from the SDK source: stripe 16.1.0: stripe/\_api_requestor.py specific_v1_api_error, stripe/\_error.py; stripe 23.1.0: cjs/Error.js generateV1Error, cjs/RequestSender.js.

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:no-api-key` (declarative, [source](../../probes/stripe/no-api-key.yaml))

Observations: none from reporters yet.

## Related errors

- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Invalid Stripe API version: 2099-01-01`](invalid-api-version-400.md) · GET /v1/customers · HTTP 400
- [`Invalid integer: abc`](limit-not-an-integer.md) · GET /v1/customers · HTTP 400 `parameter_invalid_integer`
- [A rate-limited request returns HTTP 429 with a Stripe-Rate-Limited-Reason header (global-rate, endpoint-rate, global-concurrency, endpoint-concurrency or resource-specific); a 429 without it is not a rate limit, e.g. lock_timeout.](rate-limited-reason-header.md) · GET /v1/customers · HTTP 429
- [`No such customer: 'cus_apifactsnosuch'`](starting-after-missing-object.md) · GET /v1/customers · HTTP 400 `resource_missing`

## Machine access

Match signature (what `check()` matches): `you did not provide an api key. you need to provide your api key in the authorization header, using bearer auth (e.g. 'authorization: <redacted>'). see <url> for details, or we can help at <url>`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers"},"error":{"status":401,"body_excerpt":"you did not provide an api key. you need to provide your api key in the authorization header, using bearer auth (e.g. '\''authorization: <redacted>'\''). see <url> for details, or we can help at <url>"}}'
```

YAML: [facts/stripe/missing-api-key-401.yaml](../../facts/stripe/missing-api-key-401.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
