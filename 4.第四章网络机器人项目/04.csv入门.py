# csv操作 - 方式一:文件操作的原始方式
# # 写
# with open ("csv_data/01.csv","w",encoding="utf-8") as f:
#     f.write("姓名,年龄,爱好,段位\n")
#     f.write("小王,12,'王者,Python,Java',星耀\n")
#     f.write("小李,16,basketball,王者\n")
#
# # 读
# with open ("csv_data/01.csv","r",encoding="utf-8") as f:
#     for line in f:
#         print(line.strip())

# 方式二:csv
import csv
# 写
with open ("csv_data/02.csv","w",encoding="utf-8",newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()# 写入表头
    writer.writerow({"姓名":"小王","年龄":12,"性别":"男","爱好":"Python,Java"})
    writer.writerow({"姓名":"小李","年龄":16,"性别":"女","爱好":"go"})
    writer.writerow({"姓名":"小张","年龄":18,"性别":"男","爱好":"瓦"})
    writer.writerow({"姓名":"涛哥","年龄":20,"性别":"男","爱好":"football,Java"})

# 读
with open ("csv_data/02.csv","r",encoding="utf-8",newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)