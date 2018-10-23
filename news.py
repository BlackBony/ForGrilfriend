#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup


"""获取金山词霸每日一句，英文和翻译"""
def get_news():
	
	resp=urlopen('http://www.wufazhuce.com/')
	soup=BeautifulSoup(resp,'html.parser')

	#print(soup.find('img',class_="fp-one-imagen"))
	text=soup.find_all('a')[2].string
	return text

