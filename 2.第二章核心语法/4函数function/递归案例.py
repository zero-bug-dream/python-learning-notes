# 案例1:计算n的阶乘
# 递归:函数中自己调用自己的情况,要设置终结点
"""ctrl + d
jc(10) = 10 *jc(9)
jc(9) = 9 *jc(8)
jc(8) = 8 *jc(7)
jc(7) = 7 *jc(6)
jc(6) = 6 *jc(5)
jc(5) = 5 *jc(4)
jc(4) = 4 *jc(3)
jc(3) = 3 *jc(2)
jc(2) = 2 *jc(1)
jc(1) = 1
"""
def jc(n):
    if n ==1:
        return 1
    else:
        return n * jc(n-1)
result = jc(10)
print(result)

