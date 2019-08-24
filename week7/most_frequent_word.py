lines = open('input.txt', 'r', encoding='UTF-8')
seq = lines.readlines()
mydict, mylist1, mylist2 = dict(), [], []
for line in seq:
    for word in line.split():
        mydict[word] = mydict.get(word, 0) + 1
        mylist1.append(mydict[word])
        mylist2.append((word, mydict[word]))
print(min([k for k, v in mylist2 if v == max(mylist1)]))
lines.close()
