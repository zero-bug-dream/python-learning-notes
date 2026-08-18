# -*- coding: utf-8 -*-
"""
TMDB 高分电影 Top100 爬虫
=========================
爬取 https://www.themoviedb.org/movie/top-rated 共5页(每页20部)的100部电影,
解析每部电影的11项详情字段并保存到 csv_data/movie_list.csv

依赖安装：
    pip install requests lxml
"""

import requests
from lxml import etree
import csv
import os
import time

# ============================================================
# 一、常量配置
# ============================================================
BASE_URL = "https://www.themoviedb.org"
TOP_RATED_URL = f"{BASE_URL}/movie/top-rated"  # 第1页 GET
DISCOVER_URL = f"{BASE_URL}/discover/movie/items"  # 第2~5页 POST
TOTAL_PAGES = 5  # 共5页
PER_PAGE = 20  # 每页20部
REQUEST_DELAY = 1.2  # 每次请求强制延时(秒),规避IP封禁
OUTPUT_DIR = "csv_data"  # 输出目录
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "movie_list.csv")

# 表头(11项详情字段)
CSV_HEADERS = [
    "电影名", "上映时间", "电影类型", "电影时长", "电影评分百分比",
    "原始电影语言", "电影导演", "主演演员", "编剧/作者",
    "电影宣传口号tagline", "剧情简介",
]

# 完整浏览器请求头: 携带 UA + Accept-Language, 规避 403 BLOCKED_CLIENT 拦截
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,application/signed-exchange;v=b3;q=0.9,*/*;q=0.8"
    ),
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.themoviedb.org/movie/top-rated",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "sec-ch-ua": '"Chromium";v="120", "Not_A Brand";v="8", "Google Chrome";v="120"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
}

# POST 分页表单参数(截图全套表单, 仅 page 字段随页码变化)
# 不要删除任何参数, 保证多页数据正常加载
FORM_DATA = {
    "language": "zh",
    "sort_by": "vote_average.desc",
    "vote_count.gte": "300",
    "with_original_language": "",
    "with_genres": "",
    "without_genres": "",
    "release_date.gte": "",
    "release_date.lte": "",
    "region": "",
    "page": "1",
}


# ============================================================
# 二、xpath 工具函数 (安全封装, 杜绝 list[0] 索引越界)
# ============================================================
def safe_xpath_text(tree, xpath_expr, default=""):
    """
    安全获取单个节点的文本, 节点不存在返回 default
    支持 xpath 返回字符串列表或元素列表两种情况
    """
    try:
        result = tree.xpath(xpath_expr)
        if not result:
            return default
        # 取第一个, 处理 lxml 元素或字符串两种返回
        first = result[0]
        if isinstance(first, str):
            return first.strip()
        # 元素节点: 取 text
        text = first.text if first.text is not None else ""
        # 也拼上尾巴 (如 <a>标题<span>...</span>尾巴</a>)
        tail_text = "".join(first.itertext()) if hasattr(first, "itertext") else text
        return (tail_text or text).strip()
    except Exception:
        return default


def safe_xpath_attr(tree, xpath_expr, attr, default=""):
    """安全获取节点属性, 不存在返回 default"""
    try:
        result = tree.xpath(f"{xpath_expr}/@{attr}")
        if result and len(result) > 0:
            return result[0].strip()
        return default
    except Exception:
        return default


def safe_xpath_join(tree, xpath_expr, sep=",", default=""):
    """
    安全获取多节点文本, 用 sep 拼接成一个字符串
    适用于 多导演 / 多主演 / 多编剧 / 多类型
    """
    try:
        result = tree.xpath(xpath_expr)
        if not result:
            return default
        items = []
        for node in result:
            if isinstance(node, str):
                txt = node.strip()
            else:
                # 元素节点
                txt = "".join(node.itertext()).strip() if hasattr(node, "itertext") else (node.text or "").strip()
            if txt:
                items.append(txt)
        return sep.join(items) if items else default
    except Exception:
        return default


def get_first_text(tree, xpath_list, default=""):
    """
    多备选 xpath 模式: 依次尝试列表中的 xpath, 返回第一个非空结果
    适应 TMDB 页面 DOM 多版本结构
    """
    for expr in xpath_list:
        val = safe_xpath_text(tree, expr, default="")
        if val:
            return val
    return default


# ============================================================
# 三、单电影详情爬取函数
# ============================================================
def fetch_movie_detail(url):
    """
    请求电影详情页并解析 11 项字段, 返回 dict
    单电影解析异常会被单独捕获, 失败时填充空数据不终止程序
    """
    # 预置空数据 (失败时返回这个)
    data = {key: "" for key in CSV_HEADERS}

    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        # 显式声明编码 (TMDB 默认 utf-8)
        if resp.encoding and resp.encoding.lower() != "utf-8":
            resp.encoding = "utf-8"
        tree = etree.HTML(resp.text)

        # 1. 电影名 (多版本结构回退)
        data["电影名"] = get_first_text(tree, [
            '//h2[@class="7"]/a/text()',
            '//div[contains(@class,"header_info")]/h2/a/text()',
            '//section[contains(@class,"header")]//h2//a/text()',
            '//div[contains(@class,"title")]/h2/a/span/text()',
            '//h2[@itemprop="name"]/a/text()',
        ])

        # 2. 上映时间 (取括号内年份或 release_date 文本)
        release = get_first_text(tree, [
            '//h2[@class="7"]/span[@class="release_date"]/text()',
            '//span[@class="release_date"]/text()',
            '//div[contains(@class,"header_info")]//span[@class="release_date"]/text()',
            '//section[contains(@class,"header")]//span[contains(@class,"release")]/text()',
        ])
        if release:
            # 形如 (2023-05-18) -> 去括号
            data["上映时间"] = release.strip("() ").strip()

        # 3. 电影类型 (多个用逗号拼接)
        data["电影类型"] = safe_xpath_join(tree, '//ul[contains(@class,"genres")]/li/a/text()', sep=",") or \
                           safe_xpath_join(tree, '//span[@class="genres"]/a/text()', sep=",") or \
                           safe_xpath_join(tree, '//p[contains(@class,"genres")]/a/text()', sep=",")

        # 4. 电影时长
        data["电影时长"] = get_first_text(tree, [
            '//section[contains(@class,"facts")]//p[@class="runtime"]/text()',
            '//p[contains(@class,"runtime")]/text()',
            '//span[@class="runtime"]/text()',
            '//*[contains(text(),"时长")]/following-sibling::text()',
        ])

        # 5. 电影评分百分比 (data-percent 属性优先, 回退文本)
        data["电影评分百分比"] = safe_xpath_attr(
            tree, '//div[contains(@class,"user_score_chart")]', "data-percent"
        ) or safe_xpath_attr(
            tree, '//div[@class="percent_circle"]', "data-percent"
        ) or get_first_text(tree, [
            '//div[contains(@class,"user_score_chart")]/text()',
            '//div[@class="percent_circle"]/div[@class="icon_r"]/text()',
            '//*[@class="no_pad"]/div[contains(@class,"percent")]/text()',
        ])

        # 6. 原始电影语言
        data["原始电影语言"] = get_first_text(tree, [
            '//*[contains(text(),"原始语言")]/following-sibling::text()',
            '//section[contains(@class,"facts")]//strong[contains(text(),"原始语言")]/following-sibling::text()',
            '//p[contains(@class,"genres")]/following-sibling::p[contains(text(),"语言")]/text()',
            '//bdi/following-sibling::text()[contains(.,"语言")]',
        ])
        data["原始电影语言"] = data["原始电影语言"].lstrip("：: ").strip()

        # 7. 电影导演 (多位逗号拼接, 在 People 区按 "Directing" 过滤)
        data["电影导演"] = safe_xpath_join(
            tree,
            '//ol[contains(@class,"people")]/li[contains(@class,"director")]/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//section[@id="director"]//a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//div[contains(@class,"crew")]/p[@class="name"]/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//p[contains(text(),"导演")]/following-sibling::ul[1]/li/a/text()',
            sep=",",
        )

        # 8. 主演演员 (多位逗号拼接)
        data["主演演员"] = safe_xpath_join(
            tree,
            '//ol[contains(@class,"people")]/li[@class="card"]/p[@class="name"]/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//ol[@class="people scroller"]/li/p[@class="name"]/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//section[@id="cast"]//p[@class="name"]/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//div[contains(@class,"cast")]/p[@class="name"]/a/text()',
            sep=",",
        )

        # 9. 编剧/作者 (Writing 部门)
        data["编剧/作者"] = safe_xpath_join(
            tree,
            '//ol[contains(@class,"people")]/li[contains(@class,"writer")]/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//section[@id="writer"]//a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//p[contains(text(),"编剧")]/following-sibling::ul[1]/li/a/text()',
            sep=",",
        ) or safe_xpath_join(
            tree,
            '//*[contains(text(),"编剧")]/following-sibling::a/text()',
            sep=",",
        )

        # 10. 电影宣传口号 tagline
        data["电影宣传口号tagline"] = get_first_text(tree, [
            '//h3[@class="tagline"]/text()',
            '//p[@class="tagline"]/text()',
            '//*[@class="tagline"]//text()',
            '//*[@itemprop="tagline"]/text()',
        ])

        # 11. 剧情简介
        data["剧情简介"] = get_first_text(tree, [
            '//div[@class="overview"]/p/text()',
            '//*[@itemprop="description"]/p/text()',
            '//div[contains(@class,"overview")]//p/text()',
            '//*[@class="overview"]/text()',
        ])

    except requests.exceptions.RequestException as e:
        print(f"  [详情请求失败] {url} -> {e}")
    except Exception as e:
        # 单电影详情解析异常单独捕获, 不终止整个程序
        print(f"  [详情解析异常] {url} -> {e}")

    return data


# ============================================================
# 四、保存 csv 函数
# ============================================================
def save_to_csv(rows, is_append=False):
    """
    将电影数据列表写入 csv_data/movie_list.csv
    - 自动检测并创建 csv_data 文件夹
    - utf-8-sig 编码解决 Excel 中文乱码
    - 第一次写入表头, 后续追加不加表头
    """
    if not rows:
        return
    # 自动创建目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"[创建目录] {OUTPUT_DIR}")

    # 判断写入模式: 文件不存在或非追加 -> 写表头
    write_header = (not is_append) or (not os.path.exists(OUTPUT_FILE))
    mode = "a" if is_append else "w"

    try:
        with open(OUTPUT_FILE, mode, newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
            if write_header:
                writer.writeheader()
            for row in rows:
                writer.writerow(row)
        print(f"[保存成功] 本次写入 {len(rows)} 条, 累计文件: {OUTPUT_FILE}")
    except Exception as e:
        print(f"[保存失败] {e}")


# ============================================================
# 五、主分页爬取逻辑
# ============================================================
def parse_card_list(tree):
    """
    从分页 HTML 中解析电影卡片列表
    DOM: <div class="media-list-results contents"> 下的子div卡片
    每张卡片提取海报 a 标签 href 拼接完整详情页 url
    返回 url 列表
    """
    urls = []
    try:
        # 所有电影卡片都在 media-list-results contents 下的子div
        cards = tree.xpath('//div[contains(@class,"media-list-results") and contains(@class,"contents")]/div')
        if not cards:
            # 回退: 直接找卡片
            cards = tree.xpath('//div[contains(@class,"card style_1")]') or \
                    tree.xpath('//div[@class="card style_1"]')

        for card in cards:
            try:
                # 提取海报 a 标签 href
                href = safe_xpath_attr(card, './/a[contains(@href,"/movie/")]', "href")
                if not href:
                    href = safe_xpath_attr(card, './/a', "href")
                if href:
                    # 拼接完整详情页 url
                    full_url = href if href.startswith("http") else BASE_URL + href
                    if full_url not in urls:
                        urls.append(full_url)
            except Exception:
                continue
    except Exception as e:
        print(f"  [卡片列表解析失败] -> {e}")
    return urls


def crawl_page(page_num):
    """
    抓取单页: 第1页用 GET, 第2~5页用 POST
    分页请求异常会被单独捕获, 失败返回空列表不终止程序
    """
    print(f"\n========== 开始抓取第 {page_num} 页 ==========")
    try:
        if page_num == 1:
            # 第1页 GET
            resp = requests.get(TOP_RATED_URL, headers=HEADERS, timeout=15)
        else:
            # 第2~5页 POST, 仅修改 page 字段
            form = FORM_DATA.copy()
            form["page"] = str(page_num)
            resp = requests.post(DISCOVER_URL, data=form, headers=HEADERS, timeout=15)

        resp.raise_for_status()
        if resp.encoding and resp.encoding.lower() != "utf-8":
            resp.encoding = "utf-8"

        # 检测是否被拦截
        if "BLOCKED_CLIENT" in resp.text or resp.status_code == 403:
            print(f"  [拦截警告] 第 {page_num} 页被 403 BLOCKED_CLIENT 拦截, 跳过")
            return []

        tree = etree.HTML(resp.text)
        movie_urls = parse_card_list(tree)
        print(f"  [第 {page_num} 页] 共解析到 {len(movie_urls)} 部电影卡片")
        return movie_urls

    except requests.exceptions.RequestException as e:
        # 分页请求异常单独捕获
        print(f"  [分页请求失败] 第 {page_num} 页 -> {e}")
        return []
    except Exception as e:
        print(f"  [分页处理异常] 第 {page_num} 页 -> {e}")
        return []


def main():
    print("=" * 60)
    print("TMDB 高分电影 Top100 爬虫启动")
    print(f"目标: {TOTAL_PAGES} 页, 每页 {PER_PAGE} 部, 共 {TOTAL_PAGES * PER_PAGE} 部")
    print(f"输出: {OUTPUT_FILE}")
    print("=" * 60)

    # 初始化输出文件 (首次写入会带表头)
    all_rows = []
    total_collected = 0

    for page in range(1, TOTAL_PAGES + 1):
        movie_urls = crawl_page(page)

        if not movie_urls:
            print(f"  [跳过] 第 {page} 页无电影链接, 进入下一页")
            time.sleep(REQUEST_DELAY)
            continue

        page_rows = []
        for idx, url in enumerate(movie_urls, start=1):
            print(f"  [第 {page} 页 {idx}/{len(movie_urls)}] 采集: {url}")
            try:
                row = fetch_movie_detail(url)
                page_rows.append(row)
                total_collected += 1
                print(f"    -> 电影名: {row.get('电影名', '')[:30]} | 评分: {row.get('电影评分百分比', '')}")
            except Exception as e:
                # 兜底: 单电影任何未捕获异常都补空行, 不影响后续
                print(f"    [单电影兜底异常] {url} -> {e}")
                page_rows.append({key: "" for key in CSV_HEADERS})

            # 强制延时, 防止 IP 封禁
            time.sleep(REQUEST_DELAY)

        # 每页结束追加保存一次 (断点续存, 防止中途崩溃丢数据)
        save_to_csv(page_rows, is_append=(page > 1 or total_collected > len(page_rows)))
        all_rows.extend(page_rows)
        print(f"  [第 {page} 页完成] 累计采集 {total_collected} 部")

    print("\n" + "=" * 60)
    print(f"爬取完成! 共采集 {total_collected} 部电影")
    print(f"数据文件: {os.path.abspath(OUTPUT_FILE)}")
    print("=" * 60)


if __name__ == "__main__":
    main()