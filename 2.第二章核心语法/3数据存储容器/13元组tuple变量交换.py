# 存成绩排序,元组定义完成只能查询,不能修改,存数据类型不同类型 t = (元素1,元素2...),有序
# 操作
# 定义元组
t = (1,2,43,56,12,1) # t = 1,2,43,56,12,1
print(t)
print(t[0])
print(type(t))
# 定义空元组
# t1 = ()
# t2 = tuple()

#  切片
print(t[0:5:2])

# 方法  count() 记数                  index() 获取第一次出现元素索引位置
print(t.count(1))
print(t.index(1))

t3 = (100)     #定义单元素加,
print(t3)
print(type(t3))

# -----------------元组组包和解包---------------------
t1 = (0,7,24,12,14,12,26)
t2 = 0,7,24,12,14,12,26
print(t1,t2)

a,b,c,d,e,f,g = t1
print(a,b,c,d,e,f,g)

a1,b1,*c1,d1 =t1
print(c1)
print(type(c1))

a2,b2,c2,*d2 = t2
print(d2)

# 案例 变量交换ab互换    abc赋值于cab
# a = 10
# b = 20
# a,b = b,a
# print(a,b)

# a = 100
# b = 200
# c = 300
# c,a,b = a,b,c
# print(a,b,c)