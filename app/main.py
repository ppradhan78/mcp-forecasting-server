from mcp.server.fastmcp import FastMCP

from tools.weather_tools import register_weather_tools
from tools.order_tools import register_order_tools
from tools.product_tools import register_product_tools

from resources.business_resources import register_resources
from prompts.business_prompts import register_prompts


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