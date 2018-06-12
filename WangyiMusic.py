# _*_ coding: utf-8 _*_

from pyecharts import Bar
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import requests
import json

url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_516076896?csrf_token=4079f419344d3f49ccdf146abf4d5c2a"
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
          "Host":"music.163.com",
          'Origin':'http://music.163.com',
          'Referer':'http://music.163.com/song?id=516076896'}
data = {"params":"0v77EpYbS8BgBZPD4m5ilvxhkMqVkmf7UFNoz0eYaAjhHtuhOAU1PDw6TH8RQPPxoox1zmYBi3yGieaceUucz1x0aswQpJfgNjDpWBNnJ652/mR2NREf0qNHZbE2bYzALvGD0ISaoM7Wka3KtfPd7opqdArS3DN1INKQNSwXhyDZnfD2c4tT1EA3i8mm88PRacIp6YkMLLCFobRQq6fCU39wcDfNu3dhE/m8snZAiqE=", "encSecKey":"6de27dd67dc63b38ef8fd2bf420a7e199e10230122e3a10dbbedc16a8648f1e7c8de0d4df6afa0d7cb9a84e9dbc80a0ebfe8e06a26f2d63f509c1b497a2db19eba359f819bbe4bed05dc07b0b6936ad570b12141f659712631baef3741d9051893fc9b0a712778f9fea4fa1e6f4287a56accca9162ada0e648d973915f4f86f7"}

try:
    html = requests.post(url, headers=header, data=data)
except Exception as e:
    print(e)
else:
    #post请求得到的是一个json数据，所以要用json.loads()解析一下数据
    data = json.loads(html.text)
    remark = []
    for hotcomment in data['hotComments']:
        items = {'nickName' : hotcomment['user']['nickname'],
                 'content' : hotcomment['content'],
                 'likedCount' : hotcomment['likedCount']
                 }
        remark.append(items)
    nick_name = [content['nickName'] for content in remark]
    content_list = [content['content'] for content in remark]
    liked_count = [content['likedCount'] for content in remark]

#使用pyecharts 模块生成一个图表
bar = Bar("热评中点赞数示例图")
#.add()主要方法，用于添加图表的数据和设置各种配置项
bar.add("点赞数", nick_name, liked_count, is_stack=True, mark_line=["min", "max"], mark_point=["average"])
#.render()默认将会在根目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:my_first_chart.html")，文件用浏览器打开。
bar.render()

#使用wordcloud模块绘制词云图，并用matplotlib可视化

content_text = " ".join(content_list)#str.join(squence) 方法用于将序列str中的元素以指定的字符squence连接生成一个新的字符串

#设置词云图的各项参数
wordcloud = WordCloud(font_path=r"dragon.otf", max_words=200).generate(content_text)
plt.figure()#figure函数，创建图表
#显示图像
plt.imshow(wordcloud, interpolation='bilinear')
# 关掉图像的坐标
plt.axis('off')
plt.show()