from __future__ import annotations


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text="{}", json_error=False):
        self.status_code = status_code
        self._payload = payload
        self.text = text
        self._json_error = json_error

    def json(self):
        if self._json_error:
            raise ValueError("not json")
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, params=None, timeout=None, headers=None):
        self.calls.append(
            {"method": "GET", "url": url, "params": params, "timeout": timeout, "headers": headers}
        )
        return self.responses.pop(0)

    def post(self, url, json=None, timeout=None, headers=None):
        self.calls.append(
            {"method": "POST", "url": url, "json": json, "timeout": timeout, "headers": headers}
        )
        return self.responses.pop(0)
