'''

'''

import requests

from bs4 import BeautifulSoup
from sympy import div

url = "https://www.runoob.com/python3/python3-basic-syntax.html"

res = requests.get(url)

soup = BeautifulSoup(res.text,features="lxml")

# 获取对应属性的值

# find、find_all 方法

soup.find("div",attrs={"class:"},)