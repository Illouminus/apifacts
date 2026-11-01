# For a bot without a webhook, getWebhookInfo returns url as an empty string rather than omitting it, and getUpdates answers ok: true.

**Telegram Bot API · GET /{bot_token}/{method} · HTTP 200**

Status: ✅ verified:server:prod · first seen 2026-10-24 · last confirmed 2026-11-01 · 362 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:telegram:probe:no-webhook-state`](../../probes/telegram/no-webhook-state.yaml) sends (prod) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
GET https://api.telegram.org/bot<key>/getWebhookInfo
```

Step 2 → HTTP 200:

```http
GET https://api.telegram.org/bot<key>/getUpdates?limit=1
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "ok": true
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: no_webhook

## Evidence

Probe `af:telegram:probe:no-webhook-state` (declarative, [source](../../probes/telegram/no-webhook-state.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors are a JSON object with ok: false, a description and an integer error_code equal to the HTTP status (documented as subject to change); there is no result field.](error-envelope-ok-false.md) · GET /{bot_token}/{method} · HTTP 400
- [`Not Found`](unknown-method-404.md) · GET /{bot_token}/{method} · HTTP 404
- [`Bad Request: user not found`](user-not-found-400.md) · GET /{bot_token}/{method} · HTTP 400

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.telegram.org/{bot_token}/{method}"},"error":{"status":200}}'
```

YAML: [facts/telegram/no-webhook-url-empty-string.yaml](../../facts/telegram/no-webhook-url-empty-string.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
