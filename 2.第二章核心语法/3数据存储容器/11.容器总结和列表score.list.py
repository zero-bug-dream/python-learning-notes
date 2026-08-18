# # 一种可以容纳多份数据的数据类型,每一份数据称为元素(可以是任意类型)
# # 列表(list)   字符串(str)不可变   元组(tuple)不可变|之前全有序,可重复元素  集合(set)去重   字典(dict)
#   s = [...]   s = "..."    s = (...)    s = {...}        s = {key:value,...}
# s = [1,1,2]  s = "spring"  s =(1,1,2,)  s = {1,5,3,2}    s = {'名字':'张三','语文':90,'数学':80}
# # 列表定义 s = [....]
# # 列表名 = [元素1,2,2,3,4,4.....]有序.可改.可用不同类型
# # 元素1 = 列表名[0] 正向索引从0开始         元素last = 列表名[-1] 反向..-1开始
#
# s = [1,12,32,"姜磊爱玩原神",True,"!"]
# print(type(s))
#
# # 获取
# print(s[3])
# print(s[-3])
#
# # 修改
# s[4] = "姜磊是卡卡罗的狗"
# print(s)
#
# # 删除
# del  s[0]
# print(s)
#
# 证明有序
# for x in s:
#     print(x)

# # 切片:截取列表一部分 d[开始索引:结束..:步长]
# d = [1,2,3,4,6,12,32,2]
#
# print(d [0:4:1])
# print(d [0:4])
# print(d [0:4:])
# print(d [:4])
#
# print(d[1:7:1])
#
# print(d[1:7:2])
#
# print(type(d[1:7:2]))

# 列表方法(功能): s.append(尾部要添加的元素)       s.insert(索引位置(序列数)前,插入元素)
#              s.remove(删除第一个匹配的元素)    s.pop(删除该索引位置)   s.pop:即删最后一个元素
#               s.sort():对相同数据类型排序       s.reverse():翻转列表元素

# s = [1,2,1,4,656,4,768,234]
# s.append(1314)
# print(s)

# s.insert(2,520)
# print(s)

# s.remove(4)
# print(s)
#
# s.pop(-3)
# print(s)
#
# s.sort()
# print(s)
#
# s.reverse()
# print(s)
#
# print(s.count(1))


# # 案例1 输入10个数，对这些数排序，输出其最小值,最大值和平均值sum(求和函数)len(个数)
# s = []
#
# for i in range(10):
#     num = int(input("请输入一个有效数字:"))
#     s.append(num)
# print(f"列表: {s}")
# s.sort()
# print(f"排序后的列表: {s}")
# print(f"最大值为:   {s[0]}")
# print(f"最小值为:   {s[-1]}")
# print(f"平均值为:   {sum(s)/len(s)}")


# # 案例2 num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# #      num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]       对两个列表进行去重
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# for num in num_list2:
#     num_list1.append(num)
# print(num_list1)
# print(f"合并后的原始列表{num_list1}")
# # 解包:将列表解开一个个元素 *s
# # 组包:将多元素合并到一个容器
# new_list =[] # new_list = [*num_list1,*num_list2] # new_list = num_list1 + num_list2
# new_list = [*num_list1,*num_list2]
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print("去重后列表:   ", new_list)

# 案例3 1-20平方列表
# 方式一
# s = []
# for i in range(21):
#     s.append(i**2)
s = [i**2 for i in range(21)]
print(s)


# # 列表推导式:快速生成列表的方式 方式1:列表 = [要插入的元素 for i in 列表/序列] (range序列)
# #                         方式2:列表 = [要插入的元素 for i in 列表/序列 if 条件]
# s1 = [i**2 for i in range(21)]
# print(s1)

# # 案例4 提取列表s2的偶数,生成该偶数平方列表
# s2 = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98, 110, 111, 122]
# s2 = [i**2 for i in s2 if i %2 ==0]
# print(s2)


