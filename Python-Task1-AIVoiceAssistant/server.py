from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("Jarvis")


@mcp.tool
def get_current_time():
    """Get the current system time."""
    return datetime.now().strftime("%I:%M:%S %p")


@mcp.tool
def get_current_date():
    """Get today's date."""
    return datetime.now().strftime("%d %B %Y")


@mcp.tool
def add_numbers(a: int, b: int):
    """Add two numbers."""
    return a + b


@mcp.tool
def greet(name: str):
    """Greets the user."""
    return f"Hello {name}! I'm Jarvis."


if __name__ == "__main__":
    print("🚀 Jarvis MCP Server Started")
    mcp.run(transport="stdio")