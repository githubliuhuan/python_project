# coding:utf8
'''
author:liuhuan
'''

import requests
from random import choice
import json
import pymysql
import time

# 获取授权
def return_Authentication():
	headers = {
			  'Request-Line':'POST /v1/user/login HTTP/1.1',
			   'Host':'api.druidtech.cn:9090',
			   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
			   'Accept':'application/json, text/plain, */*',
			   'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
			   'Accept-Encoding':'gzip, deflate, br',
			   'X-Druid-Authentication':'false',
			   'Referer':'http://bird.druidtech.cn/',
			   'Origin':'http://bird.druidtech.cn',
				'Content-Type':'application/json;charset=utf-8'
			   }
	data = {"username":"Database","password":"af8e5e2399ff98ca3692acda3fec1b79468789f04cb6a47b9cc0f074ed7ed450"}
	url_watch = 'https://api.druidtech.cn:9090/v1/user/login'
	try:
		rep_watch = requests.post(url_watch,data=json.dumps(data),headers=headers)
		return rep_watch.headers['X-Druid-Authentication']
	except Exception as e:
		print('授权失败！！！')
		return

# 解析html，入库
def insert_druid(tagert_num):
	for i in range(0, tagert_num):
		id = tagert[i]['id']
		device_id = tagert[i]['device_id']
		company_id = tagert[i]['company_id']
		company_name = tagert[i]['company_name']
		uuid = tagert[i]['uuid']
		firmware_version = tagert[i]['firmware_version']
		timestamp = tagert[i]['timestamp']
		updated_at = tagert[i]['updated_at']
		mark = tagert[i]['mark']
		sleep_time = tagert[i]['sleep_time']
		other_time = tagert[i]['other_time']
		activity_time = tagert[i]['activity_time']
		fly_time = tagert[i]['fly_time']
		peck_time = tagert[i]['peck_time']
		crawl_time = tagert[i]['crawl_time']
		run_time = tagert[i]['run_time']
		total_expend = tagert[i]['total_expend']
		sleep_expend = tagert[i]['sleep_expend']
		other_expend = tagert[i]['other_expend']
		activity_expend = tagert[i]['activity_expend']
		fly_expend = tagert[i]['fly_expend']
		peck_expend = tagert[i]['peck_expend']
		crawl_expend = tagert[i]['crawl_expend']
		run_expend = tagert[i]['run_expend']
		sql = 'insert into druid_technology_behavior (id,device_id,company_id,company_name,uuid,firmware_version,timestamp,updated_at,mark,sleep_time,other_time,activity_time,fly_time,peck_time,crawl_time,run_time,total_expend,sleep_expend,other_expend,activity_expend,fly_expend,peck_expend,crawl_expend,run_expend) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		try:
			cursor.execute(sql, (
			id, device_id, company_id, company_name, uuid, firmware_version, timestamp, updated_at, mark, sleep_time,
			other_time, activity_time, fly_time, peck_time, crawl_time, run_time, total_expend, sleep_expend,
			other_expend, activity_expend, fly_expend, peck_expend, crawl_expend, run_expend,))
			print('%s %s %s 成功插入第%s条！' % ((time.strftime("%Y-%m-%d %X", time.localtime())), device_id, id, i + 1))
			conn.commit()
		except Exception as e:
			conn.rollback()  # 事务回滚
			print('%s 事务处理失败 %s %s %s' % ((time.strftime("%Y-%m-%d %X", time.localtime())), device_id, id, e))
			return False

# 返回所有设备id值
def return_id(data, headers, L=None):
	if L is None:
		L = []
	url = "https://api.druidtech.cn:9090/v1/device/"
	req = requests.get(url,data = data,headers = headers,timeout = 5000)
	tagert = json.loads(req.text)
	for i in range(len(tagert)):
		L.append(tagert[i]['id'])
	return L

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
	headers = {
		'Request-Line': 'GET /v1/gps/ HTTP/1.1',
		'Host': 'api.druidtech.cn:9090',
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate, br',
		'X-Druid-Authentication': return_Authentication(),
		'X-Result-Sort': '-updated_at',
		'x-result-limit': '100',
		'x-result-offset': '0',
		'Referer': 'http://www.druidtech.cn/center/',
		'Origin': 'http://www.druidtech.cn'
	}
	data = {"username": "Database", "password": "testing"}
	device_list = return_id(data,headers)
	# 遍历设备号
	for device in device_list:
		# 定义偏移量
		headers['x-result-offset'] = '0'
		url = "https://api.druidtech.cn:9090/v1/behavior/device/%s?last=-6" % device
		while True:
			try:
				req = requests.get(url, data=data, headers=headers, timeout=5000)
				# 解析json格式,解出来是一个字典
				tagert = json.loads(req.text)
				# 判断是否有内容
				if len(tagert) != 0:
					tagert_num = len(tagert)
					print(headers['x-result-offset'])
					flag = insert_druid(tagert_num)
					# 判断是否爬取到最后一页
					if flag is None:
						headers['x-result-offset'] = str(int(headers['x-result-offset']) + 100)
						print('休眠2秒！')
						print('2..')
						time.sleep(1)
						print('1..')
						time.sleep(1)
					else:
						print('%s 爬取下一个追踪器！' % ((time.strftime("%Y-%m-%d %X", time.localtime()))))
						break
				else:
					break
			except Exception as e:
				print('连接失败！%s' % (e))

	cursor.close()
	conn.close()
