dictA = ["南京市","南京市长","长江","长江大桥","大桥"]  #字典
maxDictA = max([len(word) for word in dictA])  #最大词长度
sentence = "南京市长江大桥"
def cutA(sentence):
    result = []
    sentenceLen = len(sentence)
    n = 0
    while n<sentenceLen:
        matched = 0
        for i in range(maxDictA,0,-1): #最大字符串开始匹配
            piece = sentence[n:n+i]      #从左到右
            print(piece)
            if piece in dictA:
                result.append(piece)
                matched = 1
                n = n+i
                break
        if not matched:
            result.append(sentence[n])
            n += 1
    print(result)

cutA(sentence)

"""
羽毛球拍卖完了
一只小猫出现在房子旁边
咱们连长说明天下午回营里休整
"""
        
