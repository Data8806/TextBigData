#爬取长津湖评分等级及相应短评
#从文件中取出要爬取的内容
import re #正则表达式
from bs4 import BeautifulSoup
import pandas as pd #用于将数据保存到excel

df = pd.DataFrame({"comment":["shorter"],"grade":["推荐"]})
k = 0
for i in range(10):
    #读出文件中的内容
    with open(f"./Data/comment/comment{i}.html","rb") as fr:
        file_read = fr.read().decode(encoding="utf-8")
    soup = BeautifulSoup(file_read,"html.parser")
    file_list = soup.find_all("div",attrs={"class":"comment-item"})
    # print(file_list)clear
    for item in file_list:
        try:
            data = item.find("span",attrs={"class":"short"})
            grade = item.find("span",attrs={"class":re.compile("allstar[1-5][0]\S* rating")})
            #print(grade)
            short = data.text
            #print(short)
            grade_num = grade.attrs["title"]
                #写入数据
            df.loc[k] = [short,grade_num]
            k+=1
            #保存到excel里
        except :
            continue

    df.to_excel("./Code/data/评论.xlsx")