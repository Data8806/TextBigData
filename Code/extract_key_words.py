"""
提取红楼梦中的关键词
"""
# 导入模块

import jieba
from jieba import analyse
def extract(sentence):
    keywords = analyse.extract_tags(sentence,topK=20,withWeight=True)
    return keywords

if __name__=="__main__":
    with open("../Data/红楼梦_utf8.txt","r",encoding="utf-8") as file:
        sentence = file.read()
    
    key_words = extract(sentence)
    print(key_words)
    for i in key_words:
        print(i[0],i[1])