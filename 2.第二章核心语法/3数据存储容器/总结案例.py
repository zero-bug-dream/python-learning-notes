student_infor = {} # student_infor ={student_name1{"chinese":chinese_score,math:math_score,english:english_score
#                                               student_name2{...})...}
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出学生信息 6.统计班级成绩 7.退出系统        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

请选择要执行的操作(1-7):1
请输入学生姓名: 张三
请输入语文成绩: 92
请输入数学成绩: 92
请输入英语成绩: 92
添加[张三]成功

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# 1.添加学生信息 2.修改学生信息 3.删除学生信息 4.查询学生信息 5.列出学生信息 6.统计班级成绩 7.退出系统        #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
"""
print("欢迎来到教务系统")

while True:
    print(menu)
    choice = input("请输入要执行的操作(1-7):")
    match choice:
        case "1":
            student_names = input("请输入学生姓名:")
            if student_names in student_infor:
                print("已存在学生信息,请重新输入")
            else:
                chinese_score = float(input("请输入语文成绩:"))
                math_score = float(input("请输入数学成绩:"))
                english_score = float(input("请输入英语成绩:"))
                student_infor[student_names] = {"chinese": chinese_score, "math": math_score, "english": english_score}

        case "2":
            student_names = input("请输入学生姓名:")
            if student_names not in student_infor:
                print("不存在学生信息,请重新输入")
            else:
                chinese_score = float(input("请输入修改后的语文成绩:"))
                math_score = float(input("请输入修改后的数学成绩:"))
                english_score = float(input("请输入修改后的英语成绩:"))
                student_infor[student_names] = {"chinese": chinese_score, "math": math_score, "english": english_score}
        case "3":
            student_names = input("请输入要删除学生姓名:")
            if student_names not in student_infor:
                print("不存在学生信息,请重新输入")
            else:
                del student_infor[student_names]
        case "4":
            student_names = input("请输入要查询的学生姓名:")
            if student_names in student_infor:
                student_score = student_infor[student_names]
                print(f"学生姓名:{student_names},语文成绩:{student_score["chinese"]},"
                      f"数学成绩:{student_score["math"]},英语成绩:{student_score["english"]}")
            else:
                print("不存在该学生信息,请重新输入")
        case "5":
            for student_names in student_infor.keys():
                student_score = student_infor[student_names]
                print(f"学生姓名:{student_names},语文成绩:{student_score["chinese"]},"
                      f"数学成绩:{student_score["math"]},英语成绩:{student_score["english"]}")

        case "6":# student_infor ={student_name1{"chinese":chinese_score,math:math_score,english:english_score
            # student_name2{...}
            if len(student_infor) == 0:
                print("暂无学生数据,无法统计")
            else:
                chinese_list = [] #list [(a,b)...元组内]列表外
                math_list = []
                english_list = []
                for student_names,student_score in student_infor.items():

                    chinese_list.append((student_score["chinese"],student_names))
                    math_list.append((student_score["math"],student_names))
                    english_list.append((student_score["english"],student_names))

                    ch_max_score, ch_max_name = max(chinese_list)
                    ch_min_score, ch_min_name = min(chinese_list)
                    ma_max_score, ma_max_name = max(math_list)
                    ma_min_score, ma_min_name = min(math_list)
                    en_max_score, en_max_name = max(english_list)
                    en_min_score, en_min_name = min(english_list)

                    ch_avg = sum(item[0] for item in chinese_list) / len(chinese_list)
                    ma_avg = sum(item[0] for item in math_list) / len(math_list)
                    en_avg = sum(item[0] for item in english_list) / len(english_list)

                print(f"语文最高分:{ch_max_score},{ch_max_name},语文最低分:{ch_min_score},{ch_min_name},平均分:{ch_avg:.1f}")
                print(f"数学最高分:{ma_max_score},{ma_max_name},数学最低分:{ma_min_score},{ma_min_name},平均分:{ma_avg:.1f}")
                print(f"英语最高分:{en_max_score},{en_max_name},英语最低分:{en_min_name},{en_min_name},平均分:{en_avg:.1f}")

        case "7":
            print("退出系统,886")
            break
        case _:
            print("操作错误,不支持!!!")

