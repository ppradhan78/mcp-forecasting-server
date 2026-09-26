import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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