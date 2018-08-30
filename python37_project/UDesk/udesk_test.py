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
    'Cookie': 'Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760,1513684335; _ga=GA1.2.1676670225.1512370465; Qs_lvt_102458=1512371267; Qs_pv_102458=2510706366026374000; Hm_lvt_85cdbdd6ba7f014cd503e9f1cd5e5ba0=1512371267; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220; aliyungf_tc=AQAAAPzEyHQVeAwALBIM0rWJCDK3pJaF; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513755355; HttpOnly=true; _helpdesksysteem_session=aUxUVDR5UGltRDZZUUhrMm8yd0hNanh2ZWRJM2ZXU0lDTkcyOXFMSWFlVFBNdXE3ekJwVVdHQlBKVkI3aHFWVnRxdEduM3hsRDhBTG9OQjI0V2NjNG9CUnZWOWFyNi9odnVhaEV4ZEk4YkFwOWpUazc3UlZmWmdxNFlMMzBvTXRNY2xTcGNnSGdCeEVVdHh6Um5MclVVZ3oybTFuR25oUTVjRGRmMEg4U2pDUWpWWHE5SzE1Vlg2a0hweVIwNzJ5SmN3OVN5elkrMmVaSjZZNmdkamYrcGxMUWF6bnJEdWZFdnhpN2FJbzFzdGxXU3NoQTJIMWxKazNrRlByZ29vTmI0KzhqcEVlblYrWmJiclg1RHl5U1d5UWc1UHdyY0FOL1I4Q0g4RGE3Ny82VGx5dUxsUkJlRkdscmpSMHM4YnhHNlZwMjV0ek9wRVNRUGwzdWtRYjZXTGZIMGZOQlhOOGd5WEIvUmFHTmFXQWRISWFYWHJmSkhnTFRKZGNvRVg1bDJFQ2xUMGR4VUFkeWNGaUdlMVFIcjFFZ040UUV4L0YrZkoweWQvT3VVRkJOTmZiV0pzeG45S2Q1bUJScG42RVVyM0ZQdysyY3BseTgyREdNZ25VVWc9PS0tZkFDakZIRkdMWXBiT29XTnY3UVdtdz09--4210f91bc95bcf7324c852f081e6ef60930d96c0; _gat=1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
}


# 请求指定客户的内容
def return_context(phone):
    url='http://www.duanrong.udesk.cn/spa1/callcenter_logs/list'
    postdata={
        'keyword': phone,
        # 'page': page
        # ,
        # 'all_conditions': [
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
        #     {
        #         'field_name': 'relevant_agent_ids',
        #         'operation': 'should',
        #         'value': '63212'
        #     }
        #    ]
    }
    login_req=requests.post(url, headers=headers, data=json.dumps(postdata))
    return login_req.content.decode('utf8')


# 获取mp3下载链接
def return_download(content, url=None):
    if url is None:
        url={}
        data=json.loads(content)
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
        "AND nci.CHECK_CONTENT <> '' order by trace.COMPLETE_TIME asc"
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
        app_no=rows[r]['APP_NO'].strip
        check_mobile=re.sub(r'(-| )', '', rows[r]['CHECK_MOBILE'])
        operator_id=rows[r]['OPERATOR_ID']#.replace('.','_')
        print(app_no)
        print(check_mobile)
        print(operator_id)
        context=return_context(check_mobile)
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