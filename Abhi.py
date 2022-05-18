from pyrogram import Client, filters

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


def parse_url(url: str):
    # read url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"
    }
    req = Request(url, headers=headers)
    u_client = u_reqs(req)

    page_html = u_client.read()
    u_client.close()

    # scrape page as html
    page_soup = Soup(page_html, "html.parser")

    return page_soup


def get_lyrics(page_soup: Soup):
    # containerize
    containers = page_soup.find_all("div", {"class": "BNeawe tAd8D AP7Wnd"})
    lyrics = []

    for i in range(0, len(containers), 2):
        lyrics.append(containers[i].text)
    lyrics_str = "".join([str(x) for x in lyrics]).strip("\n")
    return lyrics_str


def get_artist(page_soup: Soup):
    # containerize
    containers = page_soup.find_all("span", {"class": "BNeawe s3v9rd AP7Wnd"})
    return containers[1].text


def get_title(page_soup: Soup):
    # containerize
    containers = page_soup.find_all("span", {"class": "BNeawe tAd8D AP7Wnd"})
    return containers[0].text


@Client.on_message(filters.command("lyrics"))
async def _get_lyrics(_, message: Message):
    chat_id = message.chat.id
    if len(message.command) < 2:
        return await message.reply((chat_id, "invalid_lyrics"))
    query = message.text.strip().split(None, 1)[1]
    lek = await message.reply((chat_id, "searching"))
    google_link = f"https://google.com/search?q={query}+lyrics"
    parsed = parse_url(google_link)
    lyrics, title, artist = get_lyrics(parsed), get_title(parsed), get_artist(parsed)
    await lek.edit((chat_id, "**Title: {}**\n**Artist: {}**\n\n**Lyrics: **\n{}").format(title, artist, lyrics))

bot.start()
print(
        """
-----------------
| Bot Started! |
-----------------
"""
    )
 
