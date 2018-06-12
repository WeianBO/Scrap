#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
__author__ = 'GonnaZero'

import requests
from selenium import webdriver
from multiprocessing import Pool
import re
import json


def get_one_page(url):
    web = webdriver.PhantomJS(executable_path='D:\PyFile\Tool\phantomjs\\bin\phantomjs.exe')
    web.get(url)
    html = web.page_source
    # print(html)
    # print(type(html))
    item = parse_one_page(html)
    for m in item:
        print(m)
        write_into_file(m)

def write_into_file(m):
    #使用utf-8格式保存到文件
    with open('D:/python/Zfile/maoyan.txt', 'a',encoding='utf-8') as f:
        f.write(json.dumps(m, ensure_ascii=False) + '\n')
        f.close()

def parse_one_page(html):
    pattern = re.compile('<dd>.*?index-.*?">(.*?)</i>.*?title="(.*?)" class.*?src="(.*?)" alt=.*?star">(.*?)</p>.*?time">'
'(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    item = re.findall(pattern, html)
    for m in item:
        #构建返回器，同时改编成字典格式
        yield{
            'rank':m[0],
            'name':m[1],
            'src':m[2],
            'actor':m[3].strip()[3:],
            'time':m[4].strip()[5:],
            'score':m[5] + m[6]
        }


def main(i):
    url = 'http://maoyan.com/board/4?offset=' + str(i)
    get_one_page(url)


if __name__ == "__main__":
    #调用多线程
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])