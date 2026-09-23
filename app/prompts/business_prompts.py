def register_prompts(mcp):

    @mcp.prompt()
    def weather_summary(
        city: str,
        country_code: str
    ):
        """
        Create a prompt for summarizing weather information.
        """

        return (
            f"Retrieve the current weather for {city}, {country_code} "
            f"and provide a concise summary including "
            f"temperature, feels-like temperature, weather condition, "
            f"humidity, wind speed, and location."
        )