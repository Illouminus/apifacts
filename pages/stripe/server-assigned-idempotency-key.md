# A POST sent without an Idempotency-Key header is answered with an Idempotency-Key response header holding a UUID chosen by Stripe; a GET gets no such header.

**Stripe API · POST /v1/customers · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-05 · 27 confirmations from 2 vantages

## What to do

1. Send header Idempotency-Key = new UUID per distinct request.

## Example

What probe [`af:stripe:probe:server-idempotency-key`](../../probes/stripe/server-idempotency-key.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

```http
POST https://api.stripe.com/v1/customers
Authorization: Bearer <key>
Content-Type: application/x-www-form-urlencoded

description=agent-facts+probe
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Idempotency-Key: <matches ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$>
```

## In your code

Fix 1:

```python
import uuid
headers["Idempotency-Key"] = str(uuid.uuid4())  # a new value per distinct request; reuse it only to retry
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: any

## Evidence

Probe `af:stripe:probe:server-idempotency-key` (declarative, [source](../../probes/stripe/server-idempotency-key.yaml))

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

YAML: [facts/stripe/server-assigned-idempotency-key.yaml](../../facts/stripe/server-assigned-idempotency-key.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
