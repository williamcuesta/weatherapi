from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends

from weatherapi.infrastructure.adapters.remote_endpoint import WeatherService
from weatherapi.models.weather_model import CountryModel, CityModel
from weatherapi.infrastructure.adapters.builder import WeatherBuilder
from fastapi_cache.decorator import cache
from weatherapi.settings import APP
router = APIRouter()


@router.get("/weather/")
@cache(namespace="temporal_cache", expire=APP.TTL)
async def get_weather(
    city: str = Depends(CityModel), country: str = Depends(CountryModel)
):
    weather_response = await WeatherService.get_data(
        with_information={"city": city.city, "country": country.country}
    )
    response = WeatherBuilder.build(weather_response)
    json_compatible_item_data = jsonable_encoder(response)

    return JSONResponse(content=json_compatible_item_data)
