#tesuto

import re
import requests
from bs4 import BeautifulSoup
import time

with open('version(skrp3).txt', 'r') as f:
    ver_list = f.read().split("\n")
print(ver_list)

headers = {
    'User-Agent':'Mozilla/5.0'
}

for ver_str in ver_list:
    ver = ver_str.replace('.', '')  # 6.0.3 が 603 に
    url = 'https://wpscan.com/wordpress/' + ver
    print(url)
    response = requests.get(url, headers=headers)
    code = response.status_code

    if code == 200:#OK
        #スクレイピングをする。
        print('OK', ver_str)
    elif code == 404:#Not Found 
        print('Not Found', ver_str)
        continue
    else:
        print('???', ver_str, code)
    
    # WPScan のサイトは 1 分間に 5 回までしかアクセスできない？
    # Too many requests (429) 対策
    time.sleep(13)