# `This operation has been blocked as a potential Cross-Site Request Forgery (CSRF). Please either specify a 'content-type' header (with a type that is not one of application/x-www-form-urlencoded, multipart/form-data, text/plain) or provide a non-empty value for one of the following headers: x-apollo-operation-name, apollo-require-preflight`

**Linear API · GET /graphql · HTTP 400 `BAD_REQUEST`**

Status: ✅ verified:server:prod · first seen 2026-10-31 · last confirmed 2026-11-04 · 43 confirmations from 2 vantages

> GET /graphql without a Content-Type is blocked as a potential CSRF: HTTP 400 BAD_REQUEST in a GraphQL errors\[\] body, before the key is checked (an Authorization header gets the same 400). With Content-Type: application/json the same GET reaches authentication.

## What to do

1. Send header Content-Type = application/json.

## Example

What probe [`af:linear:probe:graphql-get-csrf`](../../probes/linear/graphql-get-csrf.yaml) sends (prod) and what it checks in the answer; `apifacts-invalid-key` is a deliberately wrong key.

Step 1 → HTTP 400:

```http
GET https://api.linear.app/graphql?query=%7B+viewer+%7B+id+%7D+%7D
```

Step 2 → HTTP 400:

```http
GET https://api.linear.app/graphql?query=%7B+viewer+%7B+id+%7D+%7D
Authorization: apifacts-invalid-key
```

Response (only what the probe asserts; other fields omitted):

```http
HTTP 400

{
  "errors": [
    {
      "extensions": {
        "code": "BAD_REQUEST"
      }
    }
  ]
}
```

## In your code

Fix 1:

```python
headers["Content-Type"] = "application/json"
```

## Dimensions

env: prod · plan: any · region: any · account_state: anonymous

## Evidence

Probe `af:linear:probe:graphql-get-csrf` (declarative, [source](../../probes/linear/graphql-get-csrf.yaml))

Observations: none from reporters yet.

## Related errors

- [Errors are a GraphQL body {errors: \[{message, extensions: {code, type, statusCode, userError, userPresentableMessage, http}}\]} sent with a matching HTTP status; the vendor code is errors\[0\].extensions.code and the request id comes in the x-request-id header.](error-envelope.md) · GET /graphql · HTTP 401
- [`Authentication required, not authenticated`](invalid-api-key-same-as-missing.md) · GET /graphql · HTTP 401 `AUTHENTICATION_ERROR`
- [`Authentication required, not authenticated`](missing-api-key-401.md) · GET /graphql · HTTP 401 `AUTHENTICATION_ERROR`

## Machine access

Match signature (what `check()` matches): `this operation has been blocked as a potential cross-site request forgery (csrf). please either specify a 'content-type' header (with a type that is not one of application/x-www-form-urlencoded, multipart/form-data, text/plain) or provide a non-empty value for one of the following headers: x-apollo-operation-name, apollo-require-preflight`

```sh
curl -s https://apifacts.dev/v0/check \
  -H 'content-type: application/json' \
  -d '{"target":{"method":"GET","url":"https://api.linear.app/graphql"},"error":{"status":400,"body_excerpt":"this operation has been blocked as a potential cross-site request forgery (csrf). please either specify a '\''content-type'\'' header (with a type that is not one of application/x-www-form-urlencoded, multipart/form-data, text/plain) or provide a non-empty value for one of the following headers: x-apollo-operation-name, apollo-require-preflight"}}'
```

YAML: [facts/linear/graphql-get-csrf-400.yaml](../../facts/linear/graphql-get-csrf-400.yaml)

---

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) · apifacts registry · This page is generated; edit the YAML, not the page.
