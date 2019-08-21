file = open('input.txt', 'r', encoding='utf-8')
seq = file.readlines()
countDict = {}
for elem in seq:
    for word in elem.split():
        countDict[word] = countDict.get(word, 0) + 1
        print((countDict[word] - 1), end=' ')
file.close()
