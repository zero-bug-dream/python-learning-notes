# # for  .  in...
# #      for  .  in...
# m = int (input("请输入长方形长度:"))
# n = int (input("请输入长方形宽度:"))
# for j in range(n):
#     for i in range(m):
#         print("^",end= "  ")
#     print()


# # 案例打印九九乘法表
# for j  in range(1,10) :#控制几行
#     for i in range(1,j+1):#控制几列
#         print(f"{i} × {j} = {i*j}",end="\t")
#     print()

# # 打印等腰直角三角形（5）
# for j in range(1,6):
#     for i in range(1,j+1):
#         print("*",end="\t")
#     print()

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(f"{j}",end="\t")
#     print()
#
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end = "\t")
        else:
            print("□", end="\t")
    print()