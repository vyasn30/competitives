inputList = list(map(str,input().split(","))) #abcd:1234,bcdgfhf:127836,sdjks:1245
print(inputList)
strlist = []
codelist = []
tempList = []
for val in inputList:
    tempList.append(list(map(str, val.split(":"))))

print(tempList)

for val in tempList:
    strlist.append(val[0])
    codelist.append((val[1]))

for i in range(0, len(codelist)):
    tempsum = 0
    for val in codelist[i]:
        tempsum = tempsum + (int(val) ** 2)

    if tempsum % 2 == 0:
        print(strlist[i][len(strlist[i]) - 2:] + strlist[i][:len(strlist[i]) - 2])
    elif tempsum % 2 != 0:
        print(strlist[i][1:] + strlist[i][0])
