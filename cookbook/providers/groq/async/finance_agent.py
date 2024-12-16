"""Run `pip install yfinance` to install dependencies."""

import asyncio
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stocks and helps users make informed decisions.",
    instructions=["Use tables to display data where possible."],
    markdown=True,
)

# asyncio.run(agent.aprint_response("Share the NVDA stock price and analyst recommendations", stream=True))
asyncio.run(agent.aprint_response("Summarize fundamentals for TSLA", stream=True))