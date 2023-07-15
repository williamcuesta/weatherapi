from typing import Union

import json
from datetime import datetime

from weatherapi.infrastructure.adapters.adapter import AdapterExternaSource
from weatherapi.models.weather_model import WeatherResponseModel


class WeatherBuilder:
    @classmethod
    def build(
        cls, data_adapter: AdapterExternaSource
    ) -> Union[WeatherResponseModel, None]:
        a_name = data_adapter.name
        a_country = data_adapter.sys['country'].lower()
        location = f"{a_name}, {a_country}"
        lat = data_adapter.coord['lat']
        lon = data_adapter.coord['lon']
        coordinates = f"[{lat}, {lon}]"
        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        adapter_data = {
            "location_name": location,
            "temperature": cls.temperature_format(data_adapter.main["temp"]),
            "wind": json.dumps(data_adapter.wind),
            "cloudiness": data_adapter.weather[0]["description"],
            "pressure": data_adapter.main["pressure"],
            "humidity": data_adapter.main["humidity"],
            "sunrise": data_adapter.sys["sunrise"],
            "sunset": data_adapter.sys["sunset"],
            "geo_coordinates": coordinates,
            "requested_time": formatted_time,
            "forecast": data_adapter.main,
        }
        return WeatherResponseModel(**adapter_data)

    @staticmethod
    def temperature_format(temperature_k: float) -> str:
        """
        Temperature format

        Parameters
        ----------
        temperature : float
            Data of temperature from external API

        Returns
        -------
        str
            The corresponding temperature format
        """
        temperature_c = temperature_k - 273.15
        temperature_f = temperature_c * 9 / 5 + 32
        return f"{temperature_c:.2f} °C, {temperature_f:.2f} °F"
