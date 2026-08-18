# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名(要设置权限,不用我们手动填充key),值就是api秘钥,这里看不到)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 与AI交互
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名很可爱甜美的AI助理，你的名字叫小美,请你使用傲娇温柔的语气回答用户问题"},
        {"role": "user", "content": "你是谁,你对我有什么帮助?"},
    ],
    stream=False
)
# 输出大模型返回的结果
print(response.choices[0].message.content)