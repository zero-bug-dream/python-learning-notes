# streamlit :一个Python库,基于Python构建一个web网站(无需前端技术)

"""
前端，就是用户眼睛能直接看到、能用手操作的那部分网页 / 软件界面！
举个最接地气的例子，你打开浏览器逛 B 站：
页面上的 logo、视频封面、播放按钮、弹幕、滚动条、登录弹窗、切换黑夜模式，这些全部都是前端做出来的。
后端：藏在服务器里默默干活，普通人看不见（比如存账号密码、查询数据库、接口计算，就是咱们之前调用 DeepSeek API 那一套）
"""
# https://streamlit.io

import streamlit as st
# 大标题
st.title("Streamlit 入门演示")
st.header("一级标题")
st.subheader("二级标题")

import streamlit as st

# 页面标题
st.title("🕷️ 蜘蛛侠 人物介绍站")
st.subheader("With great power comes great responsibility")

# 文字介绍
st.markdown("""
彼得·帕克，一名普通的纽约高中生，在被放射性蜘蛛咬伤后，获得蜘蛛一般的超能力。
能力包括：蜘蛛感应、超强力量、敏捷身手、吸附墙面、自主制造蛛丝。

本叔的名言：**能力越大，责任越大（With great power comes great responsibility）**
最初彼得只想利用能力赚钱谋生，因为忽视他人，间接导致本叔遇害。这场悲剧让他领悟英雄的意义，从此化身蜘蛛侠，守护纽约街头。

蜘蛛侠并非天生无敌，他要兼顾学业、打工赚钱、维系朋友与恋人的关系，常常陷入生活拮据、身心疲惫的困境。
正因为充满普通人的烦恼，他成为漫威最贴近大众、人气最高的超级英雄之一。

### 主流经典版本
1. 托比·马奎尔版《蜘蛛侠》三部曲（山姆雷米，经典初代银幕蜘蛛侠）
2. 安德鲁·加菲尔德《超凡蜘蛛侠》系列
3. 汤姆·赫兰德 漫威电影宇宙MCU蜘蛛侠
4. 动画电影《蜘蛛侠：平行宇宙》（迈尔斯·莫拉莱斯）
""")

# 图片（路径根据你的文件夹填写）
st.image("resources/spider_man.png", caption="蜘蛛侠", width=600)


# 音频
# st.subheader("🎵 蜘蛛侠主题曲")
# st.audio("resources/theme_audio.mp3")

# 视频
st.subheader("🎬 精彩片段")
st.video("resources/clip_short.mp4")

st.logo("resources/logo.png")

