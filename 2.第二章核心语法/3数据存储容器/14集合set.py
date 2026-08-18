# # 存手机号，不存在重复数据，无序（不能索引），可修改
# s = {1,324,3,5,1,1,43,123,2,4}
# print(s)
# print(type(s))
# print()
# s1 = set() #空集合

s1 = {100,200,300,400,500}
s1.add(123)
print(s1)

s1.remove(400)
print(s1)

# 随机删除一个元素
x = s1.pop()
print(x)
print(s1)

# 清空元素
s1.clear()
print(s1)

s2 = {1,2,3,4,5,6}
s3 = {1,2,3,9,8,7}

print(s2.difference(s3)) # 差集(-)
print(s2.intersection(s3)) # 交集(&)
print(s2.union(s3))  # 并集(|)
print()

# 集合推导式 {要加入的集合数据 for s in set1 if 条件}
set3 = {s for s in s2 if s not in s3} # 差集
print(set3)

s_list = [*s1, *s2, *s3]
print(s_list)
for x in s_list:
    print(f"{x}重复了多少次{s_list.count(x)}")