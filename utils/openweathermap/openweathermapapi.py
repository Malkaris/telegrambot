import asyncio

from aiohttp import ClientSession

from utils.openweathermap.response_schemas import WeatherResponse


class OpenWeatherMapAPI(object):
    BASE_URL: str = 'https://api.openweathermap.org/'

    def __init__(self, access_token: str) -> None:
        # assert isinstance(access_token, str)
        if not isinstance(access_token, str):
            raise TypeError('attribute access_token must be str')
        self.__access_token: str = access_token
        self.Session: ClientSession = ClientSession(
            base_url=OpenWeatherMapAPI.BASE_URL
        )

    async def get_current_weather(self, params: dict) -> WeatherResponse:
        params['appid'] = self.__access_token
        async with self.Session as session:
            response = await session.get(
                url='/data/2.5/weather',
                params=params
            )
        return WeatherResponse(**(await response.json()))


async def main():
    params = {
        'lon': 27.530510,
        'lat': 53.911838,
        'unit': 'metric',
        'lang': 'ru'

    }

    weather = OpenWeatherMapAPI(access_token='')
    print(await weather.get_current_weather(params=params))


if __name__ == '__main__':
    asyncio.run(main())
