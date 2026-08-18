# for 元素 in 数据集 :
# 循环体
# else:(可有可无)
#     循环结束,执行代码
lag = input("请输入需要遍历的字符串:")
for s in lag:
    print(f"元素:{s}")
print("循环结束")


# range语句range(4) =0 1 2 3     range(2,4) = 2 3   range(start1,end10,step3) = 1 4 7
# 案例1计算1-100间奇数之和
sum = 0
for i in range(1,101):
    if i %2 !=0:
        sum += i

print(f"1-100间奇数之和：{sum}")

# # 100-500间3的倍数的数字之和
# sum = 0
# for i in range(100,501):
#     if i % 3 == 0:
#         sum +=i
#
# print(f"100-500间3的倍数的数字之和为：{sum}")