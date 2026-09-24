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

    @mcp.prompt()
    def order_summary(
        orderId: int
    ):
        """
        Create a prompt for summarizing order information.
        """

        return (
            f"Retrieve the order for {orderId} "
            f"and provide a concise summary including "
            f"Order details customer details ,shipper details"
        )

    @mcp.prompt()
    def order_Product(
        productId: int
    ):
        """
        Create a prompt for summarizing product information.
        """

        return (
            f"Retrieve the product for {productId} "
            f"and provide a concise summary including "
            f"Order details product details ,supplyer details"
        )