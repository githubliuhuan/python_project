#coding:utf8
'''
author:huan
'''

import requests
from bs4 import BeautifulSoup
import pymysql
import time
import re
import json
from random import choice

def get_ip_list(url, headers):
	web_data = requests.get(url, headers=headers)
	soup = BeautifulSoup(web_data.text, 'lxml')
	ips = soup.find_all('tr')
	ip_list = []
	for i in range(1, len(ips)):
		ip_info = ips[i]
		tds = ip_info.find_all('td')
		ip_list.append(tds[1].text + ':' + tds[2].text)
	return ip_list

def get_random_ip(ip_list):
	proxy_list = []
	for ip in ip_list:
		proxy_list.append('http://' + ip)
	proxy_ip = choice(proxy_list)
	proxies = {'http': proxy_ip}
	return proxies

def get_proxies():
	url = 'http://www.xicidaili.com/nn/'
	ip_list = get_ip_list(url, headers={'User-Agent':useragent()})
	proxies = get_random_ip(ip_list)
	return proxies

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

def get_html(url):
	try:
		user = useragent()
		headers = {'User-Agent':user}
		# proxies=get_proxies(),
		req = requests.get(url,headers=headers,timeout = 10000)
		return req.text
	except:
		print('请求失败，尝试重新连接...')
		print('休眠10秒！')
		time.sleep(10)
		print(url)
		get_html(url)
def convert_json(html):
	try:
		record = json.loads(html)
		return record
	except Exception as e:
		return

def insert_gbif(record,c,m):
	length = len(record['results'])
	for i in range(length):
		key_1 = str(record["results"][i].setdefault('key',None))
		datasetKey = str(record['results'][i].setdefault('datasetKey',None))
		publishingOrgKey = str(record['results'][i].setdefault('publishingOrgKey',None))
		publishingCountry = str(record['results'][i].setdefault('publishingCountry',None))
		protocol = str(record['results'][i].setdefault('protocol',None))
		lastCrawled = str(record['results'][i].setdefault('lastCrawled',None))
		lastParsed = str(record['results'][i].setdefault('lastParsed',None))
		crawlId = str(record['results'][i].setdefault('crawlId',None))
		extensions = str(record['results'][i].setdefault('extensions',None))
		basisOfRecord = str(record['results'][i].setdefault('basisOfRecord',None))
		taxonKey = str(record['results'][i].setdefault('taxonKey',None))
		kingdomKey = str(record['results'][i].setdefault('kingdomKey',None))
		phylumKey = str(record['results'][i].setdefault('phylumKey',None))
		classKey = str(record['results'][i].setdefault('classKey',None))
		orderKey = str(record['results'][i].setdefault('orderKey',None))
		familyKey = str(record['results'][i].setdefault('familyKey',None))
		genusKey = str(record['results'][i].setdefault('genusKey',None))
		speciesKey = str(record['results'][i].setdefault('speciesKey',None))
		scientificName = str(record['results'][i].setdefault('scientificName',None))
		kingdom = str(record['results'][i].setdefault('kingdom',None))
		phylum = str(record['results'][i].setdefault('phylum',None))
		order_1 = str(record['results'][i].setdefault('order',None))
		family = str(record['results'][i].setdefault('family',None))
		genus = str(record['results'][i].setdefault('genus',None))
		species = str(record['results'][i].setdefault('species',None))
		genericName = str(record['results'][i].setdefault('genericName',None))
		specificEpithet = str(record['results'][i].setdefault('specificEpithet',None))
		taxonRank = str(record['results'][i].setdefault('taxonRank',None))
		dateIdentified = str(record['results'][i].setdefault('dateIdentified',None))
		decimalLongitude = str(record['results'][i].setdefault('decimalLongitude',None))
		decimalLatitude = str(record['results'][i].setdefault('decimalLatitude',None))
		coordinateUncertaintyInMeters = str(record['results'][i].setdefault('coordinateUncertaintyInMeters',None))
		year_1 = str(record['results'][i].setdefault('year',None))
		month_1 = str(record['results'][i].setdefault('month',None))
		day_1 = str(record['results'][i].setdefault('day',None))
		eventDate = str(record['results'][i].setdefault('eventDate',None))
		issues = str(record['results'][i].setdefault('issues',None))
		modified = str(record['results'][i].setdefault('modified',None))
		lastInterpreted = str(record['results'][i].setdefault('lastInterpreted',None))
		references_1 = str(record['results'][i].setdefault('references',None))
		license = str(record['results'][i].setdefault('license',None))
		identifiers = str(record['results'][i].setdefault('identifiers',None))
		media = str(record['results'][i].setdefault('media',None))
		facts = str(record['results'][i].setdefault('facts',None))
		relations = str(record['results'][i].setdefault('relations',None))
		geodeticDatum = str(record['results'][i].setdefault('geodeticDatum',None))
		class_1 = str(record['results'][i].setdefault('class',None))
		countryCode = str(record['results'][i].setdefault('countryCode',None))
		country = str(record['results'][i].setdefault('country',None))
		rightsHolder = str(record['results'][i].setdefault('rightsHolder',None))
		identifier = str(record['results'][i].setdefault('identifier',None))
		informationWithheld = str(record['results'][i].setdefault('informationWithheld',None))
		verbatimEventDate = str(record['results'][i].setdefault('verbatimEventDate',None))
		datasetName = str(record['results'][i].setdefault('datasetName',None))
		gbifID = str(record['results'][i].setdefault('gbifID',None))
		collectionCode = str(record['results'][i].setdefault('collectionCode',None))
		verbatimLocality = str(record['results'][i].setdefault('verbatimLocality',None))
		occurrenceID = str(record['results'][i].setdefault('occurrenceID',None))
		taxonID = str(record['results'][i].setdefault('taxonID',None))
		catalogNumber = str(record['results'][i].setdefault('catalogNumber',None))
		recordedBy = str(record['results'][i].setdefault('recordedBy',None))
		http_unknown_org_occurrenceDetails = str(record['results'][i].setdefault('http://unknown.org/occurrenceDetails',None))
		institutionCode = str(record['results'][i].setdefault('institutionCode',None))
		rights = str(record['results'][i].setdefault('rights',None))
		eventTime = str(record['results'][i].setdefault('eventTime',None))
		identificationID = str(record['results'][i].setdefault('identificationID',None))
		_datasetKey = str(record['results'][i].setdefault('_datasetKey',None))
		_publishingOrgKey = str(record['results'][i].setdefault('_publishingOrgKey',None))
		_verbatimRecord = str(record['results'][i].setdefault('_verbatimRecord',None))
		scrapy_country = c
		sql = 'insert into gbif_ru (key_1,datasetKey,publishingOrgKey,publishingCountry,protocol,lastCrawled,lastParsed,crawlId,extensions,basisOfRecord,taxonKey,kingdomKey,phylumKey,classKey,orderKey,familyKey,genusKey,speciesKey,scientificName,kingdom,phylum,order_1,family,genus,species,genericName,specificEpithet,taxonRank,dateIdentified,decimalLongitude,decimalLatitude,coordinateUncertaintyInMeters,year_1,month_1,day_1,eventDate,issues,modified,lastInterpreted,references_1,license,identifiers,media,facts,relations,geodeticDatum,class_1,countryCode,country,rightsHolder,identifier,informationWithheld,verbatimEventDate,datasetName,gbifID,collectionCode,verbatimLocality,occurrenceID,taxonID,catalogNumber,recordedBy,http_unknown_org_occurrenceDetails,institutionCode,rights,eventTime,identificationID,_datasetKey,_publishingOrgKey,_verbatimRecord,scrapy_country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
		try:
			cursor.execute(sql,(key_1,datasetKey,publishingOrgKey,publishingCountry,protocol,lastCrawled,lastParsed,crawlId,extensions,basisOfRecord,taxonKey,kingdomKey,phylumKey,classKey,orderKey,familyKey,genusKey,speciesKey,scientificName,kingdom,phylum,order_1,family,genus,species,genericName,specificEpithet,taxonRank,dateIdentified,decimalLongitude,decimalLatitude,coordinateUncertaintyInMeters,year_1,month_1,day_1,eventDate,issues,modified,lastInterpreted,references_1,license,identifiers,media,facts,relations,geodeticDatum,class_1,countryCode,country,rightsHolder,identifier,informationWithheld,verbatimEventDate,datasetName,gbifID,collectionCode,verbatimLocality,occurrenceID,taxonID,catalogNumber,recordedBy,http_unknown_org_occurrenceDetails,institutionCode,rights,eventTime,identificationID,_datasetKey,_publishingOrgKey,_verbatimRecord,scrapy_country))
			print('%s 成功插入第%s条！%s key:%s month:%s' % ((time.strftime("%Y-%m-%d %X", time.localtime())),(i+1),c,key_1,m))
			conn.commit()
		except Exception as e:
			conn.rollback() #事务回滚
			print('事务处理失败 %s %s %s %s %s' % (time.strftime("%Y-%m-%d %X", time.localtime()),e,c,key_1,m))
			return True
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
	country = ['RU']
	for c in country:
		month = ['1','2','3','4','5','6','7','8','9','10','11','12']
		for m in month:
			num = 0
			while True:
				url = 'https://www.gbif.org/api/occurrence/search?advanced=false&country=%s&facet=country&facet=month&facetMultiselect=true&issue.facetLimit=1000&locale=en&month=%s&month.facetLimit=12&offset=%s&taxon_key=212&type_status.facetLimit=1000&year=1000,2017' % (c,m,str(num))
				print(url)
				html = get_html(url)
				record = convert_json(html)
				while True:
					try:
						print(len(record["results"]))
						break
					except:
						html = get_html(url)
						record = convert_json(html)
				if len(record["results"]) is not 0:
					flag = insert_gbif(record,c,m)
					print(flag)
					if flag is False:
						print('休眠3秒！')
						print('3..')
						time.sleep(1)
						print('2..')
						time.sleep(1)
						print('1..')
						time.sleep(1)
						num = num + 20
						# print('%s 已成功插入%s条！' % (time.strftime("%Y-%m-%d %X", time.localtime())),success)
					else:
						print('%s 爬取下一个区域！' % ((time.strftime("%Y-%m-%d %X", time.localtime()))))
						break
				else:
					print('record为空')
					break

	cursor.close()
	conn.close()