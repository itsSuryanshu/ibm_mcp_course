import asyncio
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async def main():
    http_transport = StreamableHttpTransport(
        url="https://mcp.context7.com/mcp"
    )
    http_client = Client(transport=http_transport)
    async with http_client as client:
        tools = await client.list_tools()
    
    print(tools)

if __name__ == "__main__":
    asyncio.run(main())