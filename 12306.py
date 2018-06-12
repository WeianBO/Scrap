#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'GonnaZero'

import requests
import re

def check():
    response = requests.get('https://kyfw.12306.cn/otn/'
                            'leftTicket/query?leftTicketDTO.train_date=2018-06-12&'
                            'leftTicketDTO.from_station=ZZF&leftTicketDTO.to_station=HZH&'
                            'purpose_codes=ADULT')
    result = response.json()
    #print(result['data']['result'])
    return result['data']['result']

'''
3 = 车次
23 = 软卧
26 = 硬座
28 = 硬卧
29 = 无座

'''

for m in check():
    tmp_list = m.split('|')
    # print(tmp_list)
    # n = 0
    # 查看查询信息在各自列表中的位置
    # for i in tmp_list:
    #     print(n,i)
    #     n += 1
    if tmp_list[23] != '无' and tmp_list[23] != '':
        print(tmp_list[3],"软卧有票")
    else:
        print(tmp_list[3],"软卧无票")




