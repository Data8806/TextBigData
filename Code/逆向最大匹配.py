dictA = ["南京市","南京市长","长江","长江大桥","大桥"]
maxDictA = max([len(word) for word in dictA])
sentence = "南京市长江大桥"
def cutB(sentence):
    result = []
    sentenceLen = len(sentence)
    while sentenceLen>0:
        matched = 0
        for i in range(maxDictA,0,-1): #最大
            piece = sentence[sentenceLen-i:sentenceLen]      #从右到左
            print(piece)
            if piece in dictA:
                result.append(piece)
                matched = 1
                sentenceLen -= i
                break
        if not matched:
            sentenceLen -= 1
            result.append(sentence[sentenceLen]) 
    print(result[::-1])

cutB(sentence)


"""
羽毛球拍卖完了
一只小猫出现在房子旁边
咱们连长说明天下午回营里休整
"""
        
