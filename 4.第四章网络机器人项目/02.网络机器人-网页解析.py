import requests
from lxml import html

# 1.定义URL
goal_url = "https://www.tiobe.com/tiobe-index/"

# 2.发送请求
response = requests.get(goal_url)

# 3.输出数据至控制台
document = html.fromstring(response.text) # 字符串转换成文档对象

# 4.解析数据
# 解析表头
# th_list = document.xpath("//table[@id = 'top20']/thead/tr/th/text()")
th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析表格
# td_list = document.xpath("//tbody/tr/td/text()") 全在一行不美观
# print(td_list)

tr_list = document.xpath("//table[@id = 'top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)





