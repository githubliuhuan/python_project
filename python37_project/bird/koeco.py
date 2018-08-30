import requests
from random import choice
from bs4 import BeautifulSoup
import re
import time
import pymysql

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


def return_id():
	pass


def insert_koeco(id,j,user):
	url = "http://1.214.255.154/main/wt_view.php?id=%s&page=%s&list_num=30&sort1=&ordr1=&src_name=&src_value=" % (str(id),str(j))
	headers = {
	              'Request-Line':'GET /main/wt_view.php?id=1c56155 HTTP/1.1',
	               'Host':'1.214.255.154',
	               'User-Agent':user
	               }

	req = requests.get(url,headers,timeout = 1000)
	soup = BeautifulSoup(req.text,'lxml')
	tracker_id = soup.find_all('th',class_ = re.compile(r'^title_001'))
	tracker_id = tracker_id[0].text
	recorder_tr = soup.find_all(style="height: 28px;")
	recorder_num = len(recorder_tr)
	if recorder_num is not 0:
		for i in range(0,recorder_num):
			list1 = list(recorder_tr[i].text.split("\n"))
			list2 = [x for x in list1 if x != '']
			seq = list2[0]
			date_utc = list2[1]
			date_kst = list2[2]
			decimal_latitude = list2[3]
			decimal_longitude = list2[4]
			dms_latitude = list2[5]
			dms_longitude = list2[6]
			altitude = list2[7]
			heading = list2[8]
			speed = list2[9]
			satellite = list2[10]
			fixed_level = list2[11]
			dop = list2[12]
			contact_time = list2[15].strip()
			volt = list2[16]
			# print(no)
			# print(tracker_id)
			# print(date_utc)
			# print(date_kst)
			# print(decimal_latitude)
			# print(decimal_longitude)
			# print(dms_latitude)
			# print(dms_longitude)
			# print(altitude)
			# print(heading)
			# print(speed)
			# print(satellite)
			# print(fixed_level)
			# print(dop)
			# print(contact_time.strip())
			# print(volt)
			# exit()
			sql = 'insert into bird_koeco (seq,tracker_id,date_utc,date_kst,decimal_latitude,decimal_longitude,dms_latitude,dms_longitude,altitude,heading,speed,satellite,fixed_level,dop,contact_time,volt) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
			try:
				cursor.execute(sql,(seq,tracker_id,date_utc,date_kst,decimal_latitude,decimal_longitude,dms_latitude,dms_longitude,altitude,heading,speed,satellite,fixed_level,dop,contact_time,volt))
				conn.commit()
				print('成功插入第%s条！%s %s'%((i+1),seq,(time.strftime("%Y-%m-%d %X", time.localtime()))))
			except Exception as e:
				conn.rollback() #事务回滚
				print('事务处理失败,准备爬取下一个追踪器！%s %s'% (time.strftime("%Y-%m-%d %X", time.localtime())),e)
				return False
		return True
	else:
		print('此页没有数据，准备爬取下一个追踪器!')
		return False

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
	#root_url = "http://1.214.255.154/"
	user = useragent()
	# list_id = return_id(root_url,user)
	list_id = ['1c56155']
	for id in list_id:
		user = useragent()
		j = 1
		while True:
			result = insert_koeco(id,j,user)
			if result is True:
				print('成功爬取第%s页！%s'%(j,(time.strftime("%Y-%m-%d %X", time.localtime()))))
				j = j + 1
				print('休眠3秒！')
				print('3..')
				time.sleep(1)
				print('2..')
				time.sleep(1)
				print('1..')
				time.sleep(1)
			else:
				break
	print('本次所有追踪器的数据已经爬取结束！%s' % ((time.strftime("%Y-%m-%d %X", time.localtime()))))
	cursor.close()
	conn.close()