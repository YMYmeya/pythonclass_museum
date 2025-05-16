import requests
from bs4 import BeautifulSoup
import time
from random import uniform

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 页码列表
pages = [1, 3, 5, 7, 9]

for page in pages:
    try:
        # 构造URL
        url = f"http://fx.sjtulib.superlib.net/s?sw=python&size=15&isort=&x=788_1071&pages={page}&version=v2"

        # 发送请求
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # 检查请求是否成功
        response.encoding = 'utf-8'  # 设置编码

        # 解析HTML
        soup = BeautifulSoup(response.text, 'lxml')

        # 查找主容器
        main_list = soup.find('div', id='mainlist')
        if not main_list:
            print(f"第 {page} 页未找到 id='mainlist' 的 div 元素")
            continue

        # 处理每个图书条目
        for book_item in main_list.find_all('div', class_='fr zyList_right'):
            try:
                # 提取书名
                book_name = book_item.find('a').get_text(strip=True)
                print(f"\n书名: {book_name}")

                # 提取详细信息
                labels = book_item.find_all('span', class_='fl col9')
                values = book_item.find_all('div', class_='fl zylist_font')

                # 确保标签和值数量匹配
                for label, value in zip(labels, values):
                    print(f"{label.get_text(strip=True)}: {value.get_text(strip=True)}")

            except Exception as e:
                print(f"处理图书条目时出错: {e}")
                continue

        # 随机延迟，避免请求过于频繁
        time.sleep(uniform(0.5, 2))

    except requests.exceptions.RequestException as e:
        print(f"请求第 {page} 页出错: {e}")
        continue
    except Exception as e:
        print(f"处理第 {page} 页时出错: {e}")
        continue

print("所有页面处理完成")