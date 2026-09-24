import logging

import httpx

from config.settings import NorthWindConfig


logger = logging.getLogger(__name__)


class OrderClient:

    def __init__(self):
        self.api_url = (
            f"{NorthWindConfig.BASE_API_URL.rstrip('/')}/Orders/"
        )

    async def get_order(
        self,
        orderId: int,
    ) -> dict:

        params = {
            "q": f"{orderId},{orderId}"
        }

        logger.info(
            "Fetching order by orderId %s",
            orderId
        )

        async with httpx.AsyncClient(timeout=10.0) as client:

            response = await client.get(
                self.api_url,
                params=params
            )

            logger.info(
                "Northwind Order API response status: %s",
                response.status_code
            )

            response.raise_for_status()

            return response.json()