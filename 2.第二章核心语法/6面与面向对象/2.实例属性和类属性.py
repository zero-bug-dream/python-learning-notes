class Car:
    # 类属性(实例对象共有数据)
    wheel = 4
    tax_rate= 0.1
    def __init__(self,c_brand,c_name,c_color,c_price):
        # 实例属性(实例对象特有的属性):self.属性名
        self.brand = c_brand
        self.name = c_name
        self.color = c_color
        self.price = c_price
        self.wheel = 6
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
print(c1.wheel) # 通过实例对象会先查找实例属性,之后才是类属性
print(Car.tax_rate)
print(Car.wheel)