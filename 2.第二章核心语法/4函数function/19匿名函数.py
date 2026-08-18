# 没名字函数 lambda 参数列表 :函数体 (单行表达式)无return  def 函数名(参数列表)
out_line = lambda :print("-------------------------")
out_line()

# def out_line():
#     print("---------------------------------")
# out_line()
# 需求1计算两数之和
add = lambda x ,y : x+y
print(add(100,200))

def add(x,y):
    return x+y
print(add(10,20))

# 需求2完成列表排序(元素字符个数,从小到大排序) 列表.sort:表示排序
date_list = ["c++","c","python","java","go","english","jocker","time"]

date_list.sort()# 按字母ABCD顺序
print(date_list)
# 匿名函数运用典型案例:作为方法调用的参数运用
date_list.sort(key = lambda item :len (item))# x指元素,一般用item表示,但我英语不行
print(date_list)

date_list.sort(key = lambda x : len(x),reverse = True)# x指元素,一般用item表示,但我英语不行 reverse翻转
print(date_list)


