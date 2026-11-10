# `Method not found`

**Solana JSON-RPC (public mainnet endpoint) · POST / · HTTP 200 `-32601`**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-10 · 248 confirmations from 2 vantages

> getConfirmedBlock is removed from mainnet RPC nodes: calling it returns JSON-RPC error -32601 Method not found; its replacement is getBlock with commitment confirmed.

## What to do

1. Set body parameter method to getBlock.

## Example

What probe [`af:solana:probe:methods-removed`](../../probes/solana/methods-removed.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 200:

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getRecentBlockhash"}
```

Step 2 → HTTP 200:

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getConfirmedBlock", "params": [1]}
```

Step 3 → HTTP 200:

```http
POST https://api.mainnet-beta.solana.com/
Content-Type: application/json

{"jsonrpc": "2.0", "id": 1, "method": "getConfirmedTransaction", "params": ["5kV4NF6HuXJgNHWNzHVzZXNHe3XCpVdtEnzvRu9Kbt4pJsBqCa5qNPm3Ao5BJWUdqqASd3BSzdDNZk8DfEQYBRta"]}
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "error": {
    "code": -32601
  }
}
```

## In your code

Fix 1:

```python
body["method"] = "getBlock"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:solana:probe:methods-removed` (declarative, [source](../../probes/solana/methods-removed.yaml)) · official doc: <https://solana.com/docs/rpc/deprecated#migration-summary>

Observations: none from reporters yet.

## Related errors

- [`Your IP or provider is blocked from this endpoint`](get-program-accounts-blocked-403.md) · POST / · HTTP 403 `403`
- [On the public RPC endpoints HTTP 403 means the IP address or website has been blocked; high-traffic websites may be blocked without prior notice.](public-endpoint-403-blocked.md) · POST / · HTTP 403
- [The public mainnet endpoint allows 100 requests per 10 s per IP, 40 per 10 s per IP for a single RPC method, 40 concurrent connections and 100 MB per 30 s; exceeding them returns HTTP 429 with Retry-After.](public-mainnet-rate-limits.md) · POST / · HTTP 429

## Machine access

Match signature (what `check()` matches): `method not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"POST","url":"https://api.mainnet-beta.solana.com/"},"error":{"status":200,"body_excerpt":"method not found"}}'
```

YAML: [facts/solana/get-confirmed-block-removed.yaml](../../facts/solana/get-confirmed-block-removed.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
