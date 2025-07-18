from fastmcp import FastMCP

servidor_mcp = FastMCP("mcp-test-server")

@servidor_mcp.tool()
async def saudacao(nome: str, id: int) -> str:
    return f"Olá, {nome}! Seu ID é {id}."


if __name__ == "__main__":
    # servidor_mcp.run(transport="stdio")
    servidor_mcp.run(transport="sse") # para executar o servidor em modo SSE