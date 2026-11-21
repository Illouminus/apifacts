# Contributing to apifacts

## The contribution ladder

From most to least automatic:

1. **Our probes** run on a schedule and are the only thing that changes a fact's status.
2. **Calling `check()` is contributing.** Every request whose target matches a registered template is
   stored as a normalized observation; observations that reach quorum become `reported` facts and
   schedule a probe. There is no separate "submit" step.
3. **Test plugins** (pytest first, jest later): a failing test becomes a ready-made observation.
4. **Pull requests** — for humans and API producers. Producer signatures are always free.

## Development setup

Requires [uv](https://docs.astral.sh/uv/). Python 3.12 is installed by uv if missing.

```bash
uv sync
uv run ruff check .
uv run pytest -q
uv run apifacts validate
uv run apifacts pages build --check   # pages/ must match services/ + facts/
(cd plugins/pytest && uv sync && uv run pytest -q)   # the pytest plugin's own tests
```

All of them must be green before you push. CI (`.github/workflows/ci.yml`) runs the same commands on
every pull request.

## Rules for a fact pull request

- **One fact per file:** `facts/<service>/<slug>.yaml`, id `af:<service>:<slug>`, schema in
  [`docs/specs/01-fact-schema.md`](docs/specs/01-fact-schema.md).
- **The service must be registered** in `services/<service>.yaml`, and the fact's `path_template` must
  be one of its templates.
- **Fixes are typed only:** members of the closed vocabulary in
  [`docs/specs/02-fix-vocabulary.md`](docs/specs/02-fix-vocabulary.md). No free text, no shell commands,
  no URLs outside the vendor's registered hosts. If no client-side fix is known, use `none_known`.
- **Claims are one declarative sentence** (≤ 300 characters), no advice.
- **Evidence is required:** a probe in `probes/<service>/` that reproduces the signal, or an official
  vendor doc URL for status `official`. A fact that cannot be reproduced by running code stays
  `reported`.
- **Probes against production are read-only** (`GET`/`HEAD`); anything that creates objects runs in
  `env: sandbox`.
- Never put keys, tokens, request bodies or personal data in any file.

## Out of scope

Facts about the world, prices, opinions, stateful or paid endpoints, behaviour behind someone else's
authorization, and services whose terms forbid automated access or publishing measurements.

## Licenses

By contributing you agree that code is licensed under [MIT](LICENSE) and facts and fact pages under
[CC BY 4.0](LICENSE-DATA).
