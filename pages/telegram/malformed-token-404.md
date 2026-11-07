# `Not Found`

**Telegram Bot API · GET /{bot_token}/getMe · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-07 · 1093 confirmations from 2 vantages

> A /bot\<token\>/ segment whose token lacks the \<digits\>:\<secret\> shape returns HTTP 404 "Not Found", the same answer as an unknown method, not 401.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:invalid-token`](../../probes/telegram/invalid-token.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 401:

```http
GET https://api.telegram.org/bot[redacted]/getMe
```

Step 2 → HTTP 404:

```http
GET https://api.telegram.org/botapifacts/getMe
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "description": "Not Found"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `python-telegram-bot` (community) | `telegram.error.InvalidToken` | — |
| Node `telegraf` (community) | `TelegramError` | `err.code === 404` |

Read from the SDK source: python-telegram-bot 22.8: telegram/request/\_baserequest.py BaseRequest.\_request_wrapper; telegraf 4.16.3: lib/core/network/client.js callApi, lib/core/network/error.js.

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:telegram:probe:invalid-token` (declarative, [source](../../probes/telegram/invalid-token.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](unknown-method-404.md) · GET /{bot_token}/{method} · HTTP 404
- [`Unauthorized`](invalid-token-401.md) · GET /{bot_token}/getMe · HTTP 401

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/getMe"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/telegram/malformed-token-404.yaml](../../facts/telegram/malformed-token-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
