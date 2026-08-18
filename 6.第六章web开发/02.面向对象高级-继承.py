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

# 继承(子类只能继承父类非私有的属性)
class FuelCar(Car):# 子类
    pass

class ElectricCar(Car):
    pass

if __name__ =='__main__':
    car1 = FuelCar('bmw','x5','red','张三')
    car2 = ElectricCar('tesla','model s','black','李四')
    car1.run()
    car1.stop()
    print(car1.get__owner())
    print(car1.color)


