import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_openai.chat_models import ChatOpenAI

load_dotenv() # current dir
load_dotenv("../.env") # parent dir

CONTEXT7_API_KEY = os.getenv("CONTEXT7_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

async def main():
    client = MultiServerMCPClient(
        {
            "context7": {
                "url": "https://mcp.context7.com/mcp",
                "transport": "streamable_http",
                "headers": {
                    "CONTEXT7_API_KEY": CONTEXT7_API_KEY,
                }
            },
            "met-museum": {
                "command": "npx",
                "args": ["-y", "metmuseum-mcp"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()
    print(tools)




if __name__ == "__main__":
    asyncio.run(main())