"""
尝试爬虫
"""

# 导入所需包

import requests

from bs4 import BeautifulSoup

# 要爬取的网站

url = "https://www.w3school.com.cn/python/index.asp"

url_head = "https://www.w3school.com.cn"

res = requests.get(url)

# 查看其状态码

print(res.status_code)
print(res.encoding)

# 创建 beautifulsoup对象

soup = BeautifulSoup(res.text,features="lxml")

# 获取本网页的所有链接

itms = soup.find("div",attrs={"id":"course"})

ul_itms = itms.ul

# 找到所有的a标签
a_itms = ul_itms.find_all("a")
print(len(a_itms))
for i in a_itms:
    url_result = url_head+i["href"]
    print(i["title"]+":"+url_result)
# 检查是否正确


