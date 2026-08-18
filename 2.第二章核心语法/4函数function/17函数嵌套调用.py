# # 后进先出(弹夹)
def function_a():
    print("a---------before")
    function_b()
    print("a---------after")

def function_b():
    print("b--------before")
    function_c()
    print("b--------after")

def function_c():
    print("c--------------")

function_a()

# 案例1定义一个函数根据传入的底和高计算三角形面积(area = bottom * high / 2
def triangle_area(bottom, high):
    """
    根据传入的底和高计算三角形面积
    :param bottom: 三角形的底
    :param high: 三角形的高
    :return: 三角形的面积
    """
    area = bottom * high / 2
    return area

a1 =triangle_area(30,10)
print(a1)

# 案例2:定义一个函数:计算传入字符串中元音字母的个数(aeiouAEIOU)
def count_aeiou (str):
    """
    计算传入字符串中元音字母的个数
    :param str: 传入的字符串
    :return: 元音字母个数
    """
    num = 0
    for x in str:
        if x in 'aeiouAEIOU':
            num += 1
    return num
count_s = count_aeiou("jiangleishisb")
print(f"传入字符串的元音字母个数为:{count_s}")

# 定义一个函数:计算并统计传入班级学员高考成绩列表中的最高分,最低分,平均分(保留一位小数)
def calu_list(score_list):
    """
    计算并统计传入班级学员高考成绩列表中的最高分,最低分,平均分(保留一位小数)
    :param score_list: 成绩列表
    :return: 最高分,最低分,平均分
    """
    max_score = max(score_list)
    min_score = min(score_list)
    avg_score = round(sum(score_list) / len(score_list),1)
    return max_score, min_score, avg_score
s_list = [688,432,456,675,456,451,651]
max_score1, min_score1, avg_score1 = calu_list(s_list)
print(f"最高分:{max_score1},最低分:{ min_score1},平均分: {avg_score1}")