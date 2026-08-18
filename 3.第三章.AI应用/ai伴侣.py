import streamlit as st
import os
from openai import OpenAI
import datetime
import json

st.set_page_config(
    page_title="Ai女友小甜甜",
    page_icon="😘",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

def save_session():
    if st.session_state.current_session:
        session_data = {
            "ai_name": st.session_state.ai_name,
            "ai_personality": st.session_state.ai_personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    return session_list

def load_session(session_name):
    try:
        path = f"sessions/{session_name}.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.ai_name = session_data["ai_name"]
                st.session_state.ai_personality = session_data["ai_personality"]
                st.session_state.current_session = session_name
    except Exception:
        st.error("会话日志加载失败!")

def delete_session(session_name):
    """修复删除函数：删除文件，如果是当前会话立刻新建空白会话并保存"""
    try:
        file_path = f"sessions/{session_name}.json"
        if os.path.exists(file_path):
            os.remove(file_path)
            # 如果删除的是正在使用的会话
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
                save_session()  # 重点！删除当前会话，立刻保存新会话文件，防止幽灵会话
            st.success(f"会话 {session_name} 已删除")
    except Exception as e:
        st.error(f"会话日志删除失败! {e}")


st.title("Ai女友")

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

if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_name" not in st.session_state:
    st.session_state.ai_name = "小甜甜"
if "ai_personality" not in st.session_state:
    st.session_state.ai_personality = "温柔可爱的台湾腔姑娘"
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()
    save_session()

st.text(f"[当前会话]:{st.session_state.current_session}")

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

with st.sidebar:
    st.subheader("[AI控制面板]")

    if st.button("新建会话", width="stretch", icon="🖊️"):
        save_session()
        st.session_state.messages = []
        st.session_state.current_session = generate_session_name()
        save_session()
        st.rerun()

    st.text("[会话历史]")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([5, 1.2])
        with col1:
            btn_load = st.button(
                session,
                width="stretch",
                icon="📔",
                key=f"load_{session}",
                type="primary" if session == st.session_state.current_session else "secondary"
            )
            if btn_load:
                load_session(session)
                st.rerun()
        with col2:
            # ❗修复：按钮文字改成删除，key去掉空格
            btn_del = st.button(
                "🗑️",
                width="stretch",
                key=f"del_{session}"
            )
            if btn_del:
                delete_session(session)
                st.rerun()

    st.divider()# 分割线
    st.subheader("[💗伴侣信息]")
    ai_name = st.text_input("昵称", placeholder="请输入伴侣的名字", value=st.session_state.ai_name)
    if ai_name:
        st.session_state.ai_name = ai_name
    ai_personality = st.text_area("性格", placeholder="请输入伴侣性格", value=st.session_state.ai_personality)
    if ai_personality:
        st.session_state.ai_personality = ai_personality


prompt = st.chat_input("请输入你的问题")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.ai_name, st.session_state.ai_personality)},
            *st.session_state.messages
        ],
        stream=True
    )

    text_box = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            word = chunk.choices[0].delta.content
            full_response += word
            text_box.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()