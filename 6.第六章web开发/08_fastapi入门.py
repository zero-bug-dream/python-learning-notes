# web:全球广域网,www(world wide web) 可通过浏览器访问的网站
# 三部分:前端程序(界面展示)  服务端程序(业务逻辑处理)  数据库(数据存储和管理)
#  前端程序(界面展示) :网页由 HTML(网页结构-内容)  CSS(网页表现--样式)  JavaScrippt(网页动作-交互)

# FastAPI:用于基于Python类型提示构建API(application programming interface)接口服务

# FastAPI使用步骤

# 1. 导入FastAPI
from fastapi import FastAPI

# 2. 创建FastAPI实例对象

app = FastAPI()

# 3. 创建路径操作函数,定义访问路径(定义接口) -->该函数返回值即为接口函数返回的数据
@app.get("/") # 定义访问路径为根路径/, 请求方式为GET
def read_root():
    return {"message": "你好"}

# 3.1 再定义一个路径操作函数
@app.get("/users")
def get_users():
    return [
        {"name": "张三", "age": 18},
        {"name": "李四", "age": 20},
        {"name": "王五", "age": 22}
    ]



# 4. 运行服务
# fastapi dev "xxx.py"(uvicorn main(py名不带py后缀) :app --reload)   命令行中实现

# 启动服务 --->uvicorn :python中一个轻量级的web服务器
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host= "0.0.0.0", port = 8000)