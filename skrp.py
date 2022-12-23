#上場企業のスクレイピングを行う

import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.kstcci.or.jp/members'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

#elems = soup.find_all(href=re.compile("www.yotai.co.jp"))
section = soup.find("section")
elems = section.find_all("a")

for elem in elems:
    print(f'{elem.string},{elem["href"]}')
