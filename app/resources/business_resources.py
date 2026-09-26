from app.clients.weather_clients import WeatherClient
from app.clients.order_clients import OrderClient
from app.clients.product_clients import ProductClient




weather_client = WeatherClient()
order_clients = OrderClient()
product_clients = ProductClient()


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

    @mcp.resource(
        "order://{orderId}"
    )
    async def order_resource(
            orderId: int
    ) -> dict:
        """
        Order  retrieving for current orderid.
        """
        return await order_clients.get_order(orderId)


    @mcp.resource(
        "product://{productId}"
    )
    async def order_resource(
            productId: int
    ) -> dict:
        """
        Order  retrieving for current orderid.
        """
        return await product_clients.get_Product(productId)


