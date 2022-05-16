from Helper import page_soup

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
