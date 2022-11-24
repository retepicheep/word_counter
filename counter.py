words = "Hi I am Peter"

def count_words(wordString):
    words = []
    for word in wordString.split():
        words.append(word)
    wordsLen = len(words)
    print(wordsLen)

count_words(words)
