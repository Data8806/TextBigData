"""
文本的向量表示
"""

from gensim import corpora

import jieba

from collections import defaultdict

with open("./Code/data/data1.txt",encoding="utf-8") as f:
    d1 = f.read()

with open("./Code/data/data2.txt",encoding="utf-8") as f:
    d2 = f.read()

data1 = jieba.lcut(d1)

data2 = jieba.lcut(d2)

dictionary = corpora.Dictionary([data1,data2])

print(dictionary.num_docs)

print(dictionary.token2id)

print(dictionary.dfs)

# 得到对应的词袋的稀疏矩阵

new1 = dictionary.doc2bow(data1)

new2 = dictionary.doc2bow(data2)

print(new1)

print(new2)