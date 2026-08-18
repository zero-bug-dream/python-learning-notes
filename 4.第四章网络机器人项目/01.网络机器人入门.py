# 爬虫:网络爬虫(网络机器人),按一定规则,自动浏览抓取网络资源的程序或脚本
# 流程:开始---发送http请求---解析和提取数据---数据清洗---数据存储---http请求---结束
# 数据清洗:爬虫获取的数据进行清洗,过滤,转换成需要的数据格式,目的是让数据符合要求

# robots协议: 爬虫协议,用于限制爬虫行为,(君子协议) 域名后加/roborts.txt

# 入门:获取TIOBE榜单
"""
1.查看该网站的君子协议
2.安装requests库(pip install requests)
3.编写Python,访问该网站,获取数据
"""
import requests

# 1.定义URL
goal_url = "https://www.tiobe.com/tiobe-index/"

# 2.发送请求,获取数据
response = requests.get(goal_url)

# 一个网页由三个部分组成:HTML,CSS,JS(JavaScript)
# HTML:超文本标记语言,每个标签都有各种作用名字固定的,负责网页的结构(<p>开始标签...</p>结束标签) <a href="(属性)">超链接</a>
# CSS:层叠样式表,负责网页的样式
# JS:脚本语言,负责网页的动态效果(交互效果)

# 3.输出
print(response.text)