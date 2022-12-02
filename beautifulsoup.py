	
import requests
from bs4 import BeautifulSoup


url = 'https://jvndb.jvn.jp/search/index.php?mode=_vulnerability_search_IA_VulnSearch'
res = requests.get(url)

res.text

soup = BeautifulSoup(res.text, "html.parser")

	
elems = soup.select('#myjvn > div > div > table.result_class > tbody')

elems[0]
elems[0].contents[0]
elems[0].attrs['href']