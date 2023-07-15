from pydantic import BaseModel, validator
import datetime


class CountryModel(BaseModel):
    country: str

    @validator("country")
    def validate_value(cls, value):
        if len(value.encode("utf-8")) > 2:
            raise ValueError("El valor debe tener máximo 2 bytes")
        if any(char.isdigit() for char in value):
            raise ValueError("El valor no puede contener números")
        return value.lower()


class CityModel(BaseModel):
    city: str

    @validator("city")
    def validate_value(cls, value):
        if len(value.encode("utf-8")) > 20:
            raise ValueError("El valor debe tener máximo 20 bytes")
        if any(char.isdigit() for char in value):
            raise ValueError("El valor no puede contener números")
        return value.lower()


class WeatherResponseModel(BaseModel):
    pass
    location_name: str
    temperature: str
    wind: str
    cloudiness: str
    pressure: str
    humidity: str
    sunrise: str
    sunset: str
    geo_coordinates: str
    requested_time: datetime.datetime
    forecast: dict
