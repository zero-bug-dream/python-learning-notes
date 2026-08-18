# input 语句函数 s=input()字符串类型数据                    print( )
name = input("请输入您的名称:")
print(f" {name} 是卡卡罗的狗")

age = input( "请输入您的年龄:")
print(f"恭喜您今年{age}岁了!")


total=1000
# 输入密码
password = input(f" 请输入您的密码: ")
print(f"密码正确,{password}")

# 输入取款金额
num = input(f"请输入取款金额:")
a = total - int(num) # num是str类型要转为int


# 计算余额并输出
print(f"取款后余额为{a}")