# Python 学习笔记与项目 🐍

> 一份从零开始的 Python 学习全记录 —— 涵盖**基础语法、核心语法、AI 应用、网络爬虫、数据分析、Web 开发**六大模块,包含大量课堂案例与实战项目。

## 📁 项目结构

| 目录 | 模块 | 内容 |
| --- | --- | --- |
| `1.第一章` | Python 入门 | 环境搭建、基础脚本 |
| `2.第二章核心语法` | 核心语法 | 变量、数据类型、运算符、流程控制、容器、函数、模块、面向对象 |
| `3.第三章.AI应用` | AI 应用 | DeepSeek 大模型 API、提示词工程、Streamlit 界面、「AI 伴侣」进化史 |
| `4.第四章网络机器人项目` | 网络爬虫 | requests + XPath 解析、正则表达式、CSV 存储、TMDB 电影榜单爬取 |
| `5.第五章数据分析` | 数据分析 | pandas、matplotlib、Jupyter Notebook、TMDB TOP100 榜单分析 |
| `6.第六章web开发` | Web 开发 | 面向对象高级、FastAPI 实战、「汉字谜盒」AI 猜字谜应用 |

## ✨ 亮点项目

### 🤖 AI 伴侣(第三章)
基于 **DeepSeek 大模型 + Streamlit** 的聊天机器人,从 0.x 到 5.0 逐步迭代:

| 版本 | 功能 |
| --- | --- |
| `ai_partnter.py` | 基础对话 |
| `ai_partnter2.0(滚雪球和流式).py` | 流式输出 |
| `ai_partnter3.0(侧边栏).py` | 侧边栏控制面板 |
| `ai_partnter5.0.py` | 会话历史管理(保存 / 加载 / 删除) |

> ⚠️ 运行前需设置环境变量 `DEEPSEEK_API_KEY`(在 DeepSeek 开放平台申请)。

```bash
cd "3.第三章.AI应用"
streamlit run ai_partnter5.0.py
```

### 🕷️ TMDB 电影榜单爬虫(第四章)
使用 `requests + lxml(XPath)` 爬取 TMDB Top Rated 电影榜单详情,保存为 CSV。

### 📊 TMDB TOP100 电影榜单分析(第五章)
使用 `pandas` 清洗数据 + `matplotlib` 可视化,产出榜单数据统计图。

### 🧩 汉字谜盒(第六章)
**FastAPI + 原生 HTML/CSS/JS + DeepSeek 大模型** 的 AI 猜字谜应用,演示 RESTful API、前后端交互、会话管理(创建 / 查询 / 删除)与 AI 对话记忆。

```bash
cd "6.第六章web开发/汉字谜盒"
python main.py
# 浏览器打开 http://localhost:8000
```

> ⚠️ 需要设置环境变量 `DEEPSEEK_API_KEY`(同第三章)。

## 🚀 快速开始

```bash
# 1. 创建虚拟环境
python -m venv .venv

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行 Jupyter 学习笔记(第五章)
jupyter notebook "5.第五章数据分析"
```

## 📚 学习路线

1. **第一章 · 入门** —— 环境搭建与 Python 基础
2. **第二章 · 核心语法** —— 数据存储与运算、逻辑处理、容器、函数、模块、面向对象
3. **第三章 · AI 应用** —— 大模型 API 调用 + Streamlit 快速搭建应用
4. **第四章 · 网络机器人** —— 爬虫解析 + 数据落盘
5. **第五章 · 数据分析** —— pandas 处理 + matplotlib 可视化
6. **第六章 · Web 开发** —— FastAPI 后端 + 前端页面

## 📝 说明

- 本仓库为**个人学习记录**,代码中包含大量课堂笔记式中文注释,适合初学者对照学习。
- `.venv/`(虚拟环境)、`.idea/`(IDE 配置)、`sessions/`(运行时会话数据)已通过 `.gitignore` 排除,不纳入版本管理。
