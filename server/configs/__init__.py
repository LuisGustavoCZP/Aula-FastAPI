from os import getenv
import dotenv

dotenv.load_dotenv()

server_configs = {
    "port": int(getenv('PORT')),
}