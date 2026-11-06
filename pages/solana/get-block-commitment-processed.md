# `` Method does not support commitment below `confirmed` ``

**Solana JSON-RPC (public mainnet endpoint) · POST / · HTTP 200 `-32602`**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-06 · 200 confirmations from 2 vantages

> getBlock with commitment processed returns JSON-RPC error -32602 Method does not support commitment below \`confirmed\`.

## What to do

1. Set body parameter params\[1\].commitment to confirmed.

## Example

What probe [`af:solana:probe:block-commitment-processed`](../../probes/solana/block-commitment-processed.yaml) sends (prod) and what it checks in the answer.

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getBlock", "params": [1, {"commitment": "processed"}]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "error": {
    "code": -32602,
    "message": "Method does not support commitment below `confirmed`"
  }
}
```

## In your code

Fix 1:

```python
body["params[1].commitment"] = "confirmed"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:block-commitment-processed` (declarative, [source](../../probes/solana/block-commitment-processed.yaml))

Observations: none from reporters yet.

## Related errors

- [`Your IP or provider is blocked from this endpoint`](get-program-accounts-blocked-403.md) · POST / · HTTP 403 `403`
- [On the public RPC endpoints HTTP 403 means the IP address or website has been blocked; high-traffic websites may be blocked without prior notice.](public-endpoint-403-blocked.md) · POST / · HTTP 403
- [The public mainnet endpoint allows 100 requests per 10 s per IP, 40 per 10 s per IP for a single RPC method, 40 concurrent connections and 100 MB per 30 s; exceeding them returns HTTP 429 with Retry-After.](public-mainnet-rate-limits.md) · POST / · HTTP 429

## Machine access

Match signature (what `check()` matches): `` method does not support commitment below `confirmed` ``

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.mainnet-beta.solana.com/"},"error":{"status":200,"body_excerpt":"method does not support commitment below `confirmed`"}}'
```

YAML: [facts/solana/get-block-commitment-processed.yaml](../../facts/solana/get-block-commitment-processed.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
