import requests
from requests import Response


class ApiClient:
    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get(self, path: str) -> Response:
        return self.request("GET", path)

    def request(self, method: str, path: str, **kwargs) -> Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        try:
            return requests.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs,
            )
        except requests.RequestException as error:
            raise AssertionError(
                f"Could not connect to {url}. Is the Go service running?"
            ) from error
