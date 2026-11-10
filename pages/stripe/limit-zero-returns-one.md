# GET /v1/customers?limit=0, outside the documented range 1-100, is not rejected: it returns a list holding one object, with has_more: true.

**Stripe API · GET /v1/customers · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-09 · 37 confirmations from 2 vantages

## What to do

1. Paginate by id via starting_after, ≤ 100 per page.

## Example

What probe [`af:stripe:probe:limit-zero-returns-one`](../../probes/stripe/limit-zero-returns-one.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Step 2:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Step 3 → HTTP 200:

```http
GET https://api.stripe.com/v1/customers?limit=0
Authorization: Bearer <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "object": "list",
  "data": [
    {
      "object": "customer"
    }
  ],
  "has_more": true
}
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:limit-zero-returns-one` (declarative, [source](../../probes/stripe/limit-zero-returns-one.yaml))

Observations: none from reporters yet.

## Related errors

- [`This property cannot be expanded (data.agent_facts).`](expand-not-expandable.md) · GET /v1/customers · HTTP 400
- [`Invalid Stripe API version: 2099-01-01`](invalid-api-version-400.md) · GET /v1/customers · HTTP 400
- [`Invalid integer: abc`](limit-not-an-integer.md) · GET /v1/customers · HTTP 400 `parameter_invalid_integer`
- [`You did not provide an API key. You need to provide your API key in the Authorization header, using Bearer auth (e.g. 'Authorization: Bearer YOUR_SECRET_KEY'). See https://stripe.com/docs/api#authentication for details, or we can help at https://support.stripe.com/.`](missing-api-key-401.md) · GET /v1/customers · HTTP 401
- [A rate-limited request returns HTTP 429 with a Stripe-Rate-Limited-Reason header (global-rate, endpoint-rate, global-concurrency, endpoint-concurrency or resource-specific); a 429 without it is not a rate limit, e.g. lock_timeout.](rate-limited-reason-header.md) · GET /v1/customers · HTTP 429
- [`No such customer: 'cus_apifactsnosuch'`](starting-after-missing-object.md) · GET /v1/customers · HTTP 400 `resource_missing`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers"},"error":{"status":200}}'
```

YAML: [facts/stripe/limit-zero-returns-one.yaml](../../facts/stripe/limit-zero-returns-one.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
