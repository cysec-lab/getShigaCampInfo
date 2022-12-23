#skrp2

import re
import requests
from bs4 import BeautifulSoup

url = 'https://ja.wordpress.org/download/releases/'
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

section = soup.find("section")
elems = section.find_all("tr")
print(elems)

for elem in elems:
    td = elem.find_all("td")
    print(f'{td[0].string},{td[1].string}')


