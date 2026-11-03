# Public mainnet responses carry x-ratelimit-\* headers: tier free, a per-method limit (x-ratelimit-method-limit), a per-IP rate limit (x-ratelimit-rps-limit) and x-ratelimit-conn-limit 40.

**Solana JSON-RPC (public mainnet endpoint) · POST /**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-03 · 164 confirmations from 2 vantages

## What to do

1. Wait the number of seconds in Retry-After, then retry (≤ 3 attempts).

## Example

What probe [`af:solana:probe:rate-limit-headers`](../../probes/solana/rate-limit-headers.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 200:

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getHealth"}
```

Step 2 → HTTP 200:

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getBlock", "params": [1, {"transactionDetails": "none", "rewards": false, "maxSupportedTransactionVersion": 0}]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
X-RateLimit-Method-Limit: <matches ^[0-9]+$>
```

## In your code

Fix 1:

```python
import time

for attempt in range(3):
    response = client.send(request)
    if "Retry-After" not in response.headers:
        break
    time.sleep(float(response.headers["Retry-After"]))
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:rate-limit-headers` (declarative, [source](../../probes/solana/rate-limit-headers.yaml))

Observations: none from reporters yet.

## Related errors

- [`Your IP or provider is blocked from this endpoint`](get-program-accounts-blocked-403.md) · POST / · HTTP 403 `403`
- [On the public RPC endpoints HTTP 403 means the IP address or website has been blocked; high-traffic websites may be blocked without prior notice.](public-endpoint-403-blocked.md) · POST / · HTTP 403
- [The public mainnet endpoint allows 100 requests per 10 s per IP, 40 per 10 s per IP for a single RPC method, 40 concurrent connections and 100 MB per 30 s; exceeding them returns HTTP 429 with Retry-After.](public-mainnet-rate-limits.md) · POST / · HTTP 429

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.mainnet-beta.solana.com/"}}'
```

YAML: [facts/solana/per-method-rate-limit-headers.yaml](../../facts/solana/per-method-rate-limit-headers.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
