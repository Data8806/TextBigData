"""
爬取专业介绍
"""
import requests

from bs4 import BeautifulSoup
import wordcloud

url = "https://cs.nsu.edu.cn/bc58263d-c6bd-4d2b-a0d4-65cd2c9e0f20.html"

head_url = url[:url.rfind("/")+1]


res = requests.get(url)

res.encoding = "utf-8"

if res.status_code == 200:

    soup = BeautifulSoup(res.text,"lxml")

    ul = soup.find("ul",attrs={"style":"display: flow-root;"})

    li_item = ul.find_all("li")

    for i in li_item:

        new_url = head_url+i.a["href"]

        new_res = requests.get(new_url)
        new_res.encoding = "utf-8"

        if new_res.status_code == 200:

            with open("D:\\TextBigData\\Code\\data\\data3.txt","a",encoding="utf-8") as f:

                new_soup = BeautifulSoup(new_res.text,"lxml")

                title_text = new_soup.find("div",attrs={"class":"h-1"}).text
                # print(title_text)

                f.write(title_text+"\n")

                div_label = new_soup.find("div",attrs={"class":"text_"})
                # print(div_label)

                p_items = div_label.find_all("p")

                for i in p_items:

                    print(i.text)

                    f.write(i.text+"\n")

