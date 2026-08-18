# 函数定义:标识符命名规则
def _out():
    print("---------------------------------")
    print("---------------------------------")

# 调用函数:要调用才执行



# 函数参数与返回值
# 函数1:计算圆的面积
def circle_area(r):
    area = 3.14 * r **2
    return area

circle_area = circle_area(10)
print(circle_area)
_out()
# 函数2:计算长方形面积
def rectangle(a,b):# a,b是形参
    """
    根据长方形的长宽计算其面积
    :param a: 长
    :param b: 宽
    :return: 面积
    """
    area = a * b
    return area
# help(rectangle)

rectangle_area = rectangle(20,10)# 20,10是实参,一一对应
print(rectangle_area)

# 函数3：计算圆的面积和周长
def circle_area_len(r) :
# 函数说明文档“”“函数功能，参数及返回值”“”
    """
    根据圆的半径计算其面积和周长
:param r: 圆的半径
:return: 圆的面积,圆的周长
"""

    return round(3.14 * r **2,1), round(2 * 3.14 *r,1)
al = circle_area_len(10)
print(al)
print(type(al))

_out()
area,len = circle_area_len(10)
print(area)
print(len)

