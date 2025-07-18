import asyncio
from pathlib import Path

from fastmcp import Client

# caminho_servidor = Path(__file__).parent / "servidor.py"
caminho_servidor = "http://127.0.0.1:8000/sse/"
cliente = Client(caminho_servidor)

async def testar_servidor(cliente, nome_usuario: str, id_usuario: int):
    async with cliente:
        args = {"nome": nome_usuario, "id": id_usuario}
        response = await cliente.call_tool("saudacao", arguments=args)
        print("Resposta obtida pelo servidor MCP: ", response)

if __name__ == "__main__":
    asyncio.run(testar_servidor(
        cliente, 
        nome_usuario="João", 
        id_usuario=123)
    )