"""
猜数字游戏
系统给一个随机数 random .randint
猜错提供猜大量还是小了
直至猜对
"""
# import random
# random_num = random.randint(1, 100)
# num = int(input("请输入一个数字："))
# if num >= random_num:
#     print("您输入的数字猜大了")
# elif num <= random_num:
#     print("您输入的数字猜小了")
# else:
#     print("恭喜您猜对了！！！")
# print(f"随机生成的数字是：{random_num}")

import random
random_num = random.randint(1,100)
while True:
    num = int(input("请输入一个整数(1到100之间）:"))
    if num > random_num:
        print("您输入的数字猜大了")
    elif num < random_num:
        print("您输入的数字猜小了")
    else:
        print("恭喜您猜对了!!!")
        break
print(f"您输入的数为:{random_num}")


