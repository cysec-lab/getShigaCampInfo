#skrp4 6.1.1の脆弱性情報を取得する

import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent':'Mozilla/5.0'
}

vuln_set = []

with open('version(skrp3).txt', 'r') as f:
    ver_list = f.read().split("\n")
#print(ver_list)

for ver_str in ver_list:
    ver = ver_str.replace('.', '')  # 6.0.3 が 603 に
    url = 'https://wpscan.com/wordpress/' + ver
    # print(url)

    res = requests.get(url, headers=headers)
    if not res.ok:
        print(res, url)
    soup = BeautifulSoup(res.text, "html.parser")
    # print(soup)
        
    tables = soup.find_all("div", class_='table_tableBody__3FFxC')
    #print(tables[1])
    div = tables[1].find_all("div", class_="table_tableRow__cHvfD")
    # print(div[0])

    for elem in div:
        # print(elem)
        b = elem.find_all("div")
        
        # vuln_set　にあるかチェック
        # ないなら入れる
        # if b not in vuln_set:
            # vuln_set.append(b)
        print(f"{ver_str},{b[0].string},{b[1].find('a').string},{b[2].find('span').text}")
        with open('database(version).csv', 'a') as f:
            print(f"{ver_str},{b[0].string},{b[1].find('a').string},{b[2].find('span').text}", file=f)

            
    # print()
    time.sleep(30)

