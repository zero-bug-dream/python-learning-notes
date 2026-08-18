# 通过面向对象编程
# 1.添加学生信息("姓名:张三 | 语文:12 | 数学:98 | 英语:78 | 总分:...") 2.修改学生信息 3.删除学生信息 4.查询指定学生信息 5.列出全部学生信息
# 学生类
class student:
    def __init__(self,s_name,s_chinese,s_math,s_english):
        self.name = s_name
        self.chinese = s_chinese
        self.math = s_math
        self.english = s_english

    def __str__(self):
        return f" 姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.chinese+self.math+self.english}"
    # 修改学生信息(定义一个方法)
    def update_score(self,chinese = None,math = None,english = None):# 关键字传参可以指改一个,None不做修改
        # 要判断传递成绩成绩有没有,有就改(不满没有)
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# # 测试
# if __name__ == '__main__': # 调用自定义模块不会执行测试代码
#     s1 = student("姜磊",43,23,0)
#     s2 = student("张三",100,98,87)
#     print(s1)
#     s1.update_score(english=11)
#     print(s1)

# 教务管理系统类
class educas:
    system_version = "1.0.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = []

    # 添加学生成绩(方法)
    def add_student(self):
        name = input("请输入要添加的学生姓名:")
        # if name  in self.student_list:(不行,因为学生类别包含名字和成绩信息太多了)
        for s in self.student_list:
            if s.name == name:
                print("该学生已存在,添加失败")
                return #要给返回值,表示存在就结束
        chinese = int(input("请输入该学生的语文成绩:"))
        math = int(input("请输入该学生的数学成绩:"))
        english = int(input("请输入该学生的英语成绩:"))
        if 0 <= chinese <=100 and 0 <= math <= 100 and 0 <= english <= 100:
            new_stu = student(name,chinese,math,english)
            self.student_list.append(new_stu)
            print("学生信息添加成功!")
        else:
            print("成绩要在0-100之间")
    # 修改学生成绩
    def update_student(self):
        name = input("请输入要修改的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print("当前成绩:",s)
                chinese = int(input("请输入要修改后语文成绩:"))
                math = int(input("请输入要修改后数学成绩:"))
                english = int(input("请输入要修改后英语成绩:"))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_sore(name, chinese, math, english) # 调用魔法方法

                    print("学生信息修改成功!")
                    print("学生修改后的成绩:", s)
                    return
                else:
                    print("成绩要在0-100之间")
                    return  # 要给返回值,表示存在就结束


        print("没有该学生信息")
    # 删除学生成绩
    def del_student(self):
        name = input("请输入要删除的学生姓名:")
        # if name  in self.student_list:(不行,因为学生类别包含名字和成绩信息太多了)
        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功!")
                return  # 要给返回值,表示存在就结束

        print("没有该学生信息")
    # 查询指定学生信息
    def be_sure_student(self):
        name = input("请输入要查询的学生姓名:")
        for s in self.student_list:
            if s.name == name:
                print("要查询的学生信息为：",s)
                return  # 要给返回值,表示存在就结束,向外传输数据
        print("没有该学生信息")
    # 列出学生信息
    def lise_student(self):
        for s in self.student_list:
            print(s)
    # 运行系统
    def run(self):
        print("欢迎来到教务系统",educas.system_version)

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生 2.修改学生 3.删除学生 4.查询指定学生 5查询索引学生 6.退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")

            choice = input("请输入操作数字(1-6):")
            try:
                match choice:  # match case 匹配情况要是str类型
                    case "1":
                        self.add_student()
                    case "2":
                        self.update_student()
                    case "3":
                        self.del_student()
                    case "4":
                        self.be_sure_student()
                    case "5":
                        self.lise_student()
                    case "6":
                        print("退出系统,886")
                        break
                    case _:
                        print("输入错误,请正确输出操作数(1-6)")
            except ValueError as e:
                print("输入数据有问题,请重新输入", e)
            except Exception as e:
                print("程序出bug了,错误信息为:",e)

if __name__ == "__main__":
    educas = educas()# 创建对象
    educas.run()