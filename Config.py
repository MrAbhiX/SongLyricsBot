from dotenv import load_dotenv
from os import path, getenv, mkdir


if path.exists("local.env"):
    load_dotenv("local.env")
else:
    load_dotenv()

if not path.exists("search"):
    mkdir("search")
    
    
class Configs:
    API_ID = int(getenv("API_ID", "0"))
    API_HASH = getenv("API_HASH", "abc123")
    BOT_TOKEN = getenv("BOT_TOKEN", "123:abc")
    OWNER_ID = int(getenv("OWNER_ID", "5289852546"))    
    CHANNEL_LINK = getenv("CHANNEL_LINK", "https://t.me/vexera_updates")
    GROUP_LINK = getenv("GROUP_LINK", "https://t.me/Heaven_of_friends")

    
config = Configs()
