# Anonymous calls to the search endpoints count against a separate search resource with x-ratelimit-limit 10 (documented as 10 requests per minute), not against core.

**GitHub REST API · GET /search/repositories**

Status: ✅ verified:server:prod · first seen 2026-10-20 · last confirmed 2026-11-09 · 324 confirmations from 2 vantages

## What to do

1. Retry with exponential backoff from 6000 ms × 2, cap 60000 ms, ≤ 5 attempts, with jitter.

## Example

What probe [`af:github:probe:search-query-too-long`](../../probes/github/search-query-too-long.yaml) sends (prod) and what it checks in the answer.

```http
GET https://api.github.com/search/repositories?q=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 422
X-RateLimit-Resource: search
X-RateLimit-Limit: 10

{
  "message": "Validation Failed",
  "errors": [
    {
      "message": "The search is longer than 256 characters.",
      "field": "q",
      "code": "invalid"
    }
  ],
  "status": "422"
}
```

## In your code

Fix 1:

```python
import random
import time

delay_ms = 6000
for attempt in range(5):
    response = client.send(request)
    if response.is_success:
        break
    time.sleep(random.uniform(0, delay_ms) / 1000)
    delay_ms = min(delay_ms * 2, 60000)
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:github:probe:search-query-too-long` (declarative, [source](../../probes/github/search-query-too-long.yaml)) · official doc: <https://docs.github.com/en/rest/search/search#rate-limit>

Observations: none from reporters yet.

## Related errors

- [`Only the first 1000 search results are available`](search-first-1000-results.md) · GET /search/repositories · HTTP 422
- [`The search is longer than 256 characters.`](search-query-longer-than-256.md) · GET /search/repositories · HTTP 422 `invalid`

## Machine access

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.github.com/search/repositories"}}'
```

YAML: [facts/github/anonymous-search-rate-limit.yaml](../../facts/github/anonymous-search-rate-limit.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
