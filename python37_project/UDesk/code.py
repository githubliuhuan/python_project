#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib
import urllib.request as ur
import requests
import json

headers = {
    #'Cookie': 'HttpOnly=true; HttpOnly=true; _ga=GA1.2.1306759940.1512978049; aliyungf_tc=AQAAAPCt4yQZ7gUALBIM0paJXCtcm65o; Hm_lvt_04a130f55f93916ac7fabec664481931=1512977989,1513045542,1513045576; HttpOnly=true; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512991963,1513046031; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513147451; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513147457; _ga=GA1.3.1306759940.1512978049; _helpdesksysteem_session=dlJYdVFHSEduOFNSZlFHekpSYXozVUM5dWFBOHlyS2VWZkpZWWxtMHdKUnlKQ3E1UU4xcmZ3UUY2L0tzWmh4S0pBc1RaYXIvVTVTbW9rZTJjMUJWalVLdXUvZnkvclkvUms1MDJkRjZDNkhZWGFSMHliUUkyREkxRHlhMHpKcmpnUUo2cUZpaWJ3TVdmUkZaeUVreEhOc242QWRmbFVXTkpHaGo0N09hdW1rZ3BTSlhCUEZSYU5Bakd0anZlRzRHRFU3R3RXbFlxZlg2RFh4UnpHS3NEMXppVmZWdm9rc2VUSnhRWXVyWWpHL0JNbXhnZGUrL3lDQ2NaU0ZqYWtaSEhKY0tPNEtiTVRBbkFlQWVrWnZ1V1RMeTFIVy9SZFd0U29rZlpaeTgrSytpUFRtQVRDOHFsK1E4aHlWRStDQXZZVUtjSWZLOTFZL3Q4STJQYjZ4bFBrVUdhdWFxN3YwMmRKSG9OKzJucmpzPS0tdUFBQ3RTRThEZXRoNFRSd1RXM0VDdz09--f39c757060c9510322d089fc57b7d48c5a79d4d9',
    '(Request-Line)':'GET /collect?v=1&_v=j47&a=1878841533&t=pageview&_s=17&dl=http%3A%2F%2Fwww.duanrong.udesk.cn%2Fentry%2F&dp=%2Fcall%3Fstart_date%3D2017-12-01%252000%253A00%253A00&ul=zh-cn&de=UTF-8&dt=%E5%9C%A8%E7%BA%BF%E5%AE%A2%E6%9C%8D%E7%B3%BB%E7%BB%9F&sd=24-bit&sr=1920x1080&vp=1920x403&je=0&fl=27.0%20r0&_u=CACAAEABI~&jid=&cid=1676670225.1512370465&tid=UA-69864074-3&z=1593756468 HTTP/1.1',
    # 'Cookie': 'HttpOnly=true; Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760; _ga=GA1.2.1676670225.1512370465; Qs_lvt_102458=1512371267; Qs_pv_102458=2510706366026374000; Hm_lvt_85cdbdd6ba7f014cd503e9f1cd5e5ba0=1512371267; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220; aliyungf_tc=AQAAAAj1axqKLgIALBIM0hz/fufQ5gRy; _helpdesksysteem_session=cjRmNzViU0wyTHN1WVJDbzRFcklUcHd3SFB6Qy9aUGp4YTRpK0lRcGE3VzcvcDd4aklKa09TcGh4NHVQWEsyekhaaXZFVXBrRXVrOGppc1J5eEI1SHJwRDVoMXBuQ1hiaXdMUGZFMXUrUVc5Z0c2U0VTd0xDdE01QlNCRGNxQ3YzdUE4UUtEYkRVY2MzdTRtVDRoY1dHZmRWUFFKRDhCREhIa2V5OGxZY2ErYlV3U1ZhcWs5NVI4UFRNMURscXNYTElNRGVUNmNqVXRhUGh0YUdUZjAxWkJxeEVlOHB4a3gwQndEdHZkRE5naXFvU2I2aDBVc1BNNlJqdHRwT0RWbWtVWG94Q1JpTXA5Rml1NCttQ0lsRXlNdkhBSWhSVXBjSGhFemFqTXRQZGpWdHZNcTZaODhqOFZvMnJHUXdrRlU4Z3NYMHZqZWpNdWh2NDFHS2I3WkZ6RzVyVGJkNURFcFhUU1BoL2VDbGlNPS0tQk03alpVb0d2NS9DVzF5WGF4VkRFdz09--388fe4dc73fe7e390d4271d1054877715181e626; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513231695; HttpOnly=true; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513231678; _gat=1',
    'Cookie': 'Hm_lvt_04a130f55f93916ac7fabec664481931=1512370273,1512976760; _ga=GA1.2.1676670225.1512370465; Qs_lvt_102458=1512371267; Qs_pv_102458=2510706366026374000; Hm_lvt_85cdbdd6ba7f014cd503e9f1cd5e5ba0=1512371267; Hm_lvt_a7ba95c0fb44cd5f20314f1bcd41861f=1512371684,1513223220; aliyungf_tc=AQAAAAj1axqKLgIALBIM0hz/fufQ5gRy; _helpdesksysteem_session=ZHgzYTArbmdjbEVwUVFka0dnWDd5ZkdtMXZnc1RwVEtyK3hhTU1zTGFaZXRYUXE3QnJzYU92NW9YSGk4a0ZxVU5SWUFraFgzU2hRaWF5ZDJIT2E2R3JkeDBqSHhpZDRNM1RxTXV1bmYzVWpUeUtBZThVNTBIRnFwYVVDR3NNSjVGbGZMNGVldkR4VWNRTW55eXdKeUFUUjhUYkU5NnduOGp1UlNUZThKcGtnM09oV2gxaWFwa3F3RkNFSDZFS0V4dDZvblBlMzRJZUExbmR6RC8wZE0zUHJqYXhHenNOeWNsT2t0azdYRnY3M2F3VVc0WTNMUnJvWlBSY05FZUVjSFoyZlRzWTFxdmlaTVFDbUpRaWhXMXFsdDlQUDMwQ3pKRmw2WTh2N0tUMXhOY3pNM2RjN0pOY29OWDN0djBPRU9RNmJWYTB6WDdqNkU0M0Q2aTlPRGs3Z2luZ2MreGMxVWUzcC9hZCtrVjdRPS0tTC9ud2JHL2VmZ01SZ212VExkOUR1UT09--f7ac16236af2b93c7208238b9e465fcac31afe9c; Hm_lpvt_04a130f55f93916ac7fabec664481931=1513236984; HttpOnly=true; Hm_lpvt_a7ba95c0fb44cd5f20314f1bcd41861f=1513236948; _gat=1',
     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    'Referer':'http://www.duanrong.udesk.cn/entry/call?end_date=2017-12-01%2023%3A59%3A59&start_date=2017-11-01%2000%3A00%3A00'
}


def Login():
    # login_url = 'http://www.duanrong.udesk.cn/users/sign_in'
    #
    # request = ur.Request(login_url, headers=headers)
    # response = ur.urlopen(request)

    url = 'http://www.duanrong.udesk.cn/spa1/callcenter_logs/list'
    data = {"username": "baihanqin@duanrong.com", "password": "duan123456"}
    login_req = requests.post(url, headers=headers,data= data)
    # login_resp = ur.urlopen(login_req, timeout=5)

    return login_req.content

data = json.loads(Login())
print(data)
len_1 = len(data)
len_2 = len(data['items'])
for i in range(len_2):
    print(data['items'][i]['call_log']['sound_url'])
exit()





# with open('E:\\h\\res.txt', 'w') as t:
#     t.write(str(Login()))
#
# data=open("E:\\h\\res.txt",'r',encoding='utf8')
#
# for line in data:
#     line=line.replace('{"customer"', '\r\n')
#
# with open('E:\\h\\data.txt', 'w') as t:
#     t.write(line)
#
# link=open("E:\\h\\data.txt",'r',encoding='utf8')
#
# #with open('E:\\h\\data.txt', 'w') as t:
# for line in link:
#     start1=line.find('"sound_url":')
#     end1 = line.find(',"asr_result"')
#     start2 = line.find('"name":')
#     end2= line.find(',"phone"')
#     if start1 >= 0:
#         print(line)
#         print(start1,end1,start2,end2)
#         start1 += len('"sound_url":')
#         print(len('"sound_url":'))
#         print('start1:'+ str(start1))
#         src=line[start1:end1].strip()
#         print(src)
#         name=line[start2:end2].strip()
#         print(name)
#         if src=='null':
#             continue
#         else:
#             src1 = src.replace('"', '')
#             name = name.replace('"', '')
#             print(src1)
#             print(name)
#             exit()
#         urllib.request.urlretrieve(src1, 'E:\\h\\'+'111'+'.mp3')
