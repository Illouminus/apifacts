# Errors are a JSON object with ok: false, a description and an integer error_code equal to the HTTP status (documented as subject to change); there is no result field.

**Telegram Bot API · GET /{bot_token}/{method} · HTTP 400**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-06 · 342 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:error-envelope`](../../probes/telegram/error-envelope.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://api.telegram.org/bot<key>/getChat
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "ok": false,
  "error_code": 400,
  "description": "…"
}
```

## In your code

When an SDK receives this response:

| SDK | Raises | Check |
| --- | --- | --- |
| Python `python-telegram-bot` (community) | `telegram.error.BadRequest` | — |
| Node `telegraf` (community) | `TelegramError` | `err.code === 400` |

Read from the SDK source: python-telegram-bot 22.8: telegram/request/\_baserequest.py BaseRequest.\_request_wrapper; telegraf 4.16.3: lib/core/network/client.js callApi, lib/core/network/error.js.

## Dimensions

env: prod · plan: any · region: any · account_state: any

## Evidence

Probe `af:telegram:probe:error-envelope` (declarative, [source](../../probes/telegram/error-envelope.yaml)) · official doc: <https://core.telegram.org/bots/api#making-requests>

Observations: none from reporters yet.

## Related errors

- [`Bad Request: user not found`](user-not-found-400.md) · GET /{bot_token}/{method} · HTTP 400
- [`Bad Request: chat_id is empty`](chat-id-empty-400.md) · GET /{bot_token}/getChat · HTTP 400
- [`Bad Request: chat not found`](chat-not-found-400.md) · GET /{bot_token}/getChat · HTTP 400
- [`Bad Request: invalid file_id`](invalid-file-id-400.md) · GET /{bot_token}/getFile · HTTP 400
- [`Not Found`](unknown-method-404.md) · GET /{bot_token}/{method} · HTTP 404

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/{method}"},"error":{"status":400}}'
```

YAML: [facts/telegram/error-envelope-ok-false.yaml](../../facts/telegram/error-envelope-ok-false.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
