import urllib.request
import json
import webtech
from wplzer import Wappalyzer, WebPage
import hashlib

def makedict(url):
	arr=[]
	arr.extend(get_serverheader(url))
	arr.extend(get_tech(url))
	arr.extend(get_wappalyzer(url))
	arr.extend(get_etag(url))
	dic={}
	for i in arr:
		if i[0] not in dic:
			dic[i[0]]=i[1]
		elif dic[i[0]]==None:
			dic[i[0]]=i[1]

	print(dic)
def get_wappalyzer(url):
	wappalyzer = Wappalyzer.latest()
	webpage = WebPage.new_from_url(url)
	datas=[]
	parsed=wappalyzer.analyze_with_versions(webpage).values()
	for i in parsed:
		datas.append(list(i.values()))
		if datas[-1][-1]!=None:
			datas[-1][-1]=datas[-1][-1][0]

	return datas

def get_serverheader(url):
	try:
	    with urllib.request.urlopen(url) as response:
	    	headers = response.getheaders()
	    	status = response.getcode()

	    	datas=[]
	    	#datas.append(url)
	    	for i in headers:
	    		if i[0]=="Server" or i[0]=="X-Powered-By":
	    			for j in i[1].split(" "):
	    				datas.append(j.replace("(","").replace(")","").split("/"))
	    			#datas.extend(i[1].split(" "))
	    	for i in range(len(datas)):
	    		if len(datas[i])!=2:
	    			datas[i].append(None)
	    	return datas
	except urllib.error.URLError as e:
		return e.reason

def get_tech(url):
	wt = webtech.WebTech(options={'json': True})
	try:
		report = wt.start_from_url(url)
		data=[]
		#data.append(url)
		for i in report["tech"]:
			data.append(list(i.values()))
		return data
	except webtech.utils.ConnectionException:
		return "Connection error"

def get_etag(url):
	try:
	    with urllib.request.urlopen(url) as response:
	    	headers = response.getheaders()
	    	for i in headers:
	    		if i[0]=="ETag":
	    			return i[1]
	    	body = response.read()
	    	hs = hashlib.md5(body.decode('utf-8').encode()).hexdigest()
	    	return [["etag",hs]]
	except urllib.error.URLError as e:
		return e.reason

def page2md5(url):

	try:
		with urllib.request.urlopen(url) as response:
			body = response.read()
			hs = hashlib.md5(body.decode('utf-8').encode()).hexdigest()
			return hs
	except urllib.error.URLError as e:
		return e.reason

if __name__ == '__main__':
	url = 'https://cysec.ise.ritsumei.ac.jp/'
	#url = "http://www.rcc.ritsumei.ac.jp/"
	print("url:"+url)
	makedict(url)
