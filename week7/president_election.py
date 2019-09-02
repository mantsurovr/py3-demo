fd = open('input.txt', 'r', encoding='UTF-8')
lines = fd.readlines()
mydict, mylist, cnt = dict(), [], 0
for i in lines:
    i = i.replace("\n", "")
    mydict[i] = mydict.get(i, 0) + 1
    cnt += 1
for a in mydict:
    mylist.append((-mydict[a], a))
mylist.sort()
fd.close()
file = open('output.txt', 'w', encoding='UTF-8')
if abs(int(((mylist)[0])[0])) > int(cnt // 2):
    file.write(((mylist)[0])[1])
else:
    print(((mylist[0])[1]), file=file)
    print(((mylist[1])[1]), file=file)
file.close()
