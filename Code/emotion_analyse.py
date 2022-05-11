import jieba
import numpy as np
#打开词语文件，返回词语列表
def open_doc(name = 'hahah', path=r'./'):
    path = path + '%s.txt' % name
    dictionary = open(path, 'r', encoding='utf-8')
    word_items = []
    for word in dictionary:
        word = word.strip('\n')
        word_items.append(word)
    return word_items

#判断情感词前否定词数量的奇偶性
def judgeodd(num):
    if (num % 2) == 0:
        return 'even'
    else:
        return 'odd'
    
#情感分析处理
def sentiment_score_list(dataset):
    seg_sentence = dataset.split('。')  #按句进行划分
    count1 = []
    count2 = []
    for sen in seg_sentence: #循环遍历每一个评论
        segtmp = jieba.lcut(sen, cut_all=False)  #把句子进行分词，以列表的形式返回
        i = 0 #记录扫描到的词的位置
        a = 0 #记录情感词的位置
        poscount = 0 #积极词的第一次分值        
        negcount = 0        
        total_emotion = 0  #情感值
        for word in segtmp:            
            if word in posdict:  # 判断词语是否是积极情感词
                print("积极",word)
                poscount = 1  #积极词得分
                i = segtmp.index(word)
                c = 0
                for w in segtmp[a:i]:  # 扫描情感词前的程度词
                    if w in mostdict:
                        poscount *= 4.0
                    elif w in verydict:
                        poscount *= 3.0
                    elif w in moredict:
                        poscount *= 2.0
                    elif w in ishdict:
                        poscount *= 0.5
                    elif w in deny_word:
                        c += 1
                if judgeodd(c) == 'odd':  # 扫描情感词前的否定词数
                    poscount *= -1.0
                total_emotion = total_emotion+ poscount
                a = i + 1  # 下一次搜索的开始值
            elif word in negdict:  # 消极情感的分析，与上面一致
                print("消极",word)
                negcount = -1
                i = segtmp.index(word)
                d = 0
                for w in segtmp[a:i]:
                    if w in mostdict:
                        negcount *= 4.0
                    elif w in verydict:
                        negcount *= 3.0
                    elif w in moredict:
                        negcount *= 2.0
                    elif w in ishdict:
                        negcount *= 0.5
                    elif w in deny_word:
                        d += 1
                if judgeodd(d) == 'odd':
                    negcount *= -1.0
                total_emotion = total_emotion+ negcount    
                negcount = 0
                a = i + 1
            elif word == '！' or word == '!':  ##判断句子是否有感叹号
                total_emotion += 2            
        count2.append(total_emotion)
        count1 = []
    return count2

#分别取出否定词 情感词  程度词
deny_word = open_doc(name = '否定词', path= r'./data/')
posdict = open_doc(name = 'positive', path= r'./data/')
negdict = open_doc(name = 'negative', path= r'./data/')
degree_word = open_doc(name = '程度级别词语', path= r'./data/')
#取出不同的程度词
mostdict = degree_word[degree_word.index('extreme')+1 : degree_word.index('very')]#权重4，即在情感词前乘以4
verydict = degree_word[degree_word.index('very')+1 : degree_word.index('more')]#权重3
moredict = degree_word[degree_word.index('more')+1 : degree_word.index('ish')]#权重2
ishdict = degree_word[degree_word.index('ish')+1 : degree_word.index('last')]#权重0.5
#文本
data1 = '你就是个王八蛋，混账玩意!你们的手机真不好用！非常生气，心情也不好，我非常郁闷！！！！'
data2= '我好开心啊，非常非常非常高兴！今天我得了一百分，我很兴奋开心，愉快，开心'
print('data1分值：',sentiment_score_list(data1))
print('data2分值：',sentiment_score_list(data2))
