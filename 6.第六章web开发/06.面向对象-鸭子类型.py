class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳...")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳...")


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f"{self.age}岁的{self.name}正在游泳...")

def go_swimming(duck):
    duck.swimming()

if __name__ == '__main__': # Python多态不依赖继承体系
    go_swimming(Duck('小黑',2))
    go_swimming(Pig('佩奇',5))
    go_swimming(Duck('小黄',4))
