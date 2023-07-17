import pytest

from weatherapi.infrastructure.adapters.adapter import AdapterExternaSource
from weatherapi.infrastructure.adapters.remote_endpoint import WeatherService
from weatherapi.models.weather_model import CountryModel, CityModel


MODULE_PATH = "weatherapi.infrastructure.adapters.remote_endpoint"


@pytest.mark.asyncio
async def test_weather_service(mocker):
    adapter_test = {
        "coord": {"foo": "bar"},
        "weather": [{"main": {"temp": 100, "feels_like": 20}}],
        "base": "example.com",
        "main": {"temp": 100, "feels_like": 20},
        "visibility": 20,
        "wind": {"speed": 10, "deg": 20},
        "clouds": {"clouds": 100},
        "dt": 12,
        "sys": {"country": "US", "sunrise": 12, "sunset": 1},
        "timezone": 123445,
        "id": 23,
        "name": "hello",
        "cod": 12,
    }
    mocker.patch(f"{MODULE_PATH}.request_http_get", return_value=adapter_test)

    city: CityModel = "Bogota"
    country: CountryModel = "co"
    with_information = {
        "city": city,
        "country": country,
    }
    response = await WeatherService.get_data(with_information)

    assert isinstance(response, AdapterExternaSource)
    assert response.cod == 12
    assert response.base == "example.com"
    assert response.clouds == {'clouds': 100}
