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
    count_words(wordsString)
    if priint == True:
        print(wordsString)

#get_input()

def_list = [
    "Test 1",
    "test 2",
    "This is a test",
    "The quick brown fox jumped over the lazy dog's back.",
]

if __name__ == '__main__':
    for definition in def_list:
        print("{} - {}".format(count_words(definition), definition))

    with Pool(5) as p:
        def_count = list(p.map(count_words, def_list))

    print(dict(zip(def_count, def_list)))