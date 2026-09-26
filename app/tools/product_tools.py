
from app.clients.product_clients import ProductClient


product_clients = ProductClient()

def register_product_tools(mcp):

    @mcp.tool()
    async def get_product(
        productId: int
    ):
        """
        Get product information for a specific productid
        """

        return await product_clients.get_Product(
            productId
        )