#脆弱性情報のスクレイピング

import re
import requests
from bs4 import BeautifulSoup

with open('version(skrp3).txt', 'r') as f:
    ver_list = f.read().split("\n")
print(ver_list)

for ver_str in ver_list:
    ver = ver_str.replace('.', '')  # 6.0.3 が 603 に
    url = 'https://wpscan.com/wordpress/' + ver
    print(url)


    '''
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    section = soup.find("div")
    elems = section.find_all("")
    print(elems)
    
    for elem in elems:
        div = elem.find_all("div")
        print(f'{div[0].string},{div[1].string}')
        
        #保存のコードを書く
        with open('database(version).csv', 'a') as f:
            print()
    '''

