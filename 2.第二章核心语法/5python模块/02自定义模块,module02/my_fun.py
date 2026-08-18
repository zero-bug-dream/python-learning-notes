# 常量(名称全大写)
# __all__指定from...import * 的功能(字符串形式)
__all__= ["log_sparator4","log_sparator1","PI"]
PI = 3.1415926
NAME = "童家豪"

# 函数
def log_sparator1():
    print("-" * 20)

def log_sparator2():
    print("+" * 20)

def log_sparator3():
    print("#" * 20)

def log_sparator4():
    print("*" * 20)

# 测试代码
# __name__:内置变量,当前模块名(如果直接运行该模块,__name__的值为__main__;模块被导入时,__name__值为模块名称,运行后边变成"my_fun")
# 执行当前文件,则会执行如下代码;如果被当模块导入,当前文件代码不执行(只在该文件执行,不影响导入模版使用)
print(__name__)
if __name__ == '__main__':
    log_sparator1()
    log_sparator2()
