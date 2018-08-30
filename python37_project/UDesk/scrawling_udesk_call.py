#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib.request as ur
import requests
import json
import pymysql
import os
import time
import re

headers={
    'Content-Length': '267',
    'Content-Type': 'application/json',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    # baihanqing
    # 'Cookie': 'Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760; _ga=GA1.2.1676670225.1512370465; Qs_lvt_102458=1512371267; Qs_pv_102458=2510706366026374000; Hm_lvt_85cdbdd6ba7f014cd503e9f1cd5e5ba0=1512371267; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220; aliyungf_tc=AQAAAAj1axqKLgIALBIM0hz/fufQ5gRy; _helpdesksysteem_session=ZHgzYTArbmdjbEVwUVFka0dnWDd5ZkdtMXZnc1RwVEtyK3hhTU1zTGFaZXRYUXE3QnJzYU92NW9YSGk4a0ZxVU5SWUFraFgzU2hRaWF5ZDJIT2E2R3JkeDBqSHhpZDRNM1RxTXV1bmYzVWpUeUtBZThVNTBIRnFwYVVDR3NNSjVGbGZMNGVldkR4VWNRTW55eXdKeUFUUjhUYkU5NnduOGp1UlNUZThKcGtnM09oV2gxaWFwa3F3RkNFSDZFS0V4dDZvblBlMzRJZUExbmR6RC8wZE0zUHJqYXhHenNOeWNsT2t0azdYRnY3M2F3VVc0WTNMUnJvWlBSY05FZUVjSFoyZlRzWTFxdmlaTVFDbUpRaWhXMXFsdDlQUDMwQ3pKRmw2WTh2N0tUMXhOY3pNM2RjN0pOY29OWDN0djBPRU9RNmJWYTB6WDdqNkU0M0Q2aTlPRGs3Z2luZ2MreGMxVWUzcC9hZCtrVjdRPS0tTC9ud2JHL2VmZ01SZ212VExkOUR1UT09--f7ac16236af2b93c7208238b9e465fcac31afe9c; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513236984; HttpOnly=true; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513236948; _gat=1',

    # zhanghuijuan
    #'Cookie':'aliyungf_tc=AQAAAMZqNR9u3gYALBIM0kt8GhMLqfSw; _helpdesksysteem_session=S0NkQjFrbW9FWUdQazRzNUlFKzdNTXJpbnM3NkNtNi83ZUU2TVpBRU1LMCsxaDVhUi9FRDQ2N2xHU015LzhkQkVDSWM3bERRN0p0RHBTM3lnNGVtTUJndkhRd3lBUGU3aFRQWmJJSDR6blo3dkFBUDluWVRjSkE4Rlp4RGFja3FiVDJpam5mdndMWmY5K3FnbjdURDFObDlkOEF4d3hZa2VQSVMzanhxeVFUQ1FWZC9GcjZPRHg3SWZzakZOM2xqNW91WFZ2dU9oK0NVUnM0OVFldU1SMC83YXR0OG5QcUUxR1hPVGd4SHFGSGtpb1FMc2xTOThaSkp5TC9ibVJIQUUvSlpFSE12Rko2bVEyRVpNcU50WkdKYmxpcUdhb1VqQ2NEVWYyaE9nTFJCenNkTVk2cGp4RlAxL1dwTDhpRk5WU1Q0U0l1ZTNGbkdzR2tIeDlMRXJzU1p0YzZuVE9hVmw1MkpLNzJ5VnFvPS0tRE9sN1ZPc0d2cDlnWXVJRitHVlB0QT09--3d56dcfffbba82325df42add4137370204e5641a; Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760,1513684335; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513763163; HttpOnly=true; _ga=GA1.2.794668574.1513762133; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220,1513759839; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513763101; _gat=1',

    # tangxiuxia
    #'Cookie':'aliyungf_tc=AQAAAMZqNR9u3gYALBIM0kt8GhMLqfSw; _helpdesksysteem_session=QVVNUkVmcUc4VmMvMnFFd1NORWpqeTJNZk5XVGJhb2liOHVGNlJzbDJxaVhxL2NSVGRKbFNBdktiek5sd0N2bnNQYU05QzFjOWZaL1lMb2NhVVNZODBpZis5cWJFaitGR01uUVg4VkN4cnpYckZtalh6N2V5ekt1eDhYSGdMVjBRMUdYb1JEWFY4cnlqRWVVMzBzWjZ2N0ZGcEJ1clNHQjk0Vi9VS0xxM0pFUGE4WDFMQ2dyOUFXbHNtVTY5c1M0MUFUcjFvamFQYmpPZFBvMEMzcHlsZm1QeGdHU1o1VkRmQzhneHMxRnl4M3pwa3ZWb1pDU3JWTVJjSkY0Zmw0V0xqUk1Dc1oyOXlScjN2SEpEeXN6N1JoL2s2R1UxZzY0L0NpdWlJSVprMVYwbndhaXlzRDhlNzBzdElPUmlKQTAyb2RJa1lGMjdrbHRwSEI4WWdPOFBMSzhhZDd4anRTWDhRaHBhSFFvUEJvPS0tYnZsMTRmek5NUkFMRGcydElnVnhkdz09--6f39abb21aa28e5ab663a454a3c61fc31679feba; Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760,1513684335; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513764586; HttpOnly=true; _ga=GA1.2.794668574.1513762133; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220,1513759839; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513764517; _gat=1',

    # liyuanfei
    'Cookie':'aliyungf_tc=AQAAAMZqNR9u3gYALBIM0kt8GhMLqfSw; _helpdesksysteem_session=ZmRHcGRHMG9Oa0JEdm1WZm4zd3FQWUR5VjBjYlZ0eGpZcnF2SVFMNnlVMVFORFFkRERUUk92czlMNjVZUFNLeUdVQnIyWnM4TzBQeld4T3BpMURMZFhnOGdzbVYxRlZzK3FjVmt6cFlqa2ljVE1DMFR0blBxOEV4aVB4dUdGOElFTE9xNzdJaHR0VDJQUy9uNkpUdHQ2OXBLT1NoajFEZUhMUlI2aVBxQ0RCSU9vKzhSY3FzYlhkckpJbHoxN0oxY0hjWVZlM04yelozbDU5M2RCZ3VhYkllbWJMT3dBUkdCUzhnaW0vTEZkWlYwSjdmM1liS1RXQXBRYkdvbkF3VVg4UHhYNy9uaWJsekE2N2pSMm45N0dBNjA1N3MveWhoN1JKcFBKMnkvaGdZdmc1Snd2eHQ1alFzVkNnNzcwWkRoUFJDWThKSXVCWEFZZDVIS0RQbnNXMVVzVW5PS296UVNRK0xLRk0vcyswPS0tbTVUU25STU5Qd0N5MEVRSXh1cUtzdz09--7790cf6472eaf175f11c9397bc01d0a938916373; Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760,1513684335; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513766105; HttpOnly=true; _ga=GA1.2.794668574.1513762133; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220,1513759839; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513766045; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}


# 请求指定客户的内容
def return_context(phone):
    url='http://www.duanrong.udesk.cn/spa1/callcenter_logs/list'
    postdata={
        'keyword': phone,
        # 'page': page
        # ,
         'all_conditions': [
        #     {
        #         'field_name': 'created_at',
        #         'operation': 'gte',
        #         "value": "2017-11-01 00:00:00"
        #     },
        #     {
        #         'field_name': 'created_at',
        #         'operation': 'lte',
        #         'value': '2017-11-01 23:59:59'
        #     },
             {
                 'field_name': 'relevant_agent_ids',
                 'operation': 'should',
                 # baihanqing
                 # 'value': '63212'

                 # zhanghuijuan
                 # 'value':'28171',

                 # tangxiuxia
                 'value': '63212'
             }
            ]
    }
    login_req=requests.post(url, headers=headers, data=json.dumps(postdata))
    return login_req.content.decode('utf8')


# 获取mp3下载链接
def return_download(content, url=None):
    if url is None:
        url={}
        try:
            data=json.loads(content)
        except Exception as e:
            return url
        len_2=len(data['items'])
        for i in range(len_2):
            url[data['items'][i]['call_log']['start_time']]=data['items'][i]['call_log']['sound_url']
        return url


# 获取APP_NO和CHECK_MOBILE
def return_phone_appno():
    print('连接到mysql服务器...')
    conn=pymysql.connect(host='localhost',
                         user='report_read',
                         password='0TsBs1D2XFt0kf',
                         db='rmpsdb',
                         port=3311,
                         charset='utf8'
                         )
    sql = "select ma.APP_NO,nci.CHECK_CONTENT CHECK_MOBILE,trace.OPERATOR_ID " \
        "from tm_main_apply ma left join tm_app_trace trace on ma.APP_NO = trace.APP_NO and trace.RTF_STATE in ('cashApplyReject', 'cashApplyPass') " \
        "inner join tm_nettel_check_info nci on ma.APP_NO = nci.APP_NO and nci.CHECK_RESULT_FLAG is not null " \
        "where ma.APP_TYPE = 'CashLoan' and trace.COMPLETE_TIME >= date_add(CURDATE(), interval -1000 day) " \
        "AND trace.COMPLETE_TIME < date_add(CURDATE(), interval +1 day) " \
        "AND trace.OPERATOR_ID in ('baihanqing@duanrong.com','zhuozheng@duanrong.com'," \
        "'baonan@duanrong.com','zhangxuesong@duanrong.com','lihaihua@duanrong.com','wangjiying@duanrong.com'," \
        "'liuyaru@duanrong.com','xumingfd@duanrong.com','zhangqiang1@duanrong.com','liyuanfei@duanrong.com'," \
        "'zhangyan4@duanrong.com','zhangpengtao@duanrong.com','admin','tqwadmin') " \
        "AND nci.CHECK_CONTENT <> '' order by trace.OPERATOR_ID,trace.COMPLETE_TIME asc"
    # and DATE(trace.COMPLETE_TIME) = \'%s\'
    # and trace.OPERATOR_ID in
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    # cursor.execute(sql % (run_date))
    cursor.execute(sql)
    row=cursor.fetchall()
    cursor.close()
    conn.close()
    return row


def return_schedule(a, b, c):
    per=100.0 * a * b / c
    if per > 100:
        per=100
    print('%.2f%%' % per)


if __name__ == '__main__':
    # 获取当前抓取日期
    # run_date = time.strftime("%Y-%m-%d", time.localtime())
    # rows = return_phone_appno(run_date)
    rows=return_phone_appno()
    # 遍历客户记录
    for r in range(len(rows)):
        app_no=rows[r]['APP_NO'].strip()
        check_mobile=re.sub(r'(-| )', '', rows[r]['CHECK_MOBILE'].strip())
        operator_id=rows[r]['OPERATOR_ID'].strip()
        print(app_no)
        print(check_mobile)
        print(operator_id)
        context=return_context(check_mobile)
        # print(context)
        # exit()
        url=return_download(context)
        # 判断url是否存在
        if url is None:
            continue
        else:
            print(url)
            for (k, v) in url.items():
                if v is not None:
                    k=k.replace(':', '-')
                    if os.path.exists('E:\\h\\%s\\%s\\' % (operator_id,app_no)):
                        print('已存在目录:E:\\h\\%s\\%s\\！！！' % (operator_id,app_no))
                        pass
                    else:
                        print('创建目录:E:\\h\\%s\\%s\\' % (operator_id,app_no))
                        os.makedirs('E:\\h\\%s\\%s\\' % (operator_id,app_no))
                    print('生成mp3文件：E:\\h\\' + str(operator_id) + '\\' + str(app_no) + '\\' + str(check_mobile) + '-' + k + '.mp3')
                    urllib.request.urlretrieve(str(v),
                                               'E:\\h\\' +str(operator_id) + '\\' + str(app_no) + '\\' + str(check_mobile) + '-' + k + '.mp3',
                                               return_schedule)
                    print('休眠3秒！')
                    print('3..')
                    time.sleep(1)
                    print('2..')
                    time.sleep(1)
                    print('1..')
                    time.sleep(1)