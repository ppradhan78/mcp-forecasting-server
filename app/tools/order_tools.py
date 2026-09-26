
from app.clients.order_clients import OrderClient


order_clients = OrderClient()

def register_order_tools(mcp):

    @mcp.tool()
    async def get_order(
        orderId: int
    ):
        """
        Get order information for a orderid.
        """

        return await order_clients.get_order(
            orderId
        )