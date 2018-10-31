#coding=utf8
from bs4 import BeautifulSoup
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def tuijian(name):
	urll = 'https://wenku.baidu.com/search?lm=1&word='+name
	headers = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
	}
	mb_data = requests.get(urll,headers=headers)
	soup = BeautifulSoup(mb_data.text,'lxml')
	tag = soup.select('#bd > div > div > div.main > div > dl > dt > p.fl > a')
	#print len(tag)
	urls=[]
	for i in range(1,4):
		urls.append(tag[i].get('href'))
	titles =[]
	for i in range(0,3):
		reponse=requests.get(urls[i], headers=headers)
		conent=reponse.content.decode('gbk')
		title = re.findall(r"title.*?\:.*?\'(.*?)\'\,", conent)[0]
		titles.append(title)
		#print title
	#print len(titles)
	return urls,titles
