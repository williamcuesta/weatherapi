from weatherapi.infrastructure.adapters.adapter import AdapterExternaSource


def test_adapter_external_source():

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

    assert AdapterExternaSource(**adapter_test)
