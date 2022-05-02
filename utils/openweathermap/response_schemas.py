from pydantic import BaseModel, Field


class Coord(BaseModel):
    lon: float = Field(ge=-180, le=180)
    lat: float = Field(ge=-180, le=180)


class Weather(BaseModel):
    id: int = Field(ge=0)
    main: str
    description: str
    icon: str


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int


class Wind(BaseModel):
    speed: float
    deg: int
    gust: float | None


class Clouds(BaseModel):
    all: int


class Sys(BaseModel):
    type: int
    id: int
    message: float
    country: str
    sunrise: int
    sunset: int


class WeatherResponse(BaseModel):
    coord: Coord
    weather: Weather
    base: str
    main: Main
    visibility: int = Field(le=1000)
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
