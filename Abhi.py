from pyrogram import Client, filters

from urllib.request import urlopen as u_reqs, Request
from bs4 import BeautifulSoup as Soup
from pyrogram.types import Message
import os
import asyncio

bot = Client(
    "Song Lyrics Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)




