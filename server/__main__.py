import uvicorn
from configs import server_configs

port = server_configs["port"]

uvicorn.run("api:app", port=port)
