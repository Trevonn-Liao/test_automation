import pytest

from api.http_client import ApiClient
from config.settings import get_base_url


@pytest.fixture
def api_client() -> ApiClient:
    return ApiClient(get_base_url())
