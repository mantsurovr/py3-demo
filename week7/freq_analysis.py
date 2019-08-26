fd = open('input.txt', 'r', encoding='UTF-8')
lines = fd.readlines()
mydict, mylist = dict(), []
for i in lines:
    for word in i.split():
        mydict[word] = mydict.get(word, 0) + 1
for a in mydict:
    mylist.append((-mydict[a], a))
for b in sorted(mylist):
    print(b[1])
fd.close()
