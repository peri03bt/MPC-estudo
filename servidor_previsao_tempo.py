import os
import dotenv
import requests
from fastmcp import FastMCP

dotenv.load_dotenv()

servidor_mcp = FastMCP("mcp-buscar-previsao-tempo")
api_key_weather = os.getenv("OPENWEATHER_API_KEY")

@servidor_mcp.tool()
async def buscar_tempo_atual(local: str) -> dict:
    """Busca a temperatura atual de uma cidade"""
    app_id = api_key_weather
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    response = requests.get(url, params=params)
    return response.json()

@servidor_mcp.tool()
async def buscar_previsao_atual(local: str) -> dict:
    """Busca a previsão do tempo para os próximos dias"""
    app_id = api_key_weather
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": local,
        "appid": app_id,
        "units": "metric",
        "lang": "pt_br"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    servidor_mcp.run(transport="stdio") 