# # 类似"字典,一一对应,dict:存键值对  {key不可变类型:value,...} 不可重复,可修改
# dict1 = {"a":10,"b":20,"c":30,"d":40,"e":50}
# dict2 ={}
# dict3 = dict()
# print(dict3)
# print()
# num = dict1["a"]# 后面重复a值会覆盖
# print(num)
# print()
# dict4 = {1:12,1.323:34,"姜磊":250,(1,2):23}
# print(dict4)
# print()
# # 访问
# print(dict4[(1,2)])
# print()
# # 可改
# dict4[(1,2)] = "姜磊是卡卡罗的狗"
# print(dict4)
# dict = {dict1{dict_x1:xyxy,dict_x2:xyxy...}
# 常用操作
# dict = {1:"abc",2:"def",3:"ghi",4:"jkl"}
# dict[5] = "mno"# 添加和修改操作
# print(dict)
#
# print(dict.pop(1)) # 删除操作  .pop() :会返回value值       del :全删
# print(dict)
# del dict[2]
# print(dict)

# a = dict[3]# 查询
# print(type(a))
# print(type(dict))
# print(a)
# print(dict.get(3))#get (必须是字符串)要带引号
# print(dict.keys())
# print(dict.values())
# print(dict.items())
"""
for k in dict.keys():
    print(f"{k}:{dict[k]}")
print()

for x in dict.items():
    print(f"11{x[1]}；:22{x[0]}")
print()
dict = {1:"abc",2:"def",3:"ghi",4:"jkl"}
for m,n in dict.items():
    print(f"{m}:{n}")
    print(f"{m}:{n}:{m}")
"""
s = {"名字":"姜磊", "年龄":18, "性别":"男", "爱好":["python", "爱玩原神且是卡卡罗的狗"]}
s["名字"]="小甜甜"
s["年龄"]=18
s["性别"]="女"
s["爱好"]=["python"]
print( s)
print()
for i in s.items():
    print(f"{i[0]}:{i[1]}")
print()
for i in s.values():
    print(i)
