# -*- coding:utf-8 -*-
import datetime
import time
import wxpy
import news
from urllib.request import urlopen
from bs4 import BeautifulSoup

bot=wxpy.Bot(cache_path='wxpy.pkl')

def get_weather():
	#打开中国天气网的绍兴7天天气
	resp=urlopen('http://www.weather.com.cn/weather/101210507.shtml')
	soup=BeautifulSoup(resp,'html.parser')

	#weather作为明天天气变量
	TomorrowWeather=soup.find_all('p',class_="wea")[1].string
	TodayWeather=soup.find_all('p',class_="wea")[0].string

	#今天高低温度
	TodayTemperatureHigh=soup.find_all('p',class_="tem")[0].span.string
	TodayTemperatureLow=soup.find_all('p',class_="tem")[0].i.string

	#明天高低温度
	TomorrowTemperatureHigh=soup.find_all('p',class_="tem")[1].span.string
	TomorrowTemperatureLow=soup.find_all('p',class_="tem")[1].i.string
	return ('今天天气是'+'Today weather is '+TodayWeather+'\n最高温度是'
			+TodayTemperatureHigh+'\n最低温度是'+TodayTemperatureLow)
			

while True:
	'''get time now'''
	nowtime=datetime.datetime.now()
	#print(nowtime.strftime('%y/%m/%d %d %H:%M:%S'))
	'''send message at time'''
	if nowtime.hour==7 and nowtime.minute==0:
		weather=get_weather()
		friend=bot.search('Blueberry')[0]
		friend.send(weather)
		if TodayWeather.find('雨')!=-1 :
			friend.send('出门记得带好伞哦~')
		time.sleep(60)
	if nowtime.hour==22 and nowtime.minute==00:
		print('send news')
		dailysentence=news.get_news()
		friend=bot.search('Blueberry')[0]
		friend.send(dailysentence)
		time.sleep(60)

