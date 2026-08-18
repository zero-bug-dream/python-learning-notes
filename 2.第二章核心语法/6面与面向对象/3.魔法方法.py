# 魔法方法通常以双下划线开头和结尾的
# 如__init__,__str__,__eq__(equal),__lt__(less than),__le__(less than or equal:<=),__gt__(greater than),__ge__(>=)
# 不需要我们手动调用,Python自动调用
class Car:
    def __init__(self,c_brand,c_name,c_color,c_price):
        self.brand = c_brand
        self.name = c_name
        self.color = c_color
        self.price = c_price
        print("Car 初始化完毕,对象属性已添加")

    def runing(self):
        print(f" {self.brand},{self.name}正在行驶中,行驶了....")
#     魔法方法
#     def __str__(self):
#         return f" {self.brand}#{self.name}#{self.color}#{self.price}"

    def __eq__(self, other):
        return self.brand == other.brand and self.name == other.name and self.color == other.color

    def __lt__(self, other):
        return self.price < other.price


# 测试
c1 = Car("比亚迪","秦","白",100000)

c2 = Car("宝马","x80","黑",800000)

c3 = Car("宝马","x80","黑",800000)
print(c1) #没有__str__,结果会是<__main__.Car object at 0x0000026C61C00590>(内存地址)
print(c2)
print(c3)
print(c1 == c2)
print(c1 > c2)
print(c2 == c3)
