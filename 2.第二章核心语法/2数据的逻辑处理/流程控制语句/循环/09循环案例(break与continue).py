"""
whlie循环不知道循环次数,直到到达条件
for循环知道循环次数,字符串遍历
break 只能出现在循环中,表示结束或者跳出循环 whlie后的else代码不用执行,print就结束
continue  也只能在循环中,表示中断本次循环,直接进入下一次循环,重新循环

案例1
正确账密123456/666888 123060/111222 zhangsan/123456
登录系统
输入账密不能空
"""
while True:
    account = input("请输入您的账号:")
    password = input("请输入您的密码:")
    if account == ""or password == "":
        print("输入账密不能为空")
        continue

    if account == "123456" and password == "666888" :
        print("登录成功")
        break
    elif account == "123060" and password == "111222" :
        print("登录成功")
        break
    elif account == "zhangsan" and password == "123456" :
        print("登录成功")
        break
    else:
        print("登录失败,请输入正确账密!")



