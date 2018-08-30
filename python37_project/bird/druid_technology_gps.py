# coding:utf8
'''
author:刘焕
'''

import requests
from random import choice
import json
import pymysql
import time

#获取授权
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
    for i in range(0,tagert_num):
        id = tagert[i]['id']
        device_id = tagert[i]['device_id']
        company_id = tagert[i]['company_id']
        company_name = tagert[i]['company_name']
        mark = tagert[i]['mark']
        uuid = tagert[i]['uuid']
        firmware_version = tagert[i]['firmware_version']
        updated_at = tagert[i]['updated_at']
        timestamp = tagert[i]['timestamp']
        sms = tagert[i]['sms']
        longitude = tagert[i]['longitude']
        latitude = tagert[i]['latitude']
        altitude = tagert[i]['altitude']
        temperature = tagert[i]['temperature']
        humidity = tagert[i]['humidity']
        light = tagert[i]['light']
        pressure = tagert[i]['pressure']
        used_star = tagert[i]['used_star']
        view_star = tagert[i]['view_star']
        dimension = tagert[i]['dimension']
        speed = tagert[i]['speed']
        horizontal = tagert[i]['horizontal']
        vertical = tagert[i]['vertical']
        course = tagert[i]['course']
        battery_voltage = tagert[i]['battery_voltage']
        signal_strength = tagert[i]['signal_strength']
        point_location = tagert[i]['point_location']
        fix_time = tagert[i]['fix_time']
        sql = 'insert into druid_technology_gps (id,device_id,company_id,company_name,mark,uuid,firmware_version,updated_at,timestamp,sms,longitude,latitude,altitude,temperature,humidity,light,pressure,used_star,view_star,dimension,speed,horizontal,vertical,course,battery_voltage,signal_strength,point_location,fix_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        try:
            cursor.execute(sql,(id,device_id,company_id,company_name,mark,uuid,firmware_version,updated_at,timestamp,sms,longitude,latitude,altitude,temperature,humidity,light,pressure,used_star,view_star,dimension,speed,horizontal,vertical,course,battery_voltage,signal_strength,point_location,fix_time))
            print('%s %s %s 成功插入第%s条!' % ((time.strftime("%Y-%m-%d %X", time.localtime())),device_id,id,i+1))
            conn.commit()
        except Exception as e:
            conn.rollback() #事务回滚
            print('%s 事务处理失败 %s %s %s' % ((time.strftime("%Y-%m-%d %X", time.localtime())),device_id,id,e))
            return False

#返回所有设备id值
def return_id(data, headers, L=None):
    if L is None:
        L = []
    url = "https://api.druidtech.cn:9090/v1/device/"
    req = requests.get(url,data = data,headers = headers,timeout = 5000)
    tagert = json.loads(req.text)
    for i in range(len(tagert)):
        L.append(tagert[i]['id'])
    return L

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
          'Request-Line':'GET /v1/gps/ HTTP/1.1',
           'Host':'api.druidtech.cn:9090',
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
           'Accept':'application/json, text/plain, */*',
           'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
           'Accept-Encoding':'gzip, deflate, br',
           'X-Druid-Authentication':return_Authentication(),
           'X-Result-Sort':'-updated_at',
            'x-result-limit':'100',
            'x-result-offset':'0',
           'Referer':'http://www.druidtech.cn/center/',
           'Origin':'http://www.druidtech.cn'
           }
    data = {"username":"Database","password":"testing"}
    device_list = return_id(data,headers)
    for device in device_list:
        headers['x-result-offset'] = '0'
        #url = "https://api.druidtech.cn:9090/v1/gps/device/594f884650bd08c3efd7a9c5?begin=2000-01-01T00:00:00.000Z&end=2017-09-01T00:00:00.000Z"
        url = "https://api.druidtech.cn:9090/v1/gps/device/%s?last=-6" % device
        while True:
            try:
                req = requests.get(url, data=data, headers=headers, timeout=5000)
                #解析json格式,解出来是一个字典
                tagert = json.loads(req.text)
                if len(tagert) != 0:
                    tagert_num = len(tagert)
                    print(headers['x-result-offset'])
                    flag = insert_druid(tagert_num)
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