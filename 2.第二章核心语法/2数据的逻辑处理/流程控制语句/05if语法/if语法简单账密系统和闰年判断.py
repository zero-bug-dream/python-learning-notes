# # if条件判断
# # if 判断条件 :   输出布尔值
# #    条件成交,才执行操作 归属if语句操作语句开头要缩进4格tab
# score = 42
# if score > 332:
#     print("欢迎您来察高读书")
#     print("也恭喜你有一个美好的未来")
# print("---------------------")
#
# # 案例输入账密登录(账密为18888888888/666888)
# ok_account ="123456" #不加""这是输入整形
# ok_password ="666888"#加""变为字符串对比
# # 1接收输入的账密
# account = input("请输入您的账号:") #input永远是输入字符串
# password = input("请输入您的密码:")
# # 2判断账密是否正确,如果都正确,则登录成功
# if account == ok_account and password == ok_password:
#     print("登陆成功,进入b站")
#
# # 3判断账密是否错误,如果错误,则登录失败,提示错误信息
# if account != ok_account or password != ok_password:
#     print("登录失败")

# # if语句进阶 else
# # if 判断条件
# #    条件成立,操作1
# # else:
# #    条件不成立,操作2
#
# # 案例输入账密登录(账密为18888888888/666888)
# ok_account ="123456" #不加""这是输入整形
# ok_password ="666888"#加""变为字符串对比
#
# # 1接收输入的账密
# account = input("请输入您的账号:") #input永远是输入字符串
# password = input("请输入您的密码:")
#
# # 2判断账密是否正确,如果都正确,则登录成功
# if account == ok_account and password == ok_password:
#     print("登陆成功,进入b站")
#
# # 3判断账密是否错误,如果错误,则登录失败,提示错误信息
# else:
#     print("登录失败")

# 输入年份判断闰年还是平年:非整百年整除4,整百年整除400
year = int(input("请输入年份:")) # 字符串转整形,方便后面赋值运算
if (year % 100 != 0 and year % 4 ==0) or ( year % 100 == 0 and year % 400 ==0) :
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")