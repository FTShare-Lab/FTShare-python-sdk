from __future__ import annotations

import inspect
from typing import Any

import pytest

from ftshare.client import FtshareClient
from ftshare.endpoints import ENDPOINTS

from conftest import FakeResponse, FakeSession
from endpoint_cases import SAMPLE_VALUES, SPECIAL_CALLS, WIRE_ALIASES


NON_PUBLISHED_ENDPOINTS = {
    "stock_dividends_paginated",
    "stock_intraday",
    "stock_ohlcs",
    "stock_related",
}
PUBLIC_CONTRACTS = set(ENDPOINTS) - NON_PUBLISHED_ENDPOINTS
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


def test_contract_cases_cover_all_public_sdk_methods():
    assert len(PUBLIC_CONTRACTS) == 197
    assert PUBLIC_CONTRACTS | NON_PUBLISHED_ENDPOINTS == set(ENDPOINTS)
    assert not (PUBLIC_CONTRACTS & NON_PUBLISHED_ENDPOINTS)


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
