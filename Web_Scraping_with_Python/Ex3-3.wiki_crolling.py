from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            print(newPage)
            pages.add(newPage)
            getLinks(newPage)

getLinks("")