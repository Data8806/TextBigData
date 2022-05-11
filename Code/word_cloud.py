from PIL import Image
import jieba
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from jieba import analyse



text_path = "./Data/2019元旦.txt"

stop_word_table_path = "./Data/哈工大停用词表.txt"

# 加载停用词库


# with open(stop_word_table_path,"r",encoding="utf-8") as f:
#     list1  = f.readlines()
#     stop_word_list = [i.strip() for i in list1]


# 分词
with open(text_path,"r",encoding="utf-8") as f:

    # result_list1 = jieba.lcut(f.read())
    count_word_dict = dict()
    data = analyse.extract_tags(f.read(),topK=30,withWeight=True,allowPOS="n")
    for i in data:
        count_word_dict[i[0]] = i[1]
     




# 过滤停用词
# result_list = []
# for i in result_list1:
#     if i not in stop_word_list:
#         result_list.append(i)



# 统计词频

# count_word_dict = dict()

# for i in result_list:
#     if i in count_word_dict.keys():
#         count_word_dict[i]+=1
#     else:
#         count_word_dict[i] = 1

# 词云展示

mask = np.array(Image.open("./Code/save_img/flower.png"))



wc = wordcloud.WordCloud(font_path="D:/Anaconda3/Lib/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf",
mask=mask)

# 加载文本以及词频
wc.generate_from_frequencies(count_word_dict)

image_colors = wordcloud.ImageColorGenerator(mask)

wc.recolor(color_func=image_colors)

plt.imshow(wc)

plt.axis("off")

plt.show()


