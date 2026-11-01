# `Your IP or provider is blocked from this endpoint`

**Solana JSON-RPC (public mainnet endpoint) · POST / · HTTP 403 `403`**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-01 · 138 confirmations from 2 vantages

> On 2026-10-20 getProgramAccounts on the public mainnet endpoint returned HTTP 403 with error Your IP or provider is blocked from this endpoint to an IP whose other calls were served.

## What to do

1. No client-side fix known (vendor side).

## Example

What probe [`af:solana:probe:program-accounts-blocked`](../../probes/solana/program-accounts-blocked.yaml) sends (prod) and what it checks in the answer.

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getProgramAccounts", "params": ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 403

{
  "error": {
    "code": 403,
    "message": "Your IP or provider is blocked from this endpoint"
  }
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:program-accounts-blocked` (declarative, [source](../../probes/solana/program-accounts-blocked.yaml))

Observations: none from reporters yet.

## Related errors

- [On the public RPC endpoints HTTP 403 means the IP address or website has been blocked; high-traffic websites may be blocked without prior notice.](public-endpoint-403-blocked.md) · POST / · HTTP 403
- [The public mainnet endpoint allows 100 requests per 10 s per IP, 40 per 10 s per IP for a single RPC method, 40 concurrent connections and 100 MB per 30 s; exceeding them returns HTTP 429 with Retry-After.](public-mainnet-rate-limits.md) · POST / · HTTP 429

## Machine access

Match signature (what `check()` matches): `your ip or provider is blocked from this endpoint`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.mainnet-beta.solana.com/"},"error":{"status":403,"body_excerpt":"your ip or provider is blocked from this endpoint"}}'
```

YAML: [facts/solana/get-program-accounts-blocked-403.yaml](../../facts/solana/get-program-accounts-blocked-403.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
