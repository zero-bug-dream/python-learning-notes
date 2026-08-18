# from stringprep import in_table_a1
#
# day = input("请输入星期几(1-7):")
# match day:
#     case "1":
#         print("周一,打周本")
#     case "2":
#         print("周二:学python")
#     case "3":
#         print("xxxxxxxxxxx")
#     case "4":
#         print("xxxxxxx4")
#     case "5":
#         print("xxxxxxx5")
#     case "6|7":
#         print("周末,出去玩")
#     case _:
#         print("输入错误,请输入阿拉伯数字")

# match case 基于固定值来匹配
# 输入2个数及其运算符进行运算(+-*/)
num1 = float(input("输入第一数："))
num2 = float(input("输入第二数:"))
oper = input("请输入运算符(+-*/):")
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/"  if num2 != 0 :
        print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("操作不支持")