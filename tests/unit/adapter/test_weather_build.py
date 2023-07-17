from weatherapi.infrastructure.adapters.adapter import AdapterExternaSource
from weatherapi.infrastructure.adapters.builder import WeatherBuilder
from weatherapi.models.weather_model import WeatherResponseModel


def test_weather_builder():
    adapter_test = {
        "coord": {"lat": 100, "lon": 200},
        "weather": [{"description": "rain", "icon": "10n"}],
        "base": "example.com",
        "main": {"pressure": 12, "humidity": 0.5, "temp": 200},
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
    adapter = AdapterExternaSource(**adapter_test)
    response_model = WeatherBuilder.build(adapter)
    assert isinstance(response_model, WeatherResponseModel)
