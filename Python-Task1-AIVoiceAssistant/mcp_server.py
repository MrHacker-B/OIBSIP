from livekit.agents.llm.mcp import MCPServerStdio


def create_mcp_server():

    return MCPServerStdio(
        command="python",
        args=["server.py"]
    )
