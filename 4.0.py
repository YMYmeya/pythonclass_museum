import requests
from bs4 import BeautifulSoup

# 目标URL（确保URL完整不换行）
url = "http://fx.sjtulib.superlib.net/s?sw=python"

# 设置请求头模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

try:
    # 添加超时设置（连接超时3秒，读取超时10秒）
    response = requests.get(url, headers=headers, timeout=(3, 10))
    response.raise_for_status()  # 检查HTTP请求是否成功

    # 显式设置编码（根据实际网页编码调整）
    response.encoding = 'utf-8'

    # 使用lxml解析器（确保已安装lxml: pip install lxml）
    soup = BeautifulSoup(response.text, 'lxml')

    # 查找特定class的p标签（class_带下划线避免Python关键字冲突）
    paragraphs = soup.find_all('p', class_='hitsNum')

    # 更友好的输出方式
    if paragraphs:
        for i, p in enumerate(paragraphs, 1):
            print(f"第{i}个结果:", p.text.strip())
    else:
        print("未找到class='hitsNum'的<p>标签")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"其他错误: {e}")