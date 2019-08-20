n, myDict1, myDict2 = int(input()), dict(), dict()
for i in range(n):
    dict1 = input().split()
    key1 = dict1[0]
    key2 = dict1[1]
    if key1 not in myDict1:
        myDict1[key1] = []
    myDict1[key1].append(key2)
    if key2 not in myDict2:
        myDict2[key2] = []
    myDict2[key2].append(key1)
strng = input()
if strng in myDict1:
    print(*myDict1[strng])
elif strng in myDict2:
    print(*myDict2[strng])
