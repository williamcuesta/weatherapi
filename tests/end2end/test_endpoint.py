from fastapi.testclient import TestClient
from weatherapi.app import app
import pytest
from pydantic.error_wrappers import ValidationError

from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from typing import Any, Generator


@pytest.fixture(autouse=True)
def _init_cache() -> Generator[Any, Any, None]:
    FastAPICache.init(InMemoryBackend())
    yield
    FastAPICache.reset()


client = TestClient(app)


def test_get_weather(_init_cache):
    response = client.get("/weather?city=Bogota&country=CO")
    print(response.json())
    assert response.status_code == 200
    assert "temperature" in response.json()
    assert "Bogota, co" in response.json()["location_name"]


def test_bad_country():
    with pytest.raises(ValidationError):
        client.get("/weather?city=London&country=U1")


def test_bad_city():
    msg = "1 validation error for CityModel"
    with pytest.raises(ValidationError, match=msg):
        client.get("/weather?city=Bogot4&country=CO")
