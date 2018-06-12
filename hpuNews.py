#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from urllib.request import urlopen
from urllib import error
from bs4 import BeautifulSoup
import requests
import re

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
pattern = re.compile('<a href=.+?id.*?>(.*?)</a>', re.S)#编译正则表达式成pattern对象 匹配（）中正则表达式所对应的内容
pattern2 = re.compile('<img .*?>')#
pattern3 = re.compile('<span .*?>.*?Blue;">')

try:
    html = requests.get("http://218.196.240.155/swfweb/hpugg.aspx", headers=header)#通过requests.get请求，获取公告页面内容，urlopen不知为何不能用
except error as e:
    print(e)
else:
    print(type(html.text))
    link = re.findall(pattern, html.text)#从html源码中获取公告内容
    print(type(link))
    link = str(link)
    link = re.sub(pattern3, "", link)#替换掉<span>标签内的杂余
    link = re.sub(pattern2, "", link)#替换掉<img>标签杂余
    news = re.sub("共第一页", "", link)
    print(news)


#爬取知乎某页面
# r = requests.get("https://www.zhihu.com/explore", headers=header)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# for new in titles:
#     print(new)










