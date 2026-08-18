# 网页解析:获取所需要的HTML数据 1
# lxml:HTML和XML解析库,便于获取所需HTML数据 (第三方库:pip install lxml)
from lxml import html

# 读取html文件
with open("resources/角色档案.html", "r", encoding="utf-8") as f:
    html_data = f.read()
    # 解析HTML的文本,将其转换成一个文档对象
    document = html.fromstring(html_data)

    # 解析表头 - xpath语法
    # td_list = document.xpath("/html/body/div/div/table/tr[3]/td/text()")
    # td_list = document.xpath("//table/tr[3]/td/text()")
    td_list = document.xpath("//table/tr[last()-1]/td/text()")
    print(td_list)

    th_list = document.xpath("//table/tr/th/text()")
    print(th_list)
    # 获取所有行数据
    # xpath语法作用:准确定位文档中所需内容
    # tr_list = document.xpath("//table/tr") # "//":从任意位置查找
    # for tr in tr_list:
    #     td_list = tr.xpath("./td/text()") # "/":从根节点一级一级的查找元素 ".":从当前节点(继续上个节点)下查找
    #     print(td_list)

    # [n]:索引从1开始
    # [last()]:选最后一个元素 --- //p[lasr()]



    # text() :获取文本内容

    # p_list = document.xpath("//p/text()")
    # print(p_list)

    # [@attr]:选择该属性元素 --- //p[@color]
    # p_list = document.xpath("//p[@class]/text()")
    # print(p_list)

    # [@attr = "value"] : 选择该属性为指定值的元素  ---// p[@color = 'red']
    p_list = document.xpath("//p[@class = 'xn']/text()")
    print(p_list)

    # * :匹配任意元素节点
    th_list = document.xpath("//table/tr/*/text()")
    print(th_list)

    # @* :匹配元素的任意属性 (@xxx):匹配元素的任意xxx属性
    s_list = document.xpath("//img/@*")
    print(s_list)
    a_list = document.xpath("//img/@src")
    print(a_list)