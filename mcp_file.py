import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool()
def get_my_files():
    return os.listdir(os.path.expanduser("/Users/advance/IdeaProjects"))


if __name__ == "__main__":
    mcp.run(transport='stdio')