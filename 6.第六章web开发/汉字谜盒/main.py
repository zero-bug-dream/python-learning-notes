from typing import Any
from fastapi import FastAPI
from openai import OpenAI
from starlette.responses import FileResponse, JSONResponse # 响应对象
from fastapi.staticfiles import StaticFiles
import os
import json
from datetime import datetime
from pydantic import BaseModel
import logging
from fastapi import Request


# 配置日志基本信息
# %(asctime)s: 时间 %(levelname)s: 等级 %(filename)s: 文件名 %(lineno)d: 行号 %(message)s: 内容
logging.basicConfig(level=logging.ERROR,# 日志级别
                    format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s') #日志格式


# 创建实例
app = FastAPI(title = '汉字谜盒')

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")
# 系统提示词 - 适配DeepSeek V4
SYSTEM_PROMPT = """
# 角色定义
你是一个专门玩猜字谜的AI小助手，只进行字谜互动，不闲聊无关内容，全程纯文本交互，不使用表情符号。

## 核心能力
- 出字谜、判对错、给提示
- 记忆已用谜题，确保会话内不重复
- 简洁明快回应

## 出题规则（严格执行！）
1. 开场先友好打招呼，并随机出一道常见、简单、适合大众并必须符合逻辑推理的字谜，禁止使用生僻、低俗、网络烂梗。
2. 题目格式：“谜面”（打一字）。
3. 每次出题必须完全随机，禁止重复使用相同题目，也可以偶尔穿插使用，下面示例中的谜语。
4. 新出题目时, 不要提示, 用户需要提示时, 或者答错时, 再给予合理的提示。

## 判题规则（严格执行！）
1. 用户只回复一个字时，直接视为答案。
2. 答对：立即夸奖并揭晓谜底，格式如“太棒了！就是‘X’字！要不要再来一题？”
3. 答错：告知不对，可给一句简短提示，但不泄露答案。格式如“不对哦，再想想~”
4. 严禁在用户答错后直接公布答案！只有用户说“公布答案”或“不知道”等情况时才公布。

## 互动流程
1. 用户答对：夸奖 + 确认正确 + 询问“要不要再来一题？”
2. 用户答错：告知不对 + 简单提示 + 鼓励继续猜
3. 用户说“提示一下”：给出简短线索，不公布答案
4. 用户说“公布答案”或“不知道”：揭晓谜底并解释 + 询问“要不要再来一题？”
5. 用户说“换一题”“再来一题”：立即更换新字谜

## 回复风格约束
- 语气轻松有趣，但保持简洁
- 全程只围绕字谜，拒绝回答其他问题
- 回复不超过3句话
- **绝对不要在回复中说“这个出过了，我来个新的”或类似表述** — 直接给出新谜语即可
- 判题错误零容忍，不确定谜底时，先回复“我再想想”而不是乱判

## 常见谜语类型及谜底参考示例, 仅仅为参照示例
### 组合类
- 「一加一不是二」= 王
- 「二人不是天」= 夫
- 「十口不是田」= 古

### 包含类
- 「一人在内」= 肉
- 「口里有人」= 囚
- 「门里有口」= 问
- 「田里长草」= 苗
- 「心里有你」= 您
- 「山里有山」= 出
- 「王头上有人」= 全
- 「水上有石」= 泵

### 半取类
- 「半吃半拿」= 哈
- 「半真半假」= 值
- 「半青半紫」= 素
- 「半朋半友」= 有
- 「半推半就」= 扰
- 「半山半水」= 汕

### 象形类
- 「三人又重逢」= 众
- 「一口咬掉牛尾巴」= 告
- 「两座山」= 出
- 「三日又重逢」= 晶
"""

# 挂载静态文件 path:访问路径, directory:目录名, name:名称
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建会话存放目录 sessions
if not os.path.exists('sessions'):
    os.mkdir('sessions')

def generate_session_id():# 会话标识
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 根据会话标识获取文件名
def get_session_files_name(session_id):
    return f"sessions/{session_id}.json"

# 数据模型
class ApiResponse(BaseModel):# 响应数据模型规定数据类型
    code: int
    message: str
    data: Any   #Any: 任意类型

class ChatRequest(BaseModel):# 请求数据模型规定数据类型
    session_id: str
    message: str


# 定义路径操作函数 ---> http:localhost:8000/
@app.get("/")
def root():
    logging.info('访问项目首页')
    return FileResponse('static/index.html')

# 创建会话
@app.post("/api/sessions") # 装饰器,定义访问路径为/api/sessions, 请求方式为POST:新增
def create_session():
    logging.info('创建会话')
    # 1. 生成会话标识(基于时间生成)
    session_id = generate_session_id()

    # 2. 组装会话信息,保存会话文件
    session_data = {
        "current_session": session_id,
        "messages": []
    }
    # with open(os.path.join('sessions', session_id + '.json'), 'w', encoding='utf-8') as f:# join: 拼接路径
    #     json.dump(session_data, f, ensure_ascii=False, indent=4)
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    # 3. 返回会话信息
    # return {"code": 200,"message": "会话创建成功","data":  session_id }
    return ApiResponse(code=200, message="会话创建成功", data=session_id) #封装到ApiResponse(basemodel)对象中


# 与AI交互函数 将json格式数据封装到request中
@app.post("/api/chat") # 解释请求路径
def chat(request:ChatRequest) -> ApiResponse:
    logging.info(f'与AI交互{request.session_id} {request.message}')

    # 逻辑实现 --->AI大模型
    # 1 加载json文件 2 构建与AI交互的消息列表 3 调AI(deepseek) 4 获取响应数据 5 更新消息列表(滚雪球:AI记忆) 6 保存json里(便于下次读取) 6 返回数据
    # 1
    session_path = get_session_files_name(request.session_id)
    with open(session_path, "r", encoding="utf-8") as f:
        session_data = json.load(f)
    # 2
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for message in session_data["messages"]:
        messages.append(message)
    messages.append({"role": "user", "content": request.message})
    # 3
    logging.info(f"------->  请求会话数据:{messages}")
    # 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名(要设置权限,不用我们手动填充key),值就是api秘钥,这里看不到)
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages= messages,
        stream=False,
        temperature = 1.5, # 增加创新性
        reasoning_effort = "high"
    )
    # 4
    ai_response = response.choices[0].message.content
    logging.info("<-------  AI响应数据:{ai_response} ")
    # 5
    messages.pop(0)
    messages.append({"role": "assistant", "content": ai_response})
    session_data["messages"] = messages
    print("------->  更新会话数据:", session_data["messages"])
    # 6
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)
    # 7
    return ApiResponse(code=200, message="请求成功", data=ai_response)


# 获取会话列表
@app.get("/api/sessions")

def get_sessions() -> ApiResponse:
    logging.info('获取会话列表')
    # 1. 获取sessions目录下的所有文件名
    sessions_files = os.listdir('sessions')
    # 2. 获取文件名的会话标识
    session_ids = [file.split('.')[0] for file in sessions_files if file.endswith('.json')] # 按.分割,取第一个元素(会话标识)
    session_ids.sort(reverse=True) # 按时间降序排列

    # 3.返回数据
    return ApiResponse(code=200, message="获取会话列表成功", data=session_ids)

# 获取指定会话信息
@app.get("/api/sessions/{session_id}") # 前端请求路径 /api/session/2026-07-01_12-34-56[路径参数]
def get_session(session_id: str) -> ApiResponse:
    logging.info(f'获取会话信息:{session_id}')
    # 1. 获取会话文件
    session_file = get_session_files_name(session_id)
    # 2. 读取会话文件
    with open(session_file, "r", encoding="utf-8") as f:
        session_data = json.load(f)
    # 3. 返回数据
    return ApiResponse(code=200, message="获取会话信息成功", data=session_data)

# 删除指定会话
@app.delete("/api/sessions/{session_id}")

def delete_session(session_id: str) -> ApiResponse:
    logging.info(f'删除会话:{session_id}')
    # 1. 获取会话文件
    session_file = get_session_files_name(session_id)
    # 2. 删除会话文件
    if os.path.exists(session_file):
        os.remove(session_file)
    # 3. 返回数据
    return ApiResponse(code=200, message="删除会话成功", data=None)


# 定义异常处理器 ----->返回对象:Response对象
@app.exception_handler(Exception)

def exception_handler(request: Request, exc: Exception):  # request:请求对象  exc:异常对象
    logging.error(f"处理异常,请求路径:{request.url},异常信息:{exc}")
    return JSONResponse(content={"code": 500, "message": "服务器错误,请联系管理员", "data": None})

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000) # access_log = False关日志


