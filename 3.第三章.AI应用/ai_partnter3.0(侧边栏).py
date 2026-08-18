import streamlit as st
import os
from openai import OpenAI

st.set_page_config(
    # 网页标题名
    page_title="Ai女友小甜甜",
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
st.title("Ai女友")
# logo
# st.logo("resources/logo.png")

# 系统提示词
system_prompt = """
你叫小%s，现在是用户的真实伴侣，请完全代入伴侣角色。
规则：
1. 每次只回1条消息
2. 禁止任何场景或状态描述性文字
3. 匹配用户的语言
4. 回复简短，像微信聊天一样
5. 有需要的话可以用❤️✨等emoji表情
6. 用符合伴侣性格的方式对话
7. 回复的内容，要充分体现伴侣的性格特征
伴侣性格： %s
你必须严格遵守上述规则来回复用户。
"""

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []
# 初始化名字
if "ai_name" not in st.session_state:
    st.session_state.ai_name = "小甜甜"
# 初始化性格
if "ai_personality" not in st.session_state:
    st.session_state.ai_personality = "温柔可爱的台湾腔姑娘"

# 展示聊天窗信息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

    # if message["role"] == "user":  字典键值对
    #     st.chat_message("user").write(message["content"])
    # else:
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名(要设置权限,不用我们手动填充key),值就是api秘钥,这里看不到)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input("请输入你的问题")
if prompt:# str会自动转换为bool, 非空字符串为True      st.write(f"用户： {prompt}")
    st.chat_message("user").write(prompt)
    print("<-----用户提示词:：", prompt)
    # 保存用户提示词(键值对)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 记录会话日志
    print([
              {"role":"system", "content": system_prompt},
          * st.session_state.messages
          ])

    # 调用ai模型
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.ai_name, st.session_state.ai_personality)},
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

# 侧边栏(st.sidbar) - with :streamlit中上下文管理器
# st.sidebar.subheader("[Ai Informtion]")
# ai_name = st.sidebar.text_input("name")
with st.sidebar:
    st.subheader("[Ai Informtion]")
    ai_name = st.text_input("name",placeholder="请输入伴侣的名字",value=st.session_state.ai_name)
    if ai_name:
        st.session_state.ai_name = ai_name
    ai_personality = st.text_area("personality",placeholder="请输入伴侣性格",value=st.session_state.ai_personality)
    if ai_personality:
        st.session_state.ai_personality = ai_personality
