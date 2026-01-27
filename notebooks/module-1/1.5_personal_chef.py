from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from tavily import TavilyClient
from typing import Any

load_dotenv()

tavily_client = TavilyClient()


@tool
def web_search(query: str) -> dict[str, Any]:
    """Search the web for information"""
    return tavily_client.search(query)


SYSTEM_PROMPT = """
You are a personal chef. The user will give you a list of ingredients they have left over in their house.

Using the web search tool, search the web for recipes that can be made with the ingredients they have.

Return recipe suggestions and eventually the recipe instructions to the user, if requested.
"""


model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
agent = create_agent(model=model, tools=[web_search], system_prompt=SYSTEM_PROMPT)
