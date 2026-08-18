# 多态:指同一个方法,具有不同形态

class Car:# 默认父类(object)
    def __init__(self,brand,model,color,owner):
        self.brand = brand # 品牌
        self.model = model #型号
        self.color = color #颜色
        self.__owner = owner #所有者(私有属性)


    def start(self):
        print(f'{self.brand}{self.model }正在启动...')

    def run(self):
        print(f'{self.__owner }驾驶{self.brand }{self.model }正在行驶...')


    def stop(self):
        print(f'{self.brand }{self.model}停止驾驶...')


    def get__owner(self): #公共方法调用私有属性
        return self.__owner[0:1] + '**'

    def charge(self):
        print(f'{self.brand } {self.model }正在补充燃料...')

class FuelCar(Car):# 子类
    def charge(self):
        print(f'{self.brand} {self.model}正在加油...')

class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model}正在充电...')

def handle_charge(car:Car): # 函数参数类型声明 ---父类型(有所有子类的方法)
    car.charge()


if __name__ == '__main__':
    handle_charge(FuelCar('bmw','x5','黑色','小明'))
    handle_charge(ElectricCar('audi','a8','黑色','张三'))

