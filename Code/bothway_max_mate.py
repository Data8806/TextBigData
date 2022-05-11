"""
双向最大匹配算法
"""
dictA = ["南京市","南京市长","长江","长江大桥","大桥"]  #字典

sentence = "南京市长江大桥"

def cutA(sentence,dict):
    maxDictA = max([len(word) for word in dictA])  #最大词长度
    result = []
    sentenceLen = len(sentence)
    n = 0
    while n<sentenceLen:
        matched = 0
        for i in range(maxDictA,0,-1): #最大字符串开始匹配
            piece = sentence[n:n+i]      #从左到右
            if piece in dictA:
                result.append(piece)
                matched = 1
                n = n+i
                break
        if not matched:
            result.append(sentence[n])
            n += 1
    return result

def cutB(sentence,dict):
    maxDictA = max([len(word) for word in dictA])  #最大词长度
    result = []
    sentenceLen = len(sentence)
    while sentenceLen>0:
        matched = 0
        for i in range(maxDictA,0,-1): #最大
            piece = sentence[sentenceLen-i:sentenceLen]      #从右到左
            if piece in dictA:
                result.append(piece)
                matched = 1
                sentenceLen -= i
                break
        if not matched:
            sentenceLen -= 1
            result.append(sentence[sentenceLen]) 
    return result[::-1]

def compare(sentence,dict):
    result1 = cutA(sentence,dict)
    result2 = cutB(sentence,dict)
    # 判断结果是否相同
    if(result1==result2):
        return result1
    else:
        if len(result1)>len(result2):
            return result2
        else:
            return result1

print(compare(sentence,dictA))

if __name__ =="__main__":
    print(compare(sentence,dict))