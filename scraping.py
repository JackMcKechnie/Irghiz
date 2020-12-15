from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def le_monde():
    url = 'https://www.lemonde.fr/rss/une.xml'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, features="html.parser")

    links = soup.find_all("guid")
    urls = []
    for item in links:
        urls.append(item.contents[0])

    texts = []
    for url in urls:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        dirty_text = soup.get_text()
        text = " ".join(dirty_text.split())
        texts.append((text, soup.title.string, url))

    return texts


le_monde()

