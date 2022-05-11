"""
实验1、2
"""

"""
爬取豆瓣评论
"""
from tracemalloc import stop

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
    """
    爬取豆瓣评论
    """
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

def show_word_cloud(path,mode):
    '''
    使用两种方式来处理文本
    '''

    word_dict = dict()
    with open(path) as f:
        if mode == 1:
            key_word = analyse.extract_tags(f.read(),topK=50,withWeight=True)
            for i in key_word:
                word_dict[i[0]]=i[1]

        elif mode == 2:
            # 分词
            cut_word_list = jieba.lcut(f.read())

            # 加载停用词库

            with open("./Data/哈工大停用词表.txt") as f1:
                stop_word_list = [i.strip() for i in f1.readlines()]

            # 过滤停用词

            word_list = []

            for i in cut_word_list:
                if i not in stop_word_list:
                    word_list.append(i)

            # 统计词频

            for i in word_list:
                word_dict[i] = word_dict.get(i,0)+1            
    
    # 词云展示

    mask = np.array(Image.open("./Code/save_img/flower.png"))

    wc = wordcloud.WordCloud(font_path="D:/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf",
    mask=mask,max_words=50)

    # 加载文本以及词频
    wc.generate_from_frequencies(word_dict)

    image_colors = wordcloud.ImageColorGenerator(mask)

    wc.recolor(color_func=image_colors)

    plt.imshow(wc)

    plt.axis("off")

    plt.show()

        
if __name__=="__main__":
    show_word_cloud("./Code/data/data4.txt",2)
