"""
爬取豆瓣评论
"""
from PIL import Image

from cgitb import html

import requests

from bs4 import BeautifulSoup

import jieba

from jieba import analyse

from matplotlib import pyplot as plt

import wordcloud

import numpy as np



def crawl(num):
    for i in range(20,num,20):
        url = "https://movie.douban.com/subject/25845392/comments?start={}&limit=20&status=P&sort=new_score".format(i)

        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55"}

        res = requests.get(url,headers=header)

        if res.status_code==200:
    
            res.encoding = "utf-8"
    
            soup = BeautifulSoup(res.text,"html.parser")

            comment = soup.find_all("p",attrs={"class":"comment-content"})

            with open("./Code/data/data4.txt","a",encoding="utf-8") as f:

                for i in comment:
                    f.write(i.span.text +"\n")
