# On 2026-10-20 getMinimumBalanceForRentExemption with dataLength 0 returned 650240 lamports on mainnet.

**Solana JSON-RPC (public mainnet endpoint) · POST /**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-04 · 176 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:solana:probe:rent-exemption-zero-bytes`](../../probes/solana/rent-exemption-zero-bytes.yaml) sends (prod) and what it checks in the answer.

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getMinimumBalanceForRentExemption", "params": [0]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "result": 650240
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:rent-exemption-zero-bytes` (declarative, [source](../../probes/solana/rent-exemption-zero-bytes.yaml))

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

YAML: [facts/solana/rent-exemption-minimum-zero-bytes.yaml](../../facts/solana/rent-exemption-minimum-zero-bytes.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
