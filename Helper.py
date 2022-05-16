from urllib.request import urlopen as u_reqs, Request
from bs4 import BeautifulSoup as Soup


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
