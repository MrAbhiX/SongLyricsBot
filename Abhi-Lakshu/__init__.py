from pyrogram import Client
from .Config import Configs


config = Configs()

Bot = Client(
    ":SongLyricsBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
  )



