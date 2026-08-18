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
        self.__control_fuel() # 调用私有方法

    def stop(self):
        print(f'{self.brand }{self.model}停止驾驶...')

    def __control_fuel(self): #私有方法(只能内部访问)
        print(f'{self.brand }{self.model }正在控制燃油...')

    def get__owner(self): #公共方法调用私有属性
        return self.__owner[0:1] + '**'

    def charge(self):
        print(f'{self.brand } {self.model }正在补充燃料...')

# 继承(子类只能继承父类非私有的属性)
# 继承-重写:在子类
class FuelCar(Car):# 子类
    def charge(self):
        # super().charge() # 方式一:super().方法名()
        Car.charge(self) # 方式二:父类名.方法名(self)
        print(f'{self.brand} {self.model}正在加油...')

class ElectricCar(Car):
    def charge(self):
        super().charge() # 方式一:super().方法名()
        # Car.charge(self) # 方式二:父类名.方法名(self)
        print(f'{self.brand} {self.model}正在充电...')

if __name__ =='__main__':
    car1 = FuelCar('bmw','x5','red','张三')
    car2 = ElectricCar('Aodi','A6','black','李四')
    car1.charge()
    car2.charge()



