import requests
from bs4 import BeautifulSoup

# 配置请求参数
url = "http://fx.sjtulib.superlib.net/s?sw=python"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 发送请求
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 检查请求是否成功

    # 设置编码
    response.encoding = 'utf-8'

    # 解析HTML
    soup = BeautifulSoup(response.text, 'lxml')

    # 查找主容器
    main_list = soup.find('div', id='mainlist')
    if not main_list:
        raise ValueError("未找到 id='mainlist' 的 div 元素")

    # 处理每个图书条目
    for book_item in main_list.find_all('div', class_='fr zyList_right'):
        # 提取书名
        book_name = book_item.find('a').get_text(strip=True)
        print(f"书名: {book_name}")

        # 提取详细信息
        labels = book_item.find_all('span', class_='fl col9')
        values = book_item.find_all('div', class_='fl zylist_font')

        # 确保标签和值数量匹配
        min_length = min(len(labels), len(values))
        for i in range(min_length):
            print(f"{labels[i].get_text(strip=True)}: {values[i].get_text(strip=True)}")

        print("-" * 40)  # 分隔线

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"程序出错: {e}")