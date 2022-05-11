"""
爬取东软学院的学院简介
"""

from sqlite3 import enable_callback_tracebacks
from tkinter import W
import requests

from bs4 import BeautifulSoup
from sympy import N

# 爬取页面信息

res = requests.get("https://nsu.edu.cn/HTML/dept/")

res.encoding = "utf-8"


soup = BeautifulSoup(res.text,"lxml")

div_item = soup.find_all("div",attrs={"class":"plate-w-w"})

for i in div_item:
    with open("./data/text.txt","a",encoding="utf-8") as f:
        f.write(i.text+"\n")

