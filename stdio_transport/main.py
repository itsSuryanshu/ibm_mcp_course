from fastmcp import Client
from fastmcp.client.transports import StdioTransport
import asyncio

async def main():
    stdio_transport = StdioTransport(
        command="npx",
        args=["-y", "@upstash/context7-mcp"]
    )

    mcp_client = Client(transport=stdio_transport)

    async with mcp_client as client:
        tools = await client.list_tools()

    print(tools)

if __name__ == "__main__":
    asyncio.run(main())
