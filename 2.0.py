import requests
from bs4 import BeautifulSoup

url = "http://fx.sjtulib.superlib.net/s?sw=python"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # 添加超时设置(连接超时,读取超时)
    response = requests.get(url, headers=headers, timeout=(3.05, 10))
    response.raise_for_status()  # 检查请求是否成功

    # 显式设置编码（根据实际网页调整）
    response.encoding = response.apparent_encoding  # 或直接指定 'utf-8'

    # 使用lxml解析器（需确保已安装lxml库）
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('title')

    # 更友好的输出方式
    if title:
        print("网页标题:", title.text.strip())
    else:
        print("未找到标题标签")

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"其他错误: {e}")