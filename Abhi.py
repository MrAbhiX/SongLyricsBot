from pyrogram import Client, filters
from aiohttp import ClientSession
from Python_ARQ import ARQ
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


aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

@bot.on_message(filters.command("lyrics") & ~filters.edited)
async def lyrics_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    resp = await arq.lyrics(query)

    if not (resp.ok and resp.result):
        return await m.edit("No lyrics found.")

    song = resp.result[0]
    song_name = song['song']
    artist = song['artist']
    lyrics = song['lyrics']
    msg = f"**{song_name}** | **{artist}**\n\n__{lyrics}__"
          
    if len(msg) > 4095:
        msg = await paste(msg)
        msg = f"**LYRICS_TOO_LONG:** [URL]({msg})"
    return await m.edit(msg)

bot.start()
print("BOT STARTED SUCCESSFULLY")
