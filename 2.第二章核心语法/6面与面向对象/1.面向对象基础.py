# # 定义类(类名命名方式大驼峰式命名(不用_),如UserCount,GoodPrice...)
# class Car:
#     pass
#
# # 创建对象
# c1 = Car()
# # 动态传参(不推荐,因为传参太随便了想加几个属性就加几个)
# c1.price = 100
# c1.brand = "理想"
#
# print(c1.__dict__) # 将c1属性值以字典的形式输出

# def在类定义外为函数表示,在类内为方法表示(某种意义上来说函数也算一个方式)
# def __init__(self,参数列表):(这就规划参数的数量与类型,没有动态传参那么乱)下一行缩进self.参数名= 赋值
"""
class Car:
    def __init__(self,c_brand,c_name,c_pirce):# __init__初始化方法:对象创建时自动调用,用于为对象设置对应属性(形参列表),如brand,name...
        self.brand = c_brand                  # self:方法的第一个参数,表示当前创建的实例对象(模版名),self.属性名 = 实参
        self.name = c_name
        self.pirce = c_pirce
        print("Car 初始化完毕,对象属性已添加")
# 创建对象
c1 = Car("BMW","理想",100000)
print(c1.__dict__)
"""


# 设一个汽车比亚迪秦(brand,name,color,price)正在行驶系统和提车价格(discount,rate)
class Car:
    def __init__(self,c_brand,c_name,c_color,c_price):
        self.brand = c_brand
        self.name = c_name
        self.color = c_color
        self.price = c_price
        print("Car 初始化完毕,对象属性已添加")

    def runing(self):
        print(f" {self.brand},{self.name}正在行驶中,行驶了....")

    def total_cost(self,discount,rate,express = 0):
        """
        计算根据(discount,rate,express)
        :param discount: 折扣
        :param rate: 税率
        :param express: 运费
        :return: 提车价格
        """
        total_cost = self.price * discount + self.price * rate + express
        return total_cost


c1 = Car("比亚迪","秦","白",100000)

print(c1.__dict__)

c1.runing()

total1 = c1.total_cost(0.85,0.1,100)
print("提车价格为:",total1)

total2 = c1.total_cost(0.85,0.1)
print(f"提车价格为:{total2}")