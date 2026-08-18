import streamlit as st # 调用streamlit模块:用于制作前端网页,打开地址localhost:8501(前提pip istall streamlit
import os # 调用Python内置模块:用于读取电脑系统api_key密钥(要提前设api_key环境变量)
from openai import OpenAI # 调用OpenAI(第三方库 包含deepseek模块):用于调用deepseekapi
import datetime # 内置模块:用于命名会话日志
import json # 用于json和Python间转换

# 设置页面配置
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

# 保存会话日志,(Python转换为json文件)
def save_session():
    if st.session_state.current_session: # 判断当前会话是否为空,如果不为空,则保存会话日志
        session_date = {
            "ai_name": st.session_state.ai_name,
            "ai_personality": st.session_state.ai_personality,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        # 如果sessions目录不存在,则创建
        if not os.path.exists("sessions"):  # 判断目录是否存在
            os.mkdir("sessions")  # 创建目录

        # 保存会话日志(date是日期的意思,data是数据)
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_date, f, ensure_ascii=False, indent=2)

# 生成会话日志
def generate_session_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 加载会话日志列表信息
def load_sessions():
    session_list = []
    #  遍历sessions目录下的所有文件
    if os.path.exists("sessions"):# 判断sessions下有文件
        file_list = os.listdir("sessions") #用file_list接收sessions下的文件(listdir列出某目录下的文件)
        for filename in file_list:
            if filename.endswith(".json"): # 判断文件名是否以.json结尾
                session_list.append(filename [:-5]) #切片取日志名,日志加入列表
    session_list.sort(reverse=True)# 翻转列表倒序
    return session_list

# 加载指定会话日志(读取保存好的json文件)
def load_session(session_name): # 根据session_name加载会话日志
    try:# 异常处理
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话日志
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.ai_name = session_data["ai_name"]
                st.session_state.ai_personality = session_data["ai_personality"]
                st.session_state.current_session = session_name
    except Exception :
        st.error("会话日志加载失败!")

# 删除会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            if st.session_state.current_session == session_name:
                st.session_state.current_session = generate_session_name()
                st.session_state.messages = []
                save_session()
    except Exception:
        st.error("会话日志删除失败!")

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
# 会话日志(名字)
if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()

# 展示会话名称
st.text(f"[当前会话]:{st.session_state.current_session}")
# 展示聊天窗信息
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])


# 创建与AI大模型交互的客户端对象(DEEPSEEK_API_KEY 环境变量名(要设置权限,不用我们手动填充key),值就是api秘钥,这里看不到)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 侧边栏(st.sidbar) - with :streamlit中上下文管理器
# st.sidebar.subheader("[Ai Informtion]")
# ai_name = st.sidebar.text_input("name")
with st.sidebar:

    st.subheader("[AI控制面板]")

    # 新建会话按钮
    if st.button("新建会话",width = "stretch",icon = "🖊️"):
        # 1.保存当前会话日志
        save_session()

        # 2.创建新的会话日志
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()  # 重新运行当前页面

    # 会话历史
    st.text("[会话历史]")
    session_list = load_sessions()
    for session in session_list:
        col1,col2 = st.columns([6,1])
        # 加载指定会话日志
        with col1:
            # 三元运算符:如果条件为真则返回第一个值,否则返回第二个值 -->语法:<true_value> if 条件表达式 else <false_value>
            if st.button(session,width = "stretch",icon = "📔",key = f"load_{session}",type ="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        # 删除按钮
        with col2:
            if st.button("",width = "stretch",icon = "❌️",key = f"delete_{session}"): # 删除会话信息(key = f"delete{session}":作为组件唯一标识 )
                delete_session( session)
                st.rerun()


        # st.buttion(session,width = "stretch",icon = "📔")
        # st.buttion("",width = "stretch",icon = "❌️")

    st.divider()#
    # 伴侣信息
    st.subheader("[💗伴侣信息]")
    ai_name = st.text_input("昵称",placeholder="请输入伴侣的名字",value=st.session_state.ai_name)
    if ai_name:
        st.session_state.ai_name = ai_name  # 赋值给初始化名字
    ai_personality = st.text_area("性格",placeholder="请输入伴侣性格",value=st.session_state.ai_personality)
    if ai_personality:
        st.session_state.ai_personality = ai_personality


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

    # 保存会话信息
    save_session()


