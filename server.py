# server.py
from mcp.server.fastmcp import FastMCP
import requests

# Create an MCP server
mcp = FastMCP("Demo")

# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.tool()
def save_log_customer(callback_date: str, phone: str, status: str) -> str:
    """This tool is for recording the date, status, and phone number of customers. Use this tool whenever customer want staff to follow up later or not.

    Args:
        callback_date: The date the customer scheduled an appointment or the date of the most recent call with the customer (day-month-year)
        phone: Customer's phone number
        status: Status of all types of insurance products that the customer is interested in (ติดต่อกลับ/ไม่สนใจ)
    """

    import requests
    print("\nsave_log_customer\n")

    url = "http://3.1.190.223:8000/tool/save_log"  # Replace with your target URL
    payload = {"callback_date": callback_date, "phone": phone, "status": status}     # Replace "gpt-4" with the actual model string
    print(payload)
    for key, value in payload.items():
        if value == "":
            return f"Please provide the '{key}' parameter."
    response = requests.get(url, params=payload)