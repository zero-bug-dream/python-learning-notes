"""
TMDB TOP100 电影榜单数据统计
功能：读取 TMDB Top100 电影数据，生成四张统计图表（折线图、柱状图×2、饼图）
"""

import os
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import pandas as pd

# 全局配置：中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']

# 数据文件路径（相对于脚本所在目录）
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'movie_list1.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'tmdb_top_100榜单数据统计.png')


def load_data(filepath: str) -> pd.DataFrame:
    """加载 CSV 数据并指定列类型"""
    data = pd.read_csv(
        filepath,
        usecols=['电影名', '电影年份', '电影标签', '电影时长', '电影评分', '电影语言'],
        dtype={'电影时长': 'Int64', '电影评分': float}
    )
    # 数据清洗
    data['电影年份'] = data['电影年份'].fillna('--')
    data['电影标签'] = data['电影标签'].bfill()
    return data


# def plot_yearly_trend(data: pd.DataFrame, ax: Axes) -> None:
#     """需求一：统计每年上映的电影数量变化（折线图）"""
#     year_count = data.groupby(data['电影年份'].str[:4]).count()
#     year_count.columns = ['年份', '电影数量']
#
#     min_year = int(year_count.index.min())
#     max_year = int(year_count.index.max())
#     x = list(range(min_year, max_year + 1))
#     y = [year_count.loc[i, '电影数量'] if i in year_count.index else 0 for i in x]
#
#     ax.plot(x, y)
#     ax.set_xlabel('年份')
#     ax.set_ylabel('电影数量')
#     ax.set_title('每年上映的电影数量变化')
#     ax.set_xticks(x[::10])
#     ax.set_yticks(range(0, 30, 3))
#     ax.grid(linestyle='-.', alpha=0.5)


def plot_language_count(data: pd.DataFrame, ax: Axes) -> None:
    """需求二：统计不同语言电影数量（柱状图）"""
    language_count = data.groupby('电影语言')['电影语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()
    y_language = language_count.values.tolist()

    ax.bar(x_language, y_language, width=0.8)
    ax.set_title('不同语言电影数量', fontsize=20)
    ax.set_xlabel('语言', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.grid(linestyle='-.', alpha=0.5)
    ax.tick_params(axis='x', rotation=45)


def plot_genre_count(data: pd.DataFrame, ax: Axes) -> None:
    """需求三：统计不同标签电影数量（柱状图）"""
    type_count = {}
    for types in data['电影标签'].str.split(',').dropna():
        for t in types:
            type_count[t] = type_count.get(t, 0) + 1

    x_ticks = list(type_count.keys())
    y_ticks = list(type_count.values())

    ax.bar(x_ticks, y_ticks, width=0.8)
    ax.set_title('不同标签电影数量', fontsize=20)
    ax.set_xlabel('标签', fontsize=12)
    ax.set_ylabel('电影数量', fontsize=12)
    ax.grid(linestyle='-.', alpha=0.5)
    ax.tick_params(axis='x', rotation=45)


def plot_score_distribution(data: pd.DataFrame, ax: Axes) -> None:
    """需求四：统计各个评分的电影占比（饼状图）"""
    score_count = data.groupby('电影评分')['电影评分'].count()

    total = score_count.sum()
    large_score = score_count.loc[score_count > total * 0.04].copy()
    small_score = score_count.loc[score_count <= total * 0.04]

    if small_score.shape[0] > 0:
        large_score['其他'] = small_score.sum()

    scores = large_score.index.tolist()
    scores_values = large_score.values.tolist()

    ax.pie(scores_values, labels=scores, autopct='%1.2f%%', startangle=90, radius=1)
    ax.set_title('各个评分的电影占比', fontsize=20)
    ax.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))


def main():
    # 加载数据
    data = load_data(DATA_FILE)

    # 创建 2x2 子图
    figure, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10), dpi=100)
    figure.suptitle('tmdb_top_100榜单数据统计', fontsize=25,x =0.5, y =0.98)
    figure.subplots_adjust(hspace=0.5, wspace=0.2)

    # 绘制四张图表
    # plot_yearly_trend(data, axes[0, 0])
    plot_language_count(data, axes[0, 1])
    plot_genre_count(data, axes[1, 0])
    plot_score_distribution(data, axes[1, 1])

    # 保存并显示
    plt.savefig(OUTPUT_FILE)
    plt.show()


if __name__ == '__main__':
    main()
