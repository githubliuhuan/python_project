#coding:utf8
'''
author:刘焕
'''

import requests
from bs4 import BeautifulSoup
import re
import pymysql
import time
from random import choice

def useragent():
	USER_AGENTS = [
		"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
		"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
		"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
		"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
		"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
		"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
		"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
		"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
		"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
		"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
		"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
		"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
	]
	headers =choice(USER_AGENTS)
	return headers


def insert_index(j):
	url = 'http://www.birdreport.cn/Watch/Index?pageIndex='+str(j)
	user = useragent()
	headers = {'User-Agent':user}
	ret = requests.get(url,headers = headers,timeout = 500)
	soup = BeautifulSoup(ret.text,'lxml')
	key = soup.find_all('tr',class_=re.compile(r'^stripStyle'))
	link = soup.find_all('a',href=re.compile(r'^/Member/WatchRecord?'))
	num = len(key)
	if num != 0:
		list_id = []
		for i in range(0,num):
			list1 = list(key[i].text.split("\n"))
			list2 = [x for x in list1 if x != '']
			list3 = list(link[i].get('href').split("\n"))
			link1 = "".join(list3)
			seq = list2[0].strip()
			observ_time = list2[1].strip()
			observ_site = list2[2].strip()
			bird_species = list2[3].strip()
			recorder = list2[4].strip()
			browse_count = list2[5].strip()
			create_time = list2[6].strip()
			id =link1[23:]
			list_id.append(id)
			sql = 'insert into china_observ_birds_recordcenter (id,seq,observ_time,observ_site,bird_species,recorder,browse_count,create_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
			try:
				cursor.execute(sql,(id,seq,observ_time,observ_site,bird_species,recorder,browse_count,create_time))
			except Exception as e:
				conn.rollback() #事务回滚
				print('事务处理失败 %s %s'% (time.strftime("%Y-%m-%d %X", time.localtime()),e))
				return list_id
			else:
				conn.commit()   #事务提交
				print('爬取第%s页第%s条数据成功 (%s)! %s' % ((j),(i+1),id,(time.strftime("%Y-%m-%d %X", time.localtime()))))
		print('休眠2秒！')
		time.sleep(2)
		print('2..')
		time.sleep(1)
		print('1..')
		time.sleep(1)
		return list_id
	else:
		print('本次爬取结束！%s' % (time.strftime("%Y-%m-%d %X", time.localtime())))
		cursor.close()
		conn.close()
		exit()

def insert_watch(id):
	data = {"Account":"水鸟与湿地","Password":"shidi2017"}
	url_watch = 'http://www.birdreport.cn/Member/WatchRecord?id='+str(id)
	rep_watch = requests.get(url_watch,data,timeout = 1000)
	soup = BeautifulSoup(rep_watch.text,'lxml')
	aa = soup.find_all('div',style=re.compile(r'height: 25px; margin-top: 0px;'))
	cc = ''
	for k in range(1,len(aa)):
		bb = aa[k].text
		cc = cc.strip() + '|' + bb.strip()
	birds_name = cc
	sql = 'insert into china_observ_birds_recordcenter_watchrecord (id,birds_name) VALUES (%s,%s)'
	try:
		cursor.execute(sql,(id,birds_name))
	except Exception as e:
		conn.rollback() #事务回滚
		print('事务处理失败 %s %s'% (time.strftime("%Y-%m-%d %X", time.localtime()),e))
		cursor.close()
		conn.close()
		exit()
	else:
		conn.commit()   #事务提交

if __name__ == '__main__':
	print('连接到mysql服务器...')
	conn = pymysql.connect(host='rm-8vbqudhd5zy60sin3o.mysql.zhangbei.rds.aliyuncs.com',
						   user='bird',
						   password='Bird@2017',
						   db='birds_db',
						   port=3306,
						   charset='utf8'
						   );
	print('连接上了!')
	cursor = conn.cursor()
	j = 1
	while True:
		list_id1 = insert_index(j)
		count = 1
		for id in list_id1:
			insert_watch(id)
			print('爬取第%s页第%s条记录观测的鸟的种类成功 (%s)! %s' % ((j),(count),id,(time.strftime("%Y-%m-%d %X", time.localtime()))))
			print('休眠1秒！')
			print('1..')
			time.sleep(1)
			count = count + 1
		print('成功爬取第%s页数据！%s' % ((j),(time.strftime("%Y-%m-%d %X", time.localtime()))))
		print('休眠2秒！')
		print('2..')
		time.sleep(1)
		print('1..')
		time.sleep(1)
