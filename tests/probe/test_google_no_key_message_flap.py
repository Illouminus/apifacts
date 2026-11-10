"""The keyless Google probes hold their claim (403 PERMISSION_DENIED) under both texts.

Night window 2026-11-09/10 (gemini) and 2026-11-10 12:45Z (sheets): a keyless request answered
"Permission denied on the service." instead of "Method doesn't allow unregistered callers";
an assert on the message turned three such runs into a stale fact (agent-facts#134).
"""

import json
from pathlib import Path

import httpx
import pytest

from apifacts.probe.assertions import evaluate
from apifacts.probe.http import StepResponse
from apifacts.schema.models import Probe
from apifacts.schema.yamlio import load_yaml, plain

ROOT = Path(__file__).resolve().parents[2]
PROBES = [
    ROOT / "probes/google-gemini/models-no-key.yaml",
    ROOT / "probes/google-sheets/no-api-key.yaml",  # same flap 2026-11-10 12:45Z
]

DAY = (
    "Method doesn't allow unregistered callers (callers without established identity). "
    "Please use API Key or other form of API consumer identity to call this API."
)
NIGHT = "Permission denied on the service."


def _response(status: int, error_status: str, message: str) -> StepResponse:
    body = {"error": {"code": status, "message": message, "status": error_status}}
    return StepResponse(
        status=status,
        headers=httpx.Headers({"content-type": "application/json"}),
        body=json.dumps(body).encode(),
        json=body,
        latency_ms=100,
        error=None,
    )


def _outcome(path: Path, resp: StepResponse) -> bool:
    probe = Probe.model_validate(plain(load_yaml(path)))
    return all(evaluate(a, {1: resp}).ok for a in probe.assertions)


@pytest.mark.parametrize("path", PROBES, ids=lambda p: p.parent.name)
@pytest.mark.parametrize("message", [DAY, NIGHT])
def test_both_texts_pass(path, message):
    assert _outcome(path, _response(403, "PERMISSION_DENIED", message))


@pytest.mark.parametrize("path", PROBES, ids=lambda p: p.parent.name)
@pytest.mark.parametrize(
    ("status", "error_status"),
    [(401, "UNAUTHENTICATED"), (403, "UNAUTHENTICATED"), (400, "PERMISSION_DENIED")],
)
def test_claim_still_guarded(path, status, error_status):
    assert not _outcome(path, _response(status, error_status, NIGHT))
