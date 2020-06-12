from bs4 import BeautifulSoup
from urllib.request import urlopen

response = urlopen('https://naver.com')
soup = BeautifulSoup(response, 'html.parser')

for anchor in soup.select("div.ah_k"):
    print(anchor)