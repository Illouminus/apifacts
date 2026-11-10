# `Unauthorized`

**Telegram Bot API · GET /{bot_token}/getMe · HTTP 401**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-10 · 1313 confirmations from 2 vantages

> A token-shaped bot token (\<digits\>:\<secret\>) that is not valid returns HTTP 401 {ok: false, description: "Unauthorized"}.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:invalid-token`](../../probes/telegram/invalid-token.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.telegram.org/bot[redacted]/getMe
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "ok": false,
  "description": "Unauthorized"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `python-telegram-bot` (community) | `telegram.error.InvalidToken` | — |
| Node `telegraf` (community) | `TelegramError` | `err.code === 401` |

Read from the SDK source: python-telegram-bot 22.8: telegram/request/\_baserequest.py BaseRequest.\_request_wrapper; telegraf 4.16.3: lib/core/network/client.js callApi, lib/core/network/error.js.

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:telegram:probe:invalid-token` (declarative, [source](../../probes/telegram/invalid-token.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](malformed-token-404.md) · GET /{bot_token}/getMe · HTTP 404

## Machine access

Match signature (what `check()` matches): `unauthorized`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/getMe"},"error":{"status":401,"body_excerpt":"unauthorized"}}'
```

YAML: [facts/telegram/invalid-token-401.yaml](../../facts/telegram/invalid-token-401.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
