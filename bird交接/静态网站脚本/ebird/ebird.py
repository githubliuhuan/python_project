#coding:utf8
'''
author:liuhuan
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import time
import re


# 请求资源
def get_html(url):
	try:
		req = requests.get(url,timeout = 10000)
		return req.text
	except:
		return

# 转换格式
def convert_format(string):
	return  " ".join([x for x in string.text.split('\n') if x != ''])

# 存成list
def convert_list(string,L = None):
	if L is None:
		L = []
		for i in range(len(string)):
			L.append([x.strip() for x in [x for x in string[i].text.split('\n') if x != '']])
		return L

# 解析入库
def insert_ebird(url,c,S = None):
	if S is None:
		# 定义一个集合，存checklist
		S = set()
		html = get_html(url)
		soup = BeautifulSoup(html,'lxml')
		species_has = soup.find_all('tr',class_=re.compile('has-details'))
		species_checklist = soup.find_all('a',href=re.compile('^/ebird/view/checklist/'))
		species_obs = soup.find_all('tr',class_=re.compile('obs-details'))
		# 遍历记录
		for i in range(len(species_has)):
			species_list = list(species_has[i].text.split("\n"))
			species_comment = list(species_obs[i].text.split("\n"))
			species_id = species_list[1]
			species_name = species_list[2]
			species_count = species_list[3]
			species_date = species_list[4]
			species_by = species_list[8]
			# bird_checklist的链接
			soup_href = BeautifulSoup(str(species_has[i]),'lxml')
			species_href = soup_href.a['href']
			species_loc = species_comment[5]
			species_country = c
			sql = 'insert into ebird_record (species_id,species_name,species_count,species_date,species_by,species_href,species_loc,species_country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)'
			try:
				cursor.execute(sql,(species_id,species_name,species_count,species_date,species_by,species_href,species_loc,species_country))
				conn.commit()
				print('%s 已提交%s条数据！ %s %s %s' % (time.strftime("%Y-%m-%d %X", time.localtime()),i+1,c,species_id,species_name))
			except Exception as e:
				conn.rollback() #事务回滚
				print('%s %s %s %s已经存在！%s'% (time.strftime("%Y-%m-%d %X", time.localtime()),c,species_id,species_name,e))
				return

			# 请求、解析checklist并入库
			url_checklist = 'http://ebird.org'+str(species_href)
			html = get_html(url_checklist)
			if html is not None:
				soup = BeautifulSoup(html,'lxml')
				checklist = soup.find_all('h5',class_='rep-obs-date')
				checklist_o = soup.find_all('dl',class_='def-list')
				checklist_t = soup.find_all('tr',class_ = 'spp-entry')
				species_time = convert_format(checklist[0])
				species_total = str(convert_list(checklist_t))
				species_date_effort = str(convert_list(checklist_o))
				if species_href not in S:
					S.add(species_href)
					sql_1 = "insert into ebird_checklist (species_href,species_time,species_date_effort,species_total) VALUES (%s,%s,%s,%s)"
					try:
						cursor.execute(sql_1,(species_href,species_time,species_date_effort,species_total))
						conn.commit()
						print('%s 已提交对应的checklist记录！ %s %s' % (time.strftime("%Y-%m-%d %X", time.localtime()),url_checklist,c))
					except Exception as e:
						conn.rollback() #事务回滚
						print('%s %s 提交%s对应的checklist记录失败!'% (time.strftime("%Y-%m-%d %X", time.localtime()),c,url_checklist,e))
						# return S
						# cursor.close()
						# conn.close()
				else:
					continue
			else:
				print('%s %s 提交%s对应的checklist记录失败!'% (time.strftime("%Y-%m-%d %X", time.localtime()),c,url_checklist))
				continue
			print('休眠1秒！')
			print('1..')
			time.sleep(1)

# 程序入口
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
	url = 'http://ebird.org/ebird/country/%s?yr=all&changeDate=Set'
	# 东亚6国
	country = ['CN','RU','MN','JP','KP','KR','HK','TW','MO']
	for c in country:
		url_c = url % (c)
		insert_ebird(url_c,c)
		# for href in href_list:
		# 	url_1 = 'http://ebird.org'+str(href)
		# 	insert_checklist(url_1)
	cursor.close()
	conn.close()


