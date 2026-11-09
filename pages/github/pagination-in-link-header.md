# List endpoints such as GET /users/{username}/followers return a bare JSON array and give the next and last page URLs only in the Link header (rel="next", rel="last").

**GitHub REST API · GET /users/{username}/followers**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-09 · 672 confirmations from 2 vantages

## What to do

1. Paginate by link via page, ≤ 100 per page.

## Example

What probe [`af:github:probe:followers-per-page-cap`](../../probes/github/followers-per-page-cap.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/users/torvalds/followers?per_page=500
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 200
Link: <matches per_page=500&page=2>; rel="next">
Link: <matches rel="last">
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:followers-per-page-cap` (declarative, [source](../../probes/github/followers-per-page-cap.yaml)) · official doc: <https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api#using-link-headers>

Observations: none from reporters yet.

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/users/{username}/followers"}}'
```

YAML: [facts/github/pagination-in-link-header.yaml](../../facts/github/pagination-in-link-header.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
