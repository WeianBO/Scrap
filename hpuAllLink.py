from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import requests
import re

#定义两个空数组
inUrl = []
outUrl = []

#将外链接写入元组
def outLink(url):
    if url in outUrl:
        pass
    else:
        outUrl.append(url)
#将内链接写入元组
def inLink(url):
    url = re.sub("^/", "", url) # 使用正则表达式对数据或者字符串内容进行替换
    url = "http://www.hpu.edu.cn/" + url
    if url in inUrl:
        pass
    else:
        inUrl.append(url)
#读取数据表数据或者判断数据表数据是否为空 做哪项任务用参数judge决定
def lookUpSql(judge):
    sql = "select * from pages"
    try:
        cur.execute(sql)
        results = cur.fetchall()#获取数据表数据
        if judge:
            for row in results:
                print(row)
        else:
            return results
    except Exception as e:
        conn.rollback()
        print(e)
#向数据库中写入数据 写入内链接
def insertSql(inUrl):
    try:
        for i, m in enumerate(inUrl):
            sql = "insert into pages(id, title, content) values (\"%d\", \"%s\", \"%s\")" % (i, 'href', m)
            cur.execute(sql)
            conn.commit() #提交事件
    except Exception as e:
        conn.rollback()
        # print(e)


html = urlopen("http://www.hpu.edu.cn/www/index.html")
bsObj = BeautifulSoup(html, "html.parser")
bsObj = bsObj.findAll("a")
for link in bsObj:
    url = link.get('href')#.get('attribute')获取爬取数据的某一属性
    if 'http' not in url:
        inLink(url)
    else:
        outLink(url)

conn = pymysql.connect("localhost", "root", "373553636")
cur = conn.cursor()
cur.execute("use scraping")
row = lookUpSql(0)
if row == None:
    insertSql(inUrl)
else:
    sql = "delete from pages"
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    insertSql(inUrl)

lookUpSql(1)

conn.close()

# for i in outUrl:
#     print(i)
