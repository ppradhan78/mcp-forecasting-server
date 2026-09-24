import logging

import httpx

from config.settings import NorthWindConfig


logger = logging.getLogger(__name__)


class ProductClient:

    def __init__(self):
        self.api_url = (
            f"{NorthWindConfig.BASE_API_URL.rstrip('/')}/Products/"
        )

    async def get_Product(
        self,
        productId: int,
    ) -> dict:

        params = {
            "q": f"{productId},{productId}"
        }

        logger.info(
            "Fetching product by productId %s",
            productId
        )

        async with httpx.AsyncClient(timeout=10.0) as client:

            response = await client.get(
                self.api_url,
                params=params
            )

            logger.info(
                "Northwind product API response status: %s",
                response.status_code
            )

            response.raise_for_status()

            return response.json()