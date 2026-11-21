# 07 · Test-runner plugins and MCP

**Done when (wave 1):** `pip install apifacts-pytest` + `-p apifacts` makes a failing test whose
exception is an HTTP error (`requests.HTTPError`, `httpx.HTTPStatusError`, or an SDK error carrying
`status_code`/`http_status` and `request.url`) print a "Known facts" section in the failure report,
sourced from `POST /v0/check`; nothing is sent when the host is not in the registry's `GET /v0/services`
cache; opt-out `APIFACTS_DISABLE=1`; all of this covered by tests against a local fake server.

## pytest plugin (`plugins/pytest/`, package `apifacts-pytest`)

- Hook: `pytest_runtest_makereport` on failure → walk the exception chain → extract `(method, url,
  status, body_excerpt ≤ 2 KB)` → if host ∈ cached service hosts → `check()` with 2 s timeout →
  append section:

```
──────────── Known facts (apifacts, CC BY 4.0) ────────────
POST api.stripe.com/v1/payment_intents → 400 idempotency_error
✅ verified:server:sandbox · Reusing an Idempotency-Key with a different request body returns HTTP 400 …
   fix: Send header Idempotency-Key = new UUID per distinct request
   https://apifacts.dev/stripe/idempotency-key-reuse-different-params
```

- Privacy: never sends request bodies, headers, query strings or tokens; strips the secret-shaped
  patterns from `body_excerpt` client-side; one request per failure, none on pass.
- Config: `APIFACTS_ENDPOINT` (default `https://apifacts.dev`), `APIFACTS_DISABLE`,
  `--apifacts-offline` (use the cached YAML snapshot shipped in the wheel, no network).
- Cache: `GET /v0/services` hosts list (`hosts` + `instance_hosts`) cached 24 h in `~/.cache/apifacts/`.
  A tenant host such as `<org>.my.salesforce.com` is sent under its registry host (`my.salesforce.com`):
  the org name does not leave the machine; the offline snapshot matches the same way (D-090).

## jest plugin (wave 2, `plugins/jest/`, package `@apifacts/jest`)

Same behaviour via a custom reporter: on test failure inspect `error.response` (axios), `error.status`
+ `error.request` (fetch wrappers, SDKs); same privacy rules; TypeScript, vitest-compatible reporter too.

## MCP server (wave 2, `apifacts/mcp_server.py`)

One tool only: `check(target, error?)` with a 40-word description; no resources, no prompts. Listed in
the official registry after pages and plugins exist (plan §21: pages and plugins before MCP).

Shipped as `apifacts mcp` (`apifacts/mcp_server.py`, stdio) behind the extra `apifacts[mcp]`, so the
plugin's users do not pull the MCP SDK: `uvx --from 'apifacts[mcp]' apifacts mcp`. The error is passed
flat — `check(target, method?, status?, body?)` — because clients fill flat arguments more reliably
than a nested object; `body` may arrive as a JSON object (the SDK parses JSON strings) and is
re-serialized. Same client as the CLI (filters, 2 s timeout, 20 checks per session, `APIFACTS_DISABLE`,
`--offline` from the packaged snapshot); every failure is a text answer starting with `error:`.
`server.json` at the repository root is the registry entry (`io.github.Illouminus/apifacts`, PyPI,
`runtimeHint: uvx`); README.md carries the `mcp-name:` line the registry looks for on PyPI.

## CLI (wave 1, part of `apifacts`)

`apifacts check <url-or-locator> [--status N --body file]` for humans and shell agents; prints the
same section as the plugin.

## CI logs (`apifacts scan`, GitHub Action `action/`)

Agents that fix red CI read the failing step's log, the run's annotations and the job summary, not a
test report. `apifacts scan [FILE|-]` (`apifacts/cli_scan.py`, extractor `apifacts/client/logscan.py`)
reads the last 2 MB of a log, finds failed calls (status ≥ 400) in the formats clients print —
`requests` and `httpx` `raise_for_status()`, httpx's `HTTP Request:` log line (the OpenAI and Anthropic
SDKs, with their `Error code: N - {…}` as the body), stripe-python's logfmt log, `gh` (`HTTP 404: … (url)`),
axios with its `config` dump, ky, ofetch, `curl -f` with `-v` or the echoed command — and asks about each
distinct `(method, scrubbed URL, status)`, at most 10 (`--max-lookups`). Same filters and host gate as
the plugin: only hosts in `GET /v0/services` are sent, never a query string, a header or a request body
(axios `config.data` is never read). Our own "Known facts" sections and `title=apifacts` annotations in
the log are skipped. Exit 0 whatever happens (advisory); 2 only for an unreadable file.

**Method.** Many formats omit it, and the server refuses a path without one (spec 03); a guessed method
would be stored as an observation under the wrong template and count toward a quorum. So: a method the
log states (inline, `-X`/`-d` on a visible curl command, the axios dump, the stripe log) is used and the
error is reported as the plugin reports it. Otherwise, when the registry's templates (packaged snapshot or
`APIFACTS_SNAPSHOT`) give the path exactly one method, the call is a pre-flight — that method, no `error`
object, so nothing is stored (Q5) — and the facts are filtered by status on the client; with zero or
several candidate methods nothing is sent and the output names the `apifacts check … -X <METHOD>` command.

`--github` (default when `GITHUB_ACTIONS=true`): one `::warning title=apifacts: <target>::…` per call that
has a fact for its exact status (the service-wide rate-limit facts the cascade adds stay in the log only),
escaped like actions/toolkit (`%`, CR, LF; `:` and `,` in the title), and a markdown section appended to
`$GITHUB_STEP_SUMMARY` with the sections in a code fence (no server string becomes markdown). `--json`
prints the calls and answers instead of the plain sections.

The composite action (`uses: Illouminus/apifacts/action@v0`) takes `run` (a command run with
`bash -eo pipefail`, output tee'd, scanned only on failure, the step exits with the command's code) or
`log-file` (scan a file, always exit 0), `offline`, and `version` (default = the current release; a test
keeps it equal to `apifacts.__version__`). It starts `apifacts` with `uvx` when present, else `pipx run`,
preinstalled with Python ≥ 3.12 on ubuntu-, macos- and windows-latest; nothing in it can fail a step.
