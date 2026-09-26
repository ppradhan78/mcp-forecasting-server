from mcp.server.fastmcp import FastMCP

from app.tools.weather_tools import register_weather_tools
from app.tools.order_tools import register_order_tools
from app.tools.product_tools import register_product_tools

from app.resources.business_resources import register_resources
from app.prompts.business_prompts import register_prompts




mcp = FastMCP("Enterprise TANDMS MCP Server")


def register_all_components():

    # Tools
    register_weather_tools(mcp)
    register_order_tools(mcp)
    register_product_tools(mcp)

    # Resources
    register_resources(mcp)

    # Prompts
    register_prompts(mcp)


register_all_components()


if __name__ == "__main__":
    mcp.run(transport="streamable-http")