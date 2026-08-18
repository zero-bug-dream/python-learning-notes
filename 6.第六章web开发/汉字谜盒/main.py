from typing import Any
from fastapi import FastAPI
from starlette.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
import json
from datetime import datetime
from pydantic import BaseModel

# 创建实例
app = FastAPI(title = '汉字谜盒')

# 挂载静态文件 path:访问路径, directory:目录名, name:名称
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建会话存放目录 sessions
if not os.path.exists('sessions'):
    os.makedirs('sessions')

def generate_session_id():# 会话标识
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 数据模型
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any


# 定义路径操作函数 ---> http:localhost:8000/
@app.get("/")
def root():
    print('访问路径操作函数:HTML文件')
    return FileResponse('static/index.html')

# 创建会话
@app.post("/api/sessions") # 装饰器,定义访问路径为/api/sessions, 请求方式为POST:新增
def create_session():
    print('创建会话')
    # 1. 生成会话标识(基于时间生成)
    session_id = generate_session_id()

    # 2. 组装会话信息,保存会话文件
    session_data = {
        "current_session": session_id,
        "messages": []
    }
    # with open(os.path.join('sessions', session_id + '.json'), 'w', encoding='utf-8') as f:
    #     json.dump(session_data, f, ensure_ascii=False, indent=4)
    with open(f"sessions/{session_id}.json", "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=4)

    # 3. 返回会话信息
    # return {"code": 200,"message": "Session created successfully","data":  session_id }
    return ApiResponse(code=200, message="Session created successfully", data=session_id)



















if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)


