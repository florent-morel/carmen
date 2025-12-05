"""
Setup fixture file that can be shared across multiple tests.
"""

from collections.abc import Generator
import pytest
from starlette.testclient import TestClient

from backend.src.main import app


@pytest.fixture(scope="module")
def api_client() -> Generator:
    """
    Generates a test client for API testing.
    """
    with TestClient(app) as test_client:
        yield test_client
