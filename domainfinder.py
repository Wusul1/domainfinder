import requests
from urllib.parse import urlparse
def extract_base_url(url):
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    return base_url
from bs4 import BeautifulSoup
links=[input("Starting URL: ")]
visited = []
first = True
while True:
    for link in links:
        if not link in visited:
         visited.append(link)
         try:
            r = requests.get(link).content
         except:
            continue
         soup = BeautifulSoup(r,"html.parser").find_all("a")
         for link in soup:
            try:
                url = link["href"]
            except KeyError:
                continue
            if url[0:4] == "http":
                url = extract_base_url(url)
                if url not in links:
                    print(url)
                    links.append(url)
