# Retrieving a deleted customer returns HTTP 200 with a stub object (id, object, deleted: true) instead of 404; fields such as email are absent.

**Stripe API · GET /v1/customers/{id} · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-07 · 29 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:deleted-customer`](../../probes/stripe/deleted-customer.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Step 2 → HTTP 200:

```http
DELETE https://api.stripe.com/v1/customers/<step[1].json.id>
Authorization: Bearer <key>
```

Step 3 → HTTP 200:

```http
GET https://api.stripe.com/v1/customers/<step[1].json.id>
Authorization: Bearer <key>
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "deleted": true,
  "object": "customer"
}
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:deleted-customer` (declarative, [source](../../probes/stripe/deleted-customer.yaml))

Observations: none from reporters yet.

## Related errors

- [`No such customer: 'cus_apifactsnosuch'`](customer-not-found.md) · GET /v1/customers/{id} · HTTP 404 `resource_missing`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.stripe.com/v1/customers/{id}"},"error":{"status":200}}'
```

YAML: [facts/stripe/deleted-customer-returns-200.yaml](../../facts/stripe/deleted-customer-returns-200.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
