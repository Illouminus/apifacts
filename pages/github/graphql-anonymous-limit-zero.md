# For anonymous callers GET /rate_limit reports a graphql resource limit of 0, so the GraphQL API has no anonymous quota, while REST core allows 60 requests per hour.

**GitHub REST API · GET /rate_limit**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-06 · 571 confirmations from 2 vantages

## What to do

1. Request OAuth scope public_repo.

## Example

What probe [`af:github:probe:rate-limit`](../../probes/github/rate-limit.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/rate_limit
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200

{
  "resources": {
    "core": {
      "limit": 60
    },
    "search": {
      "limit": 10
    },
    "graphql": {
      "limit": 0
    }
  }
}
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:rate-limit` (declarative, [source](../../probes/github/rate-limit.yaml)) · official doc: <https://docs.github.com/en/rest/rate-limit/rate-limit>

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/rate_limit"}}'
```

YAML: [facts/github/graphql-anonymous-limit-zero.yaml](../../facts/github/graphql-anonymous-limit-zero.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
