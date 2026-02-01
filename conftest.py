import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://en.wikipedia.org/w/api.php"


@pytest.fixture(scope="session")
def default_headers():
    return {
        "User-Agent": "pytest-wikipedia-api/1.0 (QA testing project)"
    }


@pytest.fixture
def default_params():
    return {
        "action": "query",
        "format": "json"
    }


@pytest.fixture
def api_get(base_url, default_headers):
    def _get(params: dict):
        return requests.get(
            base_url,
            params=params,
            headers=default_headers,
            timeout=10
        )
    return _get
