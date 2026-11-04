# `Invalid param: WrongSize`

**Solana JSON-RPC (public mainnet endpoint) · POST / · HTTP 200 `-32602`**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-04 · 176 confirmations from 2 vantages

> getBalance with a string that is not a base-58 public key returns JSON-RPC error -32602 Invalid param: WrongSize.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:solana:probe:invalid-pubkey`](../../probes/solana/invalid-pubkey.yaml) sends (prod) and what it checks in the answer.

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getBalance", "params": ["notapubkey"]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "error": {
    "code": -32602,
    "message": "Invalid param: WrongSize"
  }
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:invalid-pubkey` (declarative, [source](../../probes/solana/invalid-pubkey.yaml))

Observations: none from reporters yet.

## Related errors

- [`Your IP or provider is blocked from this endpoint`](get-program-accounts-blocked-403.md) · POST / · HTTP 403 `403`
- [On the public RPC endpoints HTTP 403 means the IP address or website has been blocked; high-traffic websites may be blocked without prior notice.](public-endpoint-403-blocked.md) · POST / · HTTP 403
- [The public mainnet endpoint allows 100 requests per 10 s per IP, 40 per 10 s per IP for a single RPC method, 40 concurrent connections and 100 MB per 30 s; exceeding them returns HTTP 429 with Retry-After.](public-mainnet-rate-limits.md) · POST / · HTTP 429

## Machine access

Match signature (what `check()` matches): `invalid param: wrongsize`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.mainnet-beta.solana.com/"},"error":{"status":200,"body_excerpt":"invalid param: wrongsize"}}'
```

YAML: [facts/solana/invalid-pubkey-wrong-size.yaml](../../facts/solana/invalid-pubkey-wrong-size.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
