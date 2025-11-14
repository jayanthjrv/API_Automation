import httpx
import pytest


@pytest.fixture
def client(api_base_url):
    with httpx.Client(base_url=api_base_url) as client:
        yield client
