# Repeating a POST with the same Idempotency-Key and the same body returns the saved first response with the header Idempotent-Replayed: true, which the first response does not carry.

**Stripe API · POST /v1/customers · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-06 · 42 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:stripe:probe:idempotent-replay`](../../probes/stripe/idempotent-replay.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Step 2 → HTTP 200:

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Idempotency-Key: <run_uuid>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Idempotent-Replayed: true

{
  "object": "customer"
}
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:idempotent-replay` (declarative, [source](../../probes/stripe/idempotent-replay.yaml))

Observations: none from reporters yet.

## Related errors

- [`Idempotent key length is 256 characters long, which is outside accepted lengths. Idempotent Keys must be 1-255 characters long. If you're looking for a decent generator, try using a UUID defined by IETF RFC 4122.`](idempotency-key-too-long.md) · POST /v1/customers · HTTP 400 `idempotency_error`
- [`Received unknown parameter: agent_facts_unknown`](parameter-unknown.md) · POST /v1/customers · HTTP 400 `parameter_unknown`
- [`Received unknown parameter: agent_facts_unknown`](validation-errors-are-not-replayed.md) · POST /v1/customers · HTTP 400 `parameter_unknown`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.stripe.com/v1/customers"},"error":{"status":200}}'
```

YAML: [facts/stripe/idempotent-replay-header.yaml](../../facts/stripe/idempotent-replay-header.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
