import requests

import csv

from lxml import html

import re
# 常量
tmdb_base_url = "https://www.themoviedb.org"
tmdb_top_url_1 = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的URL(只能访问第一页数据)
tmdb_top_url_2 = "https://www.themoviedb.org/discover/movie/items"

movie_list_file = "csv_data/movie_list2.csv" # 电影列表文件
# https://www.themoviedb.org/movie/980431-avatar-aang-the-last-airbender
# 主函数 :定义核心逻辑
# 获取电影年份
def get_movie_year(movie_years):
    movie_year = movie_years[0].strip() if movie_years else '',
    return re.search(r"\d{4}-\d{2}-\d{2}", movie_year).group(0)

# 获取电影时长(统一转换为分钟)
def get_movie_cost_time(movie_cost_time):
    movie_cost_time = movie_cost_time[0].strip() if movie_cost_time else ''
    h_res = re.search(r"(\d+)h", movie_cost_time)
    m_res = re.search(r"(\d+)m", movie_cost_time)
    h = int(h_res.group(1) if h_res else 0)
    m = int(m_res.group(1) if m_res else 0)
    return h * 60 + m

def get_movie_info_url(movie_info_url):# 获取每部电影的详情
    # 1 发送请求
    movie_response = requests.get(movie_info_url,timeout= 60 )
    print(f"发送请求{movie_info_url},获取电影详情 ...")

    # 2 解析数据,获取电影详情
    movie_doc = html.fromstring(movie_response.text)
    # 电影名称
    movie_names = movie_doc.xpath("//img/@alt")[1]
    movie_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")[0]

    movie_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    movie_cost_time = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")[0]
    movie_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    movie_lag = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    movies_directors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[1]/p[1]/a/text()")
    movies_actors = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/ol/li[2]/p[1]/a/text()")
    movie_authors = movie_doc.xpath("//*[@id='cast_scroller']/ol/li[1]/a/div/img/@alt")
    movies_slogan = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    movie_jianjie = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div/p/text()")

    # 3.返回电影详情
    movie_info = {
        "电影名": movie_names.strip() if movie_names else '',
        "电影年份": get_movie_year(movie_years),
        "电影标签": ",".join(movie_tags) if movie_tags else '',
        "电影时长": get_movie_cost_time(movie_cost_time),
        "电影评分": movie_scores[0].strip() if movie_scores else '',
        "电影语言": movie_lag[0].strip() if movie_lag else '',
        "电影导演": ",".join(movies_directors) if movies_directors else '',
        "电影演员": ",".join(movies_actors) if movies_actors else '',
        "电影作者": movie_authors[0].strip() if movie_authors else '',
        "电影口号": movies_slogan[0].strip() if movies_slogan else '',
        "电影简介": movie_jianjie[0].strip() if movie_jianjie else '',
    }

    return movie_info

def save_all_movies(all_movies):# 保存所有电影信息
    with open(movie_list_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile ,fieldnames = ["电影名","电影年份","电影标签","电影时长","电影评分","电影语言","电影导演","电影演员","电影作者","电影口号","电影简介"])
        writer.writeheader()
        writer.writerows(all_movies)

def main():
    all_movies = []  # 存储所有电影信息
    # 循环获取多页数据(1-5页 共100个电影)
    for page_num in range(1, 6):
        # 1.发送HTTP请求
        if page_num == 1:
            response = requests.get(tmdb_top_url_1, timeout=60)
        else:
            response = requests.post(tmdb_top_url_2,
                                        data = f"air_date.gte=&air_date.lte=&certification=&certification_country=CN&debug=&first_air_date.gte=&first_air_date.lte=&include_adult=false&include_softcore=false&latest_ceremony.gte=&latest_ceremony.lte=&page={(page_num)}&primary_release_date.gte=&primary_release_date.lte=&region=&release_date.gte=&release_date.lte=2027-02-10&show_me=everything&sort_by=vote_average.desc&vote_average.gte=0&vote_average.lte=10&vote_count.gte=300&watch_region=CN&with_genres=&with_keywords=&with_networks=&with_origin_country=&with_original_language=&with_watch_monetization_types=&with_watch_providers=&with_release_type=&with_runtime.gte=0&with_runtime.lte=400",
                                        timeout=60)
        print(f"发送请求,访问第{page_num}页获取TMDB榜单数据 ...")

        # 2.解析数据,获取电影列表
        document = html.fromstring(response.text)
        # movie_list = document.xpath("/html/body/div[2]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[1]/div/div[@class='w-full overflow-hidden rounded-xl border border-gray-200 bg-white shadow-sm transition-colors hover:border-gray-300']")
        movie_list = document.xpath("//div[@class='media-list-results contents']/div")
        # 3.遍历电影列表,获取每部电影的详情

        for movie in movie_list:
            movie_urls = movie.xpath(".//a/@href")
            if movie_urls:
                movie_info_url = tmdb_base_url + movie_urls[0]
                movie_info = get_movie_info_url(movie_info_url)  # 获取每部电影的详情
                all_movies.append(movie_info)

    # 4.保存到csv文件中
    print("保存所有电影信息到CSV文件中 ...")
    save_all_movies(all_movies)


if __name__ == "__main__":
    main()