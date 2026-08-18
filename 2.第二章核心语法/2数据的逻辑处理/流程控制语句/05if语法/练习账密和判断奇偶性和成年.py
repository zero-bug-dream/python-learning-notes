# # 判断输入数字奇偶性
# num = int(input("输入一个数字:"))
# if num %2 ==0:
#     print(f"{num}是偶数")
# else:
#     print("f{num}是奇数")

# # 判断输入年龄是否成年
# age = int(input("请输入您的年龄:"))
# if age >= 18:
#     print(f"{age}岁已经成年")
# else:
#     print(f"{age}岁未成年")

# # 判断输入值正负,考虑0 {if进阶:if...elif...else}
# # if 条件1:
# #     操作1
# # elif 条件2
# #     操作2
# #......
# # else
# # 以上条件都不成立的结果
# a = int(input("请输入一个数:"))
# if a > 0:
#     print(f"{a}是正数")
# elif a < 0:
#     print(f"{a}是负数")
# else :
#     print(f"{a}是0")

# 登录系统 123456/666888 root/111222 zhangsan/123060(账密是字符串比较)
account = input("请输入您的账号:")
password = input("请输入您的密码:")

if account == "123456" and password == "666888":
    print("登陆成功")
elif account == "root" and password == "111222":
    print("登陆成功")
elif account == "zhangsan" and password == "123060":
    print("登陆成功")
else:
    print("登录失败,用户名或密码错误")