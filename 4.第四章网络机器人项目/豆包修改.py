import requests
import csv
import re
import time
import os
from lxml import html

# ===================== 常量配置 =====================
tmdb_base_url = "https://www.themoviedb.org"
tmdb_top_url_1 = "https://www.themoviedb.org/movie/top-rated"
tmdb_top_url_2 = "https://www.themoviedb.org/discover/movie/items"
movie_list_file = "csv_data/movie_list2.csv"
# 请求头，模拟浏览器，绕过基础反爬
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Referer": "https://www.themoviedb.org/movie/top-rated"
}
REQUEST_DELAY = 1.5  # 每次请求间隔1.5秒，防封禁
MAX_RETRY = 2         # 请求失败最大重试次数

# ===================== 工具函数 =====================
def get_movie_year(movie_years):
    """清洗年份，修复原代码多余逗号bug"""
    if not movie_years:
        return ""
    movie_year = movie_years.strip()
    return movie_year.replace("(", "").replace(")", "")

def get_movie_cost_time(time_list):
    """解析时长统一转分钟，增加空值判断，避免索引报错"""
    if not time_list:
        return 0
    time_str = time_list[0].strip()
    h_res = re.search(r"(\d+)h", time_str)
    m_res = re.search(r"(\d+)m", time_str)
    h = int(h_res.group(1)) if h_res else 0
    m = int(m_res.group(1)) if m_res else 0
    return h * 60 + m

def safe_xpath(doc, xpath_expr):
    """封装XPath安全获取，统一处理空列表，避免[0]索引崩溃"""
    result = doc.xpath(xpath_expr)
    return result if result else []

def send_request(url, method="GET", data=None, retry=0):
    """封装请求函数，统一处理超时、重试、请求头"""
    try:
        time.sleep(REQUEST_DELAY)
        if method.upper() == "GET":
            resp = requests.get(url, headers=HEADERS, timeout=60)
        else:
            resp = requests.post(url, headers=HEADERS, data=data, timeout=60)
        resp.raise_for_status()  # 状态码非200直接抛异常
        return resp
    except Exception as e:
        if retry < MAX_RETRY:
            print(f"请求失败 {url}，重试 {retry+1}/{MAX_RETRY}，错误：{str(e)}")
            time.sleep(2)
            return send_request(url, method, data, retry + 1)
        else:
            print(f"请求 {url} 多次失败，放弃，错误：{str(e)}")
            return None

# ===================== 电影详情抓取 =====================
def get_movie_info_url(movie_info_url):
    print(f"发送请求 {movie_info_url}，获取电影详情 ...")
    resp = send_request(movie_info_url, method="GET")
    if not resp:
        return {}
    movie_doc = html.fromstring(resp.text)

    # 安全xpath提取所有字段
    movie_names = safe_xpath(movie_doc, "//img/@alt")
    movie_years = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    movie_tags = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    movie_cost_time = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    movie_scores = safe_xpath(movie_doc, "//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_lag = safe_xpath(movie_doc, "//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movies_directors = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movies_actors = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_authors = safe_xpath(movie_doc, "//*[@id='cast_scroller']/ol/li[1]/a/div/img/@alt")
    movies_slogan = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_jianjie = safe_xpath(movie_doc, "//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    movie_info = {
        "电影名": movie_names[1].strip() if len(movie_names) >= 2 else "",
        "电影年份": get_movie_year(movie_years[0] if movie_years else ""),
        "电影标签": ",".join([tag.strip() for tag in movie_tags]),
        "电影时长": get_movie_cost_time(movie_cost_time),
        "电影评分": movie_scores[0].strip() if movie_scores else "",
        "电影语言": movie_lag[0].strip() if movie_lag else "",
        "电影导演": ",".join([d.strip() for d in movies_directors]),
        "电影演员": ",".join([a.strip() for a in movies_actors]),
        "电影作者": movie_authors[0].strip() if movie_authors else "",
        "电影口号": movies_slogan[0].strip() if movies_slogan else "",
        "电影简介": movie_jianjie[0].strip() if movie_jianjie else "",
    }
    return movie_info

# ===================== CSV保存 =====================
def save_all_movies(all_movies):
    # 自动创建文件夹
    folder_path = os.path.dirname(movie_list_file)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # 写入csv
    field_names = ["电影名","电影年份","电影标签","电影时长","电影评分","电影语言","电影导演","电影演员","电影作者","电影口号","电影简介"]
    with open(movie_list_file, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(all_movies)
    print(f"数据已保存至 {movie_list_file}，共抓取 {len(all_movies)} 部电影")

# ===================== 主逻辑 =====================
def main():
    all_movies = []
    # 循环1~5页
    for page_num in range(1, 6):
        print(f"\n===== 开始抓取第 {page_num} 页榜单 =====")
        if page_num == 1:
            resp = send_request(tmdb_top_url_1, method="GET")
        else:
            # POST表单必须传字典，修复原代码字符串传参错误
            post_form_data = {
                "air_date.gte": "",
                "air_date.lte": "",
                "certification": "",
                "certification_country": "CN",
                "debug": "",
                "first_air_date.gte": "",
                "first_air_date.lte": "",
                "include_adult": "false",
                "include_softcore": "false",
                "latest_ceremony.gte": "",
                "latest_ceremony.lte": "",
                "page": page_num,
                "primary_release_date.gte": "",
                "primary_release_date.lte": "",
                "region": "",
                "release_date.gte": "",
                "release_date.lte": "2027-02-10",
                "show_me": "everything",
                "sort_by": "vote_average.desc",
                "vote_average.gte": 0,
                "vote_average.lte": 10,
                "vote_count.gte": 300,
                "watch_region": "CN",
                "with_genres": "",
                "with_keywords": "",
                "with_networks": "",
                "with_origin_country": "",
                "with_original_language": "",
                "with_watch_monetization_types": "",
                "with_watch_providers": "",
                "with_release_type": "",
                "with_runtime.gte": 0,
                "with_runtime.lte": 400
            }
            resp = send_request(tmdb_top_url_2, method="POST", data=post_form_data)

        if not resp:
            print(f"第{page_num}页榜单请求失败，跳过当前页")
            continue
        document = html.fromstring(resp.text)
        movie_list = safe_xpath(document, "//div[@class='media-list-results contents']/div")
        print(f"第{page_num}页检测到 {len(movie_list)} 部电影")

        # 遍历单页所有电影
        for movie in movie_list:
            movie_urls = safe_xpath(movie, ".//a/@href")
            if not movie_urls:
                continue
            full_url = tmdb_base_url + movie_urls[0]
            movie_info = get_movie_info_url(full_url)
            if movie_info:
                all_movies.append(movie_info)

    # 全部抓取完成保存
    save_all_movies(all_movies)

if __name__ == "__main__":
    main()