from clients.weather_clients import WeatherClient


weather_client = WeatherClient()


def register_resources(mcp):

    @mcp.resource(
        "weather://{city}/{country_code}"
    )
    async def weather_resource(
        city: str,
        country_code: str
    ) -> dict:
        """
        Weather resource for retrieving current weather information.
        """

        return await weather_client.get_weather(
            city=city.strip(),
            country_code=country_code.strip().upper()
        )