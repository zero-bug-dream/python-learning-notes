def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def pow(x,y):
    return x**y

def calc(x,y,oper):# 实参可以调用函数
    return oper(x,y)

print(calc(10,20,add))

def calc(x,y,z):
    return z(x,y)
print(calc(10,20,div))