# GET /services/data on the org's instance answers HTTP 200 with the list of API versions (version, url) without any credential, while /limits on the same host needs a session.

**Salesforce Platform REST API · GET /services/data · HTTP 200**

Status: ✅ verified:server:sandbox · first seen 2026-10-24 · last confirmed 2026-11-10 · 444 confirmations from 2 vantages

## What to do

1. No client-side fix known (by design).

## Example

What probe [`af:salesforce:probe:versions-without-session`](../../probes/salesforce/versions-without-session.yaml) sends (sandbox) and what it checks in the answer; the real key is elided.

Step 1 → HTTP 200:

```http
GET https://<org>.my.salesforce.com/services/data/v62.0/limits
Authorization: Bearer <access token>
```

Step 2 → HTTP 200:

```http
GET https://login.salesforce.com/services/data
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

[
  {
    "version": "…",
    "url": "…"
  }
]
```

## Dimensions

env: sandbox · plan: any · region: any · account_state: developer_edition

## Evidence

Probe `af:salesforce:probe:versions-without-session` (declarative, [source](../../probes/salesforce/versions-without-session.yaml))

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://login.salesforce.com/services/data"},"error":{"status":200}}'
```

YAML: [facts/salesforce/version-list-needs-no-session.yaml](../../facts/salesforce/version-list-needs-no-session.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
