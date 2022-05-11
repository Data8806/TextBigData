"""
过滤红楼梦中的停用词
"""

# 导入模块
from unittest import result
import jieba

# 加载停用词库
def load_stop_lexicon():
    with open("../Data/哈工大停用词表.txt","r",encoding="utf-8") as file:
        lexicon_text = file.readlines()
    lexicon_list = []

    for i in lexicon_text:
        lexicon_list.append(i.strip())
    return lexicon_list

# 过滤

def filter(sentence):
    lexicon_list = load_stop_lexicon()
    result_list =[]
    split_list= jieba.lcut(sentence)
    for i in split_list:
        if i not in lexicon_list:
            result_list.append(i)

    return result_list


if __name__=="__main__":
    with open("../Data/红楼梦_utf8.txt","r",encoding="utf-8") as file:
        sentence = file.read()
    print(filter(sentence))
