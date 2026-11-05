# `Authentication required, not authenticated`

**Linear API · GET /graphql · HTTP 401 `AUTHENTICATION_ERROR`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-05 · 54 confirmations from 2 vantages

> A query without an Authorization header returns HTTP 401 (not 200 with errors) and errors\[0\].extensions.code AUTHENTICATION_ERROR "Authentication required, not authenticated", before the query is resolved: an issue id that does not exist is the same 401.

## What to do

1. Send header Authorization = the account setting api_key.

## Example

What probe [`af:linear:probe:no-key`](../../probes/linear/no-key.yaml) sends (prod) and what it checks in the answer.

Step 1 → HTTP 401:

```http
GET https://api.linear.app/graphql?query=%7B+viewer+%7B+id+%7D+%7D
Content-Type: application/json
```

Step 2 → HTTP 401:

```http
GET https://api.linear.app/graphql?query=%7B+issue%28id:+%22agent-facts-no-such-issue%22%29+%7B+id+%7D+%7D
Content-Type: application/json
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 401

{
  "errors": [
    {
      "extensions": {
        "code": "AUTHENTICATION_ERROR"
      }
    }
  ]
}
```

## In your code

Fix 1:

```python
headers["Authorization"] = YOUR_API_KEY
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:linear:probe:no-key` (declarative, [source](../../probes/linear/no-key.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors are a GraphQL body {errors: \[{message, extensions: {code, type, statusCode, userError, userPresentableMessage, http}}\]} sent with a matching HTTP status; the vendor code is errors\[0\].extensions.code and the request id comes in the x-request-id header.](error-envelope.md) · GET /graphql · HTTP 401
- [`Authentication required, not authenticated`](invalid-api-key-same-as-missing.md) · GET /graphql · HTTP 401 `AUTHENTICATION_ERROR`
- [`This operation has been blocked as a potential Cross-Site Request Forgery (CSRF). Please either specify a 'content-type' header (with a type that is not one of application/x-www-form-urlencoded, multipart/form-data, text/plain) or provide a non-empty value for one of the following headers: x-apollo-operation-name, apollo-require-preflight`](graphql-get-csrf-400.md) · GET /graphql · HTTP 400 `BAD_REQUEST`

## Machine access

Match signature (what `check()` matches): `authentication required, not authenticated`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.linear.app/graphql"},"error":{"status":401,"body_excerpt":"authentication required, not authenticated"}}'
```

YAML: [facts/linear/missing-api-key-401.yaml](../../facts/linear/missing-api-key-401.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
