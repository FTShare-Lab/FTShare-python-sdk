from __future__ import annotations


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text="{}", json_error=False, content=b"", headers=None, chunks=None):
        self.status_code = status_code
        self._payload = payload
        self.text = text
        self._json_error = json_error
        self.content = content
        self.headers = headers or {}
        self._chunks = chunks

    def json(self):
        if self._json_error:
            raise ValueError("not json")
        return self._payload

    def iter_content(self, chunk_size=1):
        if self._chunks is not None:
            yield from self._chunks
            return
        for start in range(0, len(self.content), chunk_size):
            yield self.content[start : start + chunk_size]

    def close(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        self.close()
        return False


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, params=None, timeout=None, headers=None, stream=False):
        self.calls.append(
            {
                "method": "GET",
                "url": url,
                "params": params,
                "timeout": timeout,
                "headers": headers,
                "stream": stream,
            }
        )
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response

    def post(self, url, json=None, timeout=None, headers=None):
        self.calls.append(
            {"method": "POST", "url": url, "json": json, "timeout": timeout, "headers": headers}
        )
        return self.responses.pop(0)
