import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    # 网页标题名
    page_title="Ai女友小花",
    # 前缀logo
    page_icon="😘",
    # 布局
    layout="wide",
    # 侧边栏状态
    initial_sidebar_state="expanded",
    menu_items={
             }
)


# 大标题
st.title("Ai女友小花")
# logo
# st.logo("resources/logo.png")

# 系统提示词
system_prompt = "你作为一名AI助理兼女友,你的名字叫小花,请用最可爱的语气回答用户问题"

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 展示聊天窗信息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名(要设置权限,不用我们手动填充key),值就是api秘钥,这里看不到)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:# str会自动转换为bool, 非空字符串为True      st.write(f"用户： {prompt}")
    st.chat_message("user").write(prompt)
    print("<-----用户提示词:：", prompt)
    # 保存用户提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 记录会话日志
    print([
              {"role":"system", "content": system_prompt},
          * st.session_state.messages
          ])

    # 与AI交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True

    )
    # 输出大模型返回的结果(非流式输出解析方式)
    # print("<-----大模型返回的结果:", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 流失输出方式
    text_box = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            word = chunk.choices[0].delta.content
            full_response += word
            text_box.chat_message("assistant").write(full_response)



    # # 保存模型返回的提示词(False)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 保存模型返回的提示词(流式输出方式)
    st.session_state.messages.append({"role": "assistant", "content": full_response})