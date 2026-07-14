import os
import asyncio
from dotenv import load_dotenv

from livekit.agents import Agent, AgentSession
from livekit.plugins import google
from mcp_server import create_mcp_server
load_dotenv()


async def main():

    print("=" * 40)
    print("🤖 JARVIS")
    print("=" * 40)

    agent = Agent(
        instructions="""
        You are Jarvis.
        You are polite, intelligent and helpful.
        Answer briefly and clearly.
        """
    )

    mcp_server = create_mcp_server()
    session = AgentSession(
        llm=google.LLM(
            model="gemini-2.5-flash",
            api_key=os.getenv("GEMINI_API_KEY")
        ),
        mcp_server=mcp_server
    )


    await session.start(agent)


    while True:

        question = input("\nYou : ")

        if question.lower() in ["exit", "quit"]:

            print("Jarvis : Goodbye!")
            break


        response = await session.generate_reply(
            instructions=question
        )


        print("\nJarvis :", response)



if __name__ == "__main__":
    asyncio.run(main())