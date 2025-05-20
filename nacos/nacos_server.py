from nacos_mcp_wrapper.server.nacos_mcp import NacosMCP
from nacos_mcp_wrapper.server.nacos_settings import NacosSettings

# 代码方式
nacos_settings = NacosSettings()
# replace with your nacos server address
nacos_settings.SERVER_ADDR = "127.0.0.1:8848"
mcp = NacosMCP("nacos_mcp_server_python",nacos_settings=nacos_settings)

# 环境变量方式：配置环境变量 NACOS_MCP_SERVER_SERVER_ADDR=127.0.0.1:8848
mcp = NacosMCP("nacos_mcp_server_python")

@mcp.tool()
def get_weather(city_name:str) -> str:
    """Get weather information by city name"""
    return "Sunny"

mcp.run()