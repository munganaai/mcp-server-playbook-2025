# Quickstart Guide to Building an MCP Server in Python

## Introduction
The Model Context Protocol (MCP) by Anthropic enables AI agents to interact with external tools, data sources, and services. This guide walks you through building an MCP server in Python using the official MCP Python SDK, integrating it with AI assistants, and deploying it for production use.

## 1. Overview of the MCP Python SDK

The MCP Python SDK provides tools to build MCP servers and clients, facilitating seamless integration between Large Language Models (LLMs) and external data sources or tools. This SDK adheres to the full MCP specification, ensuring compatibility and standardization. ([GitHub Repository](https://github.com/modelcontextprotocol/python-sdk))

## 2. Installation

To integrate MCP into your Python project, it's recommended to use `uv`, a Python package manager:

```bash
uv add "mcp[cli]"
```

Alternatively, if you're using `pip`:

```bash
pip install mcp
```

## 3. Quickstart: Building an MCP Server

Let's create a simple MCP server that offers a calculator tool and a personalized greeting resource:

```python
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Demo Server")

# Define an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

# Define a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Generates a personalized greeting."""
    return f"Hello, {name}!"

# Run the server
if __name__ == "__main__":
    mcp.run()
```

## 4. Testing the MCP Server

To test the server using the MCP Inspector:

```bash
mcp dev server.py
```

This command launches the MCP Inspector, allowing you to interact with and validate the server's functionalities.


## 6. Client Integration

6.1. **Example:** For integration with AI assistants like Claude Desktop:

```bash
mcp install server.py
```

This command installs the server into Claude Desktop, enabling seamless interaction between the assistant and the MCP server.

## 6. Deployment Considerations

When deploying your MCP server:

- **Security**: Implement authentication mechanisms, such as API keys or OAuth, to control access.
- **Scalability**: Utilize containerization tools like Docker to manage deployments across various environments.
- **Monitoring**: Set up logging and monitoring to track server performance and diagnose issues promptly.


