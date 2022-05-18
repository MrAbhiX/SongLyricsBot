from pyrogram import Client, filters, idle
from aiohttp import ClientSession as session
from Python_ARQ import ARQ
from urllib.request import urlopen as u_reqs, Request
from bs4 import BeautifulSoup as Soup
from pyrogram.types import Message
import os
import asyncio
from asyncio import get_event_loop

bot = Client(
    "Song Lyrics Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

ARQ_API_URL = os.environ.get("ARQ_API_URL", None)
ARQ_API_KEY = os.environ.get("ARQ_API_KEY", None)
    
 

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

async def main():
        global arq
        session = ClientSession()
        arq = ARQ(ARQ_API_BASE_URL, ARQ_API_KEY, session)

        await bot.start()
        print(
        """
-----------------
| Bot Started! |
-----------------
"""
    )
        await idle()


    loop = get_event_loop()
    loop.run_until_complete(main())



