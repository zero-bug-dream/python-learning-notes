# 编码（encoding）将字符转化为数字代码,UTF-8(全球通用)全可以用,asccii只能在转换字母,gbk不能转韩文和日文...
# 操作完文件,记得调用close()方法   close作用 关闭文件(不然文件会一直处于打开状态,占用内存)
"""
# 1.打开文件
f = open("resources/提示词.txt", "r", encoding="utf-8")

# 2.读取文件
# content = f.read()
# print(content)

content_list = f.readlines()# readlines()读取所有行,返回列表
for line in content_list:
    print(line.strip()) # strip()去掉字符串首尾空格

# 3.关闭文件
f.close()
"""
"""
# 1.打开文件
f = open("resources/填写内容.txt", "w", encoding="utf-8")

# 2.写文件
f.write("静夜思(李白 )\n\n")
f.write("床前明月光,\n")
f.write("疑是地上霜。\n")
f.write("举头望明月,\n")
f.write("低头思故乡 。\n")

# 3.关闭文件
f.close()
"""
# 资源释放

# ___________方案一
"""
# 1.打开文件
f = open("resources/填写内容.txt", "w", encoding="utf-8")

# 2.写文件
try:# try...except...finally...(捕获异常)
    f.write("静夜思(李白 )\n\n")
    f.write("床前明月光,\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月,\n")
    f.write("低头思故乡 。\n")

# 3.关闭文件

finally:# finally...(不管出没bug,该区域代码都会运行)
    print("关闭文件")
    f.close()
"""

# ___________方案二(推荐):with:(上下文管理器)作用:确保文件在with语句块结束后自动关闭(即使出现异常,也能正常释放)
# 相对路径写法(推荐!可移植性好): 当前目录下(".":当前目录="./(可省略)resources/填写内容.txt"   "..":上级目录,"../../xxx/")

with open("resources/填写内容.txt", "w", encoding="utf-8") as f:
    f.write("静夜思(李白 )\n\n")
    f.write("床前明月光,\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月,\n")
    f.write("低头思故乡1.0。\n")

with open("../1.第一章/通义灵码账号.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 绝对路径(转发给别人要检查路径):从文件系统的根目录开始,\\或者/ 来分隔(文件位置的完整路径) "\"在字符串中表示的是转义字符,如:\n,\t 使用\\可以表示路径的"\"
with open("D:\\迅雷下载\\源文件\\Q3.m", "r", encoding="utf-8") as f:
    print(f.read())

# 操作模式: r:读 w:写 a:追加
with open("resources/填写内容.txt", "a", encoding="utf-8") as f:# append:追加---如果文件不存在,则创建文件
    f.write("静夜思(李白 )\n\n")
    f.write("床前明月光,\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月,\n")
    f.write("测试追加内容(最低部)\n")


