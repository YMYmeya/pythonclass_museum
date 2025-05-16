import requests
from bs4 import BeautifulSoup

url = "http://fx.sjtulib.superlib.net/s?sw=python"

try:
    # 添加headers模拟浏览器访问，设置超时时间
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # 检查请求是否成功

    # 明确指定编码（根据实际网页编码调整）
    response.encoding = 'utf-8'
    html = response.text

    # 使用html.parser解析器（避免依赖外部lxml库）
    soup = BeautifulSoup(html, 'html.parser')
    paragraphs = soup.find_all('p')  # 变量名使用有意义的全称

    print(paragraphs)

except requests.exceptions.RequestException as e:
    print(f"请求出错: {e}")
except Exception as e:
    print(f"其他错误: {e}")