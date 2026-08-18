# 计算每个student的总分,各科平均分,一起输出
# 统计各科最低最高分和平均分输出
# 查找成绩(优秀平均分>90）的学生，并输出

students = (
    ("s001","王林",85,92,78),
    ("s002","李慕婉",92,88,95),
    ("s003","十三",78,85,82),
    ("s004","曾牛",88,79,91),
    ("s005","周铁",95,96,89),
    ("s006","王卓",76,82,77),
    ("s007","红蝶",89,91,94),
    ("s008","徐立国",75,69,82),
    ("s009","徐木",86,89,98),
    ("s010","通天",66,59,72),
)
print("学号 \t姓名 \t总分 \t平均分")
# for s in students:
#     total = s[-1] + s[-2] + s[-3]
for id, name, chinese, math, english in students:
    total = chinese + math + english
    avg = total/3
    print(f"{id} \t{name} \t{chinese + math + english} \t{avg:.1f}")

chinese_scores = [s[-3] for s in students ]
math_scores = [s[-2] for s in students ]
english_scores = [s[-1] for s in students ]

print(f"语文最低分:{min(chinese_scores)}语文最高分:{max(chinese_scores)}")
print(f"数学最低分:{min(math_scores)}数学最高分:{max(math_scores)}")
print(f"英语最低分:{min(english_scores)}英语最高分:{max(english_scores)}")

# for s in students:
#     total = s[-1] + s[-2] + s[-3]
#     avg = total/3
#     if avg > 90:
#         print(f"学号:{s[0]},优秀学生:{s[1]},平均分:{avg:.1f}")
for id,name,chinese_scores,math_scores,english_scores in students:
    total = chinese_scores + math_scores + english_scores
    avg = total/3
    if avg > 90:
        print(f"学号:{id},姓名:{name},平均分:{avg:.1f}")