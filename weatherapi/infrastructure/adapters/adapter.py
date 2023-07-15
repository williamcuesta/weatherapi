from pydantic import BaseModel


class AdapterExternaSource(BaseModel):
    coord: dict
    weather: list[dict]
    base: str
    main: dict
    visibility: int
    wind: dict
    clouds: dict
    dt: int
    sys: dict
    timezone: int
    id: int
    name: str
    cod: int
