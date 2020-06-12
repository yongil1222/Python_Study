import requests 
from bs4 import BeautifulSoup

url = 'https://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do'
params = {'currentPage':1, 'rowPerPage' : 300}
html = requests.get(url, params=params).text
soup = BeautifulSoup(html, 'html.parser')

names = []
for tag in soup.select('a[href*=jsMemPop]'):
    names.append(tag.text)

import pandas as pd

series = pd.Series(names)
series.str.slice(0,1).value_counts().plot(kind='bar', figsize=(12,3))
