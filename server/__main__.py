import uvicorn
from api import server_configs

port = server_configs["port"]

uvicorn.run("api:app", port=port)
