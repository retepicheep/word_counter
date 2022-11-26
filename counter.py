from multiprocessing import Pool

def count_words(wordString):
    words = []
    for word in wordString.split():
        words.append(word)
    wordsLen = len(words)
    #print(wordsLen)
    return wordsLen

def get_input(priint):
    wordsString = input()
    wordsNum = count_words(wordsString)
    if priint == True:
        print(wordsNum)
