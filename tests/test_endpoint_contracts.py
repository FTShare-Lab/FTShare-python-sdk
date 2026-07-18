from __future__ import annotations

import importlib.util
import inspect
from pathlib import Path
from typing import Any

import pytest

from ftshare.client import FtshareClient
from ftshare.endpoints import ENDPOINTS

from conftest import FakeResponse, FakeSession
from endpoint_cases import SAMPLE_VALUES, SPECIAL_CALLS, WIRE_ALIASES


ROOT = Path(__file__).resolve().parents[2]
DOC_ROOT = ROOT / "ftshare-doc" / "api-doc"
AUDIT_SCRIPT = ROOT / ".claude" / "skills" / "ftshare-doc-to-sdk-skills" / "scripts" / "audit_sync.py"
SDK_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "FTShare-skills" / "ftshare-market-data"


def _load_audit_module():
    spec = importlib.util.spec_from_file_location("ftshare_audit_sync", AUDIT_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


AUDIT = _load_audit_module()


def _public_contracts() -> dict[str, dict[str, Any]]:
    contracts: dict[str, dict[str, Any]] = {}
    for doc in sorted(DOC_ROOT.rglob("*.md")):
        relative = doc.relative_to(DOC_ROOT)
        if doc.name == "接口异常排查清单.md" or "未发布" in relative.parts:
            continue
        report = AUDIT.build_report(SDK_ROOT, SKILLS_ROOT, doc, require_skill=False)
        assert report["sdk"]["matches"], relative
        for match in report["sdk"]["matches"]:
            contracts[match["name"]] = {"document": report["document"], "endpoint": match}
    return contracts


PUBLIC_CONTRACTS = _public_contracts()
CONTROL_PARAMS = {"page", "page_size"}


def _call_kwargs(name: str) -> dict[str, Any]:
    if name in SPECIAL_CALLS:
        return dict(SPECIAL_CALLS[name])
    endpoint = ENDPOINTS[name]
    return {
        param.replace("-", "_"): SAMPLE_VALUES[param]
        for param in endpoint.params
    }


def _wire_params(name: str, kwargs: dict[str, Any]) -> dict[str, Any]:
    endpoint = ENDPOINTS[name]
    result = {}
    for param in endpoint.params:
        python_name = param.replace("-", "_")
        value = kwargs.get(python_name)
        if value is None or param in endpoint.path_params:
            continue
        result[WIRE_ALIASES.get(name, {}).get(python_name, param)] = value
    return result


def _response_payload(name: str) -> Any:
    endpoint = ENDPOINTS[name]
    if "page" in endpoint.params and "page_size" in endpoint.params:
        return {"items": [], "total_pages": 0, "total_items": 0}
    return []


def test_all_published_documents_have_sdk_contracts():
    reports = AUDIT.audit_directory(SDK_ROOT, SKILLS_ROOT, DOC_ROOT)
    assert reports["summary"]["public_documents"] == 184
    assert reports["summary"]["sdk_matches"] == 184
    assert reports["issues"] == []


def test_contract_cases_cover_all_published_sdk_methods():
    assert len(PUBLIC_CONTRACTS) == 197
    assert set(PUBLIC_CONTRACTS) <= set(ENDPOINTS)


@pytest.mark.parametrize("method_name", sorted(PUBLIC_CONTRACTS))
def test_endpoint_forwards_every_documented_parameter(method_name):
    endpoint = ENDPOINTS[method_name]
    method = getattr(FtshareClient, method_name)
    signature = inspect.signature(method)
    kwargs = _call_kwargs(method_name)

    for param in endpoint.params:
        python_name = param.replace("-", "_")
        if python_name not in signature.parameters:
            assert any(p.kind == inspect.Parameter.VAR_KEYWORD for p in signature.parameters.values())
        assert python_name in kwargs

    session = FakeSession([FakeResponse(payload=_response_payload(method_name))])
    client = FtshareClient(session=session)
    getattr(client, method_name)(as_dataframe=False, **kwargs)

    call = session.calls[0]
    expected_path = endpoint.path
    for path_param in endpoint.path_params:
        expected_path = expected_path.replace("{" + path_param + "}", str(kwargs[path_param]))
    assert call["url"] == client.base_url + expected_path
    assert call["method"] == endpoint.method

    expected_wire = _wire_params(method_name, kwargs)
    if endpoint.method == "POST":
        assert call["json"] == expected_wire
        assert "params" not in call
    else:
        expected_query = {
            key: str(value).lower() if isinstance(value, bool) else value
            for key, value in expected_wire.items()
        }
        assert call["params"] == expected_query
        assert "json" not in call


@pytest.mark.parametrize("method_name", sorted(PUBLIC_CONTRACTS))
def test_endpoint_case_covers_complete_metadata_parameter_set(method_name):
    endpoint = ENDPOINTS[method_name]
    kwargs = _call_kwargs(method_name)
    expected_python_params = {param.replace("-", "_") for param in endpoint.params}
    assert set(kwargs) == expected_python_params


def test_sample_values_cover_every_public_endpoint_parameter():
    public_params = {
        param
        for name in PUBLIC_CONTRACTS
        for param in ENDPOINTS[name].params
    }
    special_params = {
        param
        for name in SPECIAL_CALLS
        if name in PUBLIC_CONTRACTS
        for param in ENDPOINTS[name].params
    }
    assert public_params - special_params <= set(SAMPLE_VALUES)
