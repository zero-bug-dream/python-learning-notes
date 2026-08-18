"""
多继承:一个子类继承多个父类
"""
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

# 华为智能驾驶
class huweiAiDriving:
    def __init__(self,version = 'v 1.0'):
        self.version = version

    def run(self):
        print(f"使用华为智能驾驶系统{self.version}正在行驶...")

# 问界汽车 MRO(Method Resolution Order)方法解析顺序 类名.__mro__ 属性 / 类名.mro()
class wenjieCar(Car,huweiAiDriving): # 继承多个父类
    pass

# 智界汽车
class zhijieCar(Car,huweiAiDriving):
    def __init__(self,brand,model,color,owner,version):
        Car.__init__(self,brand,model,color,owner) # 类名.方法名(self)
        # super().__init__(version)
        huweiAiDriving.__init__(self,version)
    def run(self):
        Car.run(self)
        huweiAiDriving.run(self)

if __name__ == '__main__':
    c = wenjieCar('bmw','x5','黑色','小明')
    c2 = zhijieCar('智界','s9','白色','小红','v 1.0')
    print(wenjieCar.mro())
    c2.run()