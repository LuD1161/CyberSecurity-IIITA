import requests
import json
from bs4 import BeautifulSoup
from random import randint
import time
blacklist={}
list=[]
url=("http://www.colasoft.com/resources/ports_list.php")
r = requests.get(url)
data=BeautifulSoup(r.content,"lxml")
black=data.find_all("table",{"class":"Content"})
for i in black:
	black2=i.find_all('tr')
	for j in black2:
		black3=j.find_all('td')
		for k in black3:
			black4=k.get_text()
			list.append(black4)
for ab in range(0,len(list),5):
	if str(list[ab+4])=='n':
			abcd=(list[ab]).encode('utf-8')+',,'+(list[ab+2]).encode('utf-8')+',,'+list[ab+1].encode('utf-8')
			blacklist[abcd]=list[ab+3].encode('utf-8')
with open('blacklist.json', 'w') as fp:
    json.dump(blacklist, fp,indent=8)


'''
		portnumber=(list[ab]).encode('utf-8')
		service=(list[ab+2]).encode('utf-8')
		typeofport=(list[ab+1]).encode('utf-8')
		blacklist[x]={}
		blacklist[x][y]={}
		blacklist[x]['type']=(list[ab+1]).encode('utf-8')
		blacklist[x]['service']=(list[ab+2]).encode('utf-8')
		blacklist[x]['description']=(list[ab+3]).encode('utf-8')'''
