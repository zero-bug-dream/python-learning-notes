# # 数字反转
# n = int(input())
# res = 0
# while n > 0:
#     res = res * 10 + n % 10
#     n = n // 10
# print(res)


while True:
    thought = llm(f"观察: {obs}\n下一步是?")
    action = parse(thought)
    if action.type == "finish":
        break
    obs = execute(action.tool, action.args)