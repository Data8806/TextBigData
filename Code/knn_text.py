'''
用knn算法对评论文本进行分等级
'''

import pandas as pd
import jieba

from gensim import corpora,models
from sklearn.neighbors import KNeighborsClassifier
from gensim import matutils



data = pd.read_excel("./Code/data/comment.xlsx")
# print(data)

word_pre = []
for i in range(data.shape[0]):
    # 分词
    word_list = jieba.lcut(data["comment"][i])

    # 停用词过滤
    

    word_pre.append(word_list)

# 语料

dictionary  = corpora.Dictionary(word_pre)


# 词袋

word_bow = [dictionary.doc2bow(text) for text in word_pre]

tfidf = models.TfidfModel(word_bow)


data_weight = tfidf[word_bow]


# 组成向量矩阵
data_matrix = matutils.corpus2dense(data_weight,num_terms=len(dictionary.token2id.keys())).T
print(f"data_weight:{data_weight}")

# # 获取所有的评价等级

# grade_num = data["grade"].unique()

# print(grade_num)

# 标签哑处理

grade_dict = {"力荐":5, "推荐":4, "还行":3, "较差":2, "很差":1}
data["grade_new"] = data["grade"].map(grade_dict)


knn_alg = KNeighborsClassifier(n_neighbors=5,p=2)
knn_alg.fit(data_matrix,data["grade_new"])
print(knn_alg.score(data_matrix,data["grade_new"]))



t1 = "这部电影真的很好看，我很喜欢"

t1_list = jieba.lcut(t1)

# t1_list = [d.split() for d in t1_list]

t1_bow = [dictionary.doc2bow(t1_list)]

t1_weight = tfidf[t1_bow]

# 生成文本向量

t1_matrix = matutils.corpus2dense(t1_weight,num_terms=len(dictionary.token2id.keys())).T

print(t1_matrix.shape)
# 预测

print(knn_alg.predict(t1_matrix))
