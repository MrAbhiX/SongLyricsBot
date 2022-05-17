from Abhi import Bot
from pyrogram import filters, Client
from pyrogram.types import Message

from Search import get_lyrics, get_artist, get_title
from Helper import parse_url


@Client.on_message(filters.command("lyrics") & filters.group)
async def _get_lyrics(_, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply((chat_id, "**You must give title mpre than 2 characters**"))
    
    lakshu = await message.reply((chat_id, "searching"))
    google_link = f"https://google.com/search?q={query}+lyrics"
    parsed = parse_url(google_link)
    lyrics, title, artist = get_lyrics(parsed), get_title(parsed), get_artist(parsed)
    await lakshu.edit((chat_id, "**Title: {}**\n**Artist: {}**\n\n**Lyrics: **\n{}").format(title, artist, lyrics))
