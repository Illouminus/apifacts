# `Bad Request: invalid file_id`

**Telegram Bot API · GET /{bot_token}/getFile · HTTP 400**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-09 · 1256 confirmations from 2 vantages

> getFile with a file_id that is not one Telegram issued returns HTTP 400 "Bad Request: invalid file_id".

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:get-file-invalid`](../../probes/telegram/get-file-invalid.yaml) sends (prod) and what it checks in the answer; the real key is elided.

```http
GET https://api.telegram.org/bot<key>/getFile?file_id=apifacts
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "description": "Bad Request: invalid file_id"
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

Probe `af:telegram:probe:get-file-invalid` (declarative, [source](../../probes/telegram/get-file-invalid.yaml))

Observations: none from reporters yet.

## Related errors

- [`Bad Request: chat_id is empty`](chat-id-empty-400.md) · GET /{bot_token}/getChat · HTTP 400
- [`Bad Request: chat not found`](chat-not-found-400.md) · GET /{bot_token}/getChat · HTTP 400
- [Errors are a JSON object with ok: false, a description and an integer error_code equal to the HTTP status (documented as subject to change); there is no result field.](error-envelope-ok-false.md) · GET /{bot_token}/{method} · HTTP 400
- [`Bad Request: user not found`](user-not-found-400.md) · GET /{bot_token}/{method} · HTTP 400

## Machine access

Match signature (what `check()` matches): `bad request: invalid file_id`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/getFile"},"error":{"status":400,"body_excerpt":"bad request: invalid file_id"}}'
```

YAML: [facts/telegram/invalid-file-id-400.yaml](../../facts/telegram/invalid-file-id-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
