from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" +  urlparse(includeUrl).netloc
    internalLinks = []
    
    for link in bsObj.findAll("a", href=re.compile("^(/|.*" + includeUrl + ")")) :
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in internalLinks :
                if (link.attrs['href'].startswith("/")) :
                    internalLinks.append(includeUrl+link.attrs['href'])
                else :
                    internalLinks.append(link.attrs['href'])

    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []

    for link in bsObj.findAll("a", href = re.compile("^(http|www)((?!" + excludeUrl + ").)*$")) :
        if link.attrs['href'] is not None :
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    
    return externalLinks

def getRandomExternalLink(startPage):
    html = urlopen(startPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startPage).netloc)
    if len(externalLinks) == 0 :
        domain = urlparse(startPage).scheme + "://" + urlparse(startPage).netloc
        internalLinks =getInternalLinks(bsObj, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else :
        return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startPage):
    externalLink = getRandomExternalLink(startPage)
    print("Random external link is " + externalLink)
    followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")