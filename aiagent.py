import asyncio
import os
from openai import OpenAI
from openai.types.beta import Assistant
from openai.types.beta.threads import Run
from dotenv import load_dotenv
from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer, MCPServerStdio

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def interactive_chat(mcp_server: MCPServer):
    agent = Agent(
        name="Assistant",
        instructions="""
        You are a helpful assistant that can manage notes and answer general questions.
        - Use the SimpleNotes tools when the user wants to create, view, or manage notes.
        - For any other questions, respond using your general knowledge.
        - Be concise and helpful in your responses.
        """,
        mcp_servers=[mcp_server],
        model="gpt-4o-mini"  # Use GPT-4o-mini for general knowledge questions
    )

    print("Welcome to SimpleNotes Assistant!")
    print("You can manage notes or ask general questions.")
    print("Type 'quit' to exit.\n")

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if user_input.lower() == "quit":
                print("Goodbye!")
                break
            print("Assistant is thinking...", flush=True)
            result = await Runner.run(starting_agent=agent, input=user_input)
            print(f"\nAssistant: {result.final_output}")
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

async def main():
    cmd = "/opt/homebrew/bin/uv"
    async with MCPServerStdio(
        name="SimpleNotes Server",
        params={
            "command": cmd,
            "args": [
                "run", "--with", "mcp[cli]", "mcp", "run",
                "/Users/reubencleetus/code/python/MCP/simpleserver/simplenote.py"
            ],
        },
    ) as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="MCP SimpleNotes Interactive Chat", trace_id=trace_id):
            print(f"View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}\n")
            await interactive_chat(server)


if __name__ == "__main__":
    asyncio.run(main())