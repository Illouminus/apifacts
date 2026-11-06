# `Not Found`

**Telegram Bot API · GET /{bot_token}/{method} · HTTP 404**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 556 confirmations from 2 vantages

> A method name the Bot API does not know returns HTTP 404 {ok: false, error_code: 404, description: "Not Found"}.

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:unknown-method`](../../probes/telegram/unknown-method.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://api.telegram.org/bot<key>/agentFactsNoSuchMethod
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 404

{
  "error_code": 404,
  "description": "Not Found"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `python-telegram-bot` (community) | `telegram.error.TelegramError` | — |
| Node `telegraf` (community) | `TelegramError` | `err.code === 404` |

Read from the SDK source: python-telegram-bot 22.8: telegram/request/\_baserequest.py BaseRequest.\_request_wrapper; telegraf 4.16.3: lib/core/network/client.js callApi, lib/core/network/error.js.

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:telegram:probe:unknown-method` (declarative, [source](../../probes/telegram/unknown-method.yaml))

Observations: none from reporters yet.

## Related errors

- [`Not Found`](malformed-token-404.md) · GET /{bot_token}/getMe · HTTP 404
- [Errors are a JSON object with ok: false, a description and an integer error_code equal to the HTTP status (documented as subject to change); there is no result field.](error-envelope-ok-false.md) · GET /{bot_token}/{method} · HTTP 400
- [`Bad Request: user not found`](user-not-found-400.md) · GET /{bot_token}/{method} · HTTP 400

## Machine access

Match signature (what `check()` matches): `not found`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/{method}"},"error":{"status":404,"body_excerpt":"not found"}}'
```

YAML: [facts/telegram/unknown-method-404.yaml](../../facts/telegram/unknown-method-404.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
