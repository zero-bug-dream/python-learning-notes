# # 变量作用范围(定义域)
# # 函数外部定义的变量是全局变量(内外皆可访问),则内部为局部变量(只能函数内部访问)
# # global 可以在函数内修改全局变量(先声明,在使用)
a = 10 # a:全局变量
b = 100
def circle_area(r):
    global b
    b = 1
    area = 3.14 * r **2 #r,area局部变量\
    a = 10000
    print(a)
    return area

circle_area = circle_area(10)
print(circle_area)
print(a) # 外部无法访问内部的a
print(b)

# # 传参方式
# def reg_stu(name,age,gender,city = "江苏" ):# 默认参数,只在后面
#     print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
#     return {"name":name, "age":age,"gender": gender,"city": city}
#
# stu = reg_stu("张三",18,"男","江苏")# 位置传参(一一对应)5
# print(stu)
#
# stu1 = reg_stu(name = "姜磊",age = 12,gender = "女",city = "西藏" )# 关键字传参
# print(stu1)
#
# stu1 = reg_stu(city = "西藏",age = 12,name = "姜磊",gender = "女", )
# print(stu1)
#
# stu2 = reg_stu("小丑",250,city = "火星",gender = "人妖" )# 位置传参+关键字传参,位置在前,关键字在后
# print(stu2)
#
# stu1 = reg_stu("何以",21,"男") #默认参数
# print(stu1)
#
# # 不定长参数 位置传参不定长:def calc_date(*args):
# *args:是指一个列表
# def calc_date (*args):
#     min_date = min(*args)
#     max_date = max(*args)
#     avg_date = sum(args)/len(args)
#     return min_date,max_date,round(avg_date,1)
# calc_date(12,13,34,467,65,23,1,0)
# print(calc_date(12,13,34,467,65,23,1,0))
#
# print(calc_date(12,13,34,467,65,23,1,0,111,222,333,555,666))

# 关键字传参不定长:def calc_date(**kwarges):
# *kwarges 关键字不定长
def calc_date (*args,**kwargs):
    print(args)
    print(kwargs)
    min_date = min(*args)
    max_date = max(*args)
    avg_date = sum(args)/len(args)
    if kwargs.get("round") is not None:
        avg_date = round(avg_date,kwargs.get("round"))

    if kwargs.get("print") :
        print(f"最小值:{min_date},最大值:{max_date},平均值:{avg_date}")
    return min_date,max_date,avg_date

print(calc_date(12,13,34,467.4,65,23,1,0,111,213,round = 1,print = True))

