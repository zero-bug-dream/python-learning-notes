# # # 存邮箱,和列表差不多,有序 s = "..."
# # s = "python-1231"
# # print(s[0:11:2]) # 切片
# # print("-------------------------")
# # print(s[-1:3:-1]) # 反向
# # print(s[::-1]) # 翻转
# #
# # 常用方法
#
# s = "     hello-python-hello-mingchao     "
#
# x = s.find("-") # 查第一次出现的位置
# print(x)
# print("---------------------")
#
# x1 = s.count("h") # 查出现次数
# print(x1)
# print("---------------------")
#
# x2 = s.upper()# 大写
# print(x2)
# print("----------------------")
#
# x3 = s.lower()# 小写
# print(x3)
# print("----------------------")
#
# slist = s.split("-") #切割分装到列表
# print(slist)
# print("----------------------")
#
# x4 = s.strip()# 去两端空格
# print(x4)
# print("----------------------")
#
# sr = s.replace("-","_") #顾名思义
# print(sr)
# print("----------------------")
#
# print(s.startswith("hello")) #是否开头
# print(s.endswith("hello"))
# print("—————————————————————")
# print(s)

# 案例 邮箱系统（要求至少一个.和只能一个@)
mail = input("请输入一个邮箱:")
if mail.count("@") == 1 and "." in mail : # mail.count(".") >= 1
    print(f"{mail}是合法邮箱")
else:
    print(f"{mail}不是合法邮箱")
