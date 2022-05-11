'''
统计红楼梦统计词频，显示词频最高的20个词，以及出现的次数
'''

# 导入模块

from unittest import result
import jieba



def participle(sentence):
    seg_list = jieba.lcut(sentence,cut_all=False)
    result_list = []
    for i in seg_list:
        if i>=u"\u4e00" and i<= u"\u9fa5":
            result_list.append(i)
    return result_list

# 统计,并排序
def count(result_list):
    # 建立字典
    result_dict = dict()
    for i in result_list:
        if i in result_dict:
            result_dict[i]+=1
        else:
            result_dict[i]=1
    
    # 排序

    result_list = sorted(result_dict.items(),key= lambda x:x[1],reverse=True)

    #输出前二十
    return result_list[:20]
    
# 打开文件
with open("../Data/红楼梦_utf8.txt","r",encoding="utf-8") as file:
    sentence = file.read()
if __name__=="__main__":
    print(count(participle(sentence)))
