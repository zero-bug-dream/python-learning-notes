# 输入3边长,判断三角形类型
# 1输入3边长
a = int(input("输入第一个边的边长"))
b = int(input("输入第二个边的边长"))
c = int(input("输入第三个边的边长"))

# 2三角形类型判断
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print(f"{a},{b},{c}这三边构成等边三角形")
    elif a == b or b == c :
        print(f"{a},{b},{c}这三边构成腰三角形")
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        print(f"{a},{b},{c}这三边构成直角三角形")
    else:
        print(f"{a},{b},{c}这三边构成普通三角形")


else:
    print(f"{a},{b},{c}这三边不能构成三角形")