# NameError Type... Index...
# 不做处理:会因为一个bug,导致整个程序中断
# 捕获异常:按我们自己处理方式,处理异常,程序继续执行

# try:
#     可能出现bug的代码
#      ...
# except 【异常类型 as 变量名】：
# [finally]
#     不管出不出bug，该区域的代码都会运行
try:
    print("____________________")

    print("abc".hello)

    print("____________________")
except NameError as e:
    print("出bug了,请联系管理员",e)
except ZeroDivisionError as e:
    print("0不能做被除数",e)
except IndexError as e:
    print("索引错误",e)
except Exception as e:
    print("出bug了,请联系管理员",e)
finally:# 无论对错,以下代码都会运行
    print("我宣布个事:'蒋磊是卡卡罗的狗'")
    print("资源释放")


# 异常的传递
def fun1():
    print("fun1...running...")
    fun2()# 函数调用要加括号
def fun2():
    print("fun2...running...")
    fun3()
def fun3():
    print("fun3...running...")
    print(my_nmae)

if __name__ == "__main__":
    try:
        fun1()
    except Exception as e:
        print("程序出bug了,错误信息为:",e)
