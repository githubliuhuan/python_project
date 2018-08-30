# coding:utf8
'''
author:liuhuan
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import time
import re

# 解析入库
def insert_ecotone(url,csv_name):
	headers = { 'Authorization':'Basic ZHVja2NoaW5hOjZ1YzVjaDFuOQ==',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
			'Upgrade-Insecure-Requests':'1'
			   }
	req = requests.get(url,headers = headers,timeout = 1000)
	allline = (list(req.text.split('\n')))
	line_num = len((list(req.text.split('\n'))))
	for id in range(1,line_num-1):
		line = list(allline[id].split(','))
		idnr = line[0]
		gpsnumber = line[1]
		gpstime = line[2]
		smstime = line[3]
		latitude = line[4]
		longtitude = line[5]
		batteryvoltage = line[6]
		gpsdescription = line[7]
		temperature = line[8]
		gpsintervals = line[9]
		vhftelemetry = line[10]
		activity = line[11]
		gsmsignal = line[12].strip()
		gps_pos_csv = csv_name
		sql = 'insert into ecotone (gps_pos_csv,idnr,gpsnumber,gpstime,smstime,latitude,longtitude,batteryvoltage,gpsdescription,temperature,gpsintervals,vhftelemetry,activity,gsmsignal) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		try:
			cursor.execute(sql,(gps_pos_csv,idnr,gpsnumber,gpstime,smstime,latitude,longtitude,batteryvoltage,gpsdescription,temperature,gpsintervals,vhftelemetry,activity,gsmsignal))
			conn.commit()
			print('成功插入第%s条！%s %s'%((id),idnr,(time.strftime("%Y-%m-%d %X", time.localtime()))))
		except Exception as e:
			conn.rollback() #事务回滚
			print('事务处理失败！ %s %s'% (time.strftime("%Y-%m-%d %X", time.localtime())),e)

#返回url
def return_url(L = None):
	if L is None:
		L = []
		url = 'http://telemetry.ecotone.pl/duckchina/exports/positions/'
		headers = { 'Authorization':'Basic ZHVja2NoaW5hOjZ1YzVjaDFuOQ==',
				'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
				'Upgrade-Insecure-Requests':'1'
				   }
		req = requests.get(url,headers = headers,timeout = 1000)
		soup = BeautifulSoup(req.text,'lxml')
		list_csv = soup.find_all('a',href = re.compile('^gps_pos'))
		L.append(list_csv[0].text)
		return L

# 删除
def delete_ecotone(csv_name):
	try:
		cursor.execute('DELETE FROM ecotone WHERE gps_pos_csv = \'%s\'' % (csv_name))
		conn.commit()
	except Exception as e:
			conn.rollback() #事务回滚
			print('事务处理失败！%s %s'% (time.strftime("%Y-%m-%d %X", time.localtime())),e)

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
	url_list = return_url()
	# 遍历文件名
	for csv_name in url_list:
		url ='http://telemetry.ecotone.pl/duckchina/exports/positions/' + csv_name
		delete_ecotone(csv_name)
		insert_ecotone(url,csv_name)
	cursor.close()
	conn.close()