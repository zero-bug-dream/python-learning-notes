# 需要先导入json模块
# json.dumps():将python对象序列化为json字符串并写入文件(Python转json)
# json.loads():从文件中读取json字符串并反序列化为python对象(json转Python)
# 1.导入模块
import json
# 写入json的文件
s = {
    "name": "姜磊",
    "age": 18,
    "hobby": ["python", "爱玩原神且是卡卡罗的狗"],
    "gender": "man"
}
with open("resources/session.json", "w", encoding="utf-8") as f:# 序列化
    json.dump(s, f, ensure_ascii=False, indent=2)# 将s存储到f中(格式转为json字符串)
    # ensure_ascii: 默认值为True,则字符串中的非ASCII字符会被转义为Unicode(字转换为字符编号)编码,否则原样输出
    # indent: 缩进,默认为None,不缩进

# 读取json文件
with open("resources/session.json", "r", encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))
