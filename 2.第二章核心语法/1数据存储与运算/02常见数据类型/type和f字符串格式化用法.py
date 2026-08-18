# type:查看数据类型
print(type("hello"))
print(type(3.14))

num=5
print(num)
print(type(num))

print(type(None))

print(type(True))

# isinsttance(数据,类型)---bool结果
print(isinstance("hello",str))



#字符串("""多行操作)(It\'s better day)和单引号重复
# 一个字母,数字,标点算一个字符
a = 'hello'
b ="""hello
           123
                企鹅群"""
print(a,b)
print(type(b))
print("我说\"今天是星期五\"")# \"-转译字符   \n-换行符  \t-缩进制表符(tap)大小


print("\t今天是星期五;\n\t不是疯狂星期四哦!")

# 字符串拼接(+拼接)
a = "人生苦短" "我用Python"",ok"
print(a)

b = "人生苦短"
c = "我用Python"
print("黑马说:"+b +c )
print("黑马说:"+ b + " ," +c)

# eg
q = "大家好"
w = "我是蒋磊"#name
e = "今年刚满18岁"#age
r = "爱玩原神且是卡卡罗的狗!"#hobby
print(q+ "," + w + " , "+ e + " , "+r)

name="姜磊"
age=18 #age 是特殊字符串,要进行字符串转换
hobby="爱玩原神且是卡卡罗的狗!"
print("大家好,我是"+ name +" ,今年" + str(age) +"岁,爱好是 "+hobby +"")

# 字符串格式化  方式一 %s 占位符 %(1 2 3)
name="姜磊"
age=18
hobby="爱玩原神且是卡卡罗的狗!"
print("大家好,我是%s ,今年%s岁,爱好是 %s"  % (name,age,hobby))

# 方式二 f"内容 {变量/表达式} 推荐方式 f"{xxxxx}
name="姜磊"
age=18
hobby="爱玩原神且是卡卡罗的狗!"
print( f"大家好,我是{name} ,今年{age}岁,爱好是 {hobby}" )