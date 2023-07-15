from weatherapi.infrastructure.adapters.http_adapter import request_http_get
from weatherapi.infrastructure.adapters.adapter import AdapterExternaSource

from weatherapi.settings import APP


class WeatherService:
    headers = {"content-type": "application/json"}

    @classmethod
    async def get_data(cls, with_information: dict) -> AdapterExternaSource:
        """Get data from external source"""
        url_one = f'{APP.URL}?q={with_information["city"]}'
        url_two = f'{with_information["country"]}&{APP.APPID}'
        url = f'{url_one},{url_two}'

        cls.headers = {"content-type": "application/json"}

        response_request = await request_http_get(url, headers=cls.headers)
        adapter_externa_source = AdapterExternaSource(**response_request)
        return adapter_externa_source
