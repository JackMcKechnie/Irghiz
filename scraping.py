from bs4 import BeautifulSoup
import requests

url = 'https://www.lemonde.fr/rss/une.xml'
resp = requests.get(url)
soup = BeautifulSoup(resp.content)

links = soup.find_all("guid")
urls = []
for item in links:
    urls.append(item.contents)

