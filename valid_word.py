def isValidWord(word,hand,wordList):
    if word not in wordList:
        return False
    flag=0
    for i in word:
        if i in hand.keys():
            flag = 1
        else:
            return False
    if flag is 1:
        return True
