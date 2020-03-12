# inputString = input()
inputString = "A5w8@k7!|23n69"
specialCounter = 0
oddList = []
evenList = []
out = []
for val in inputString:
    if not val.isalnum():
        specialCounter+=1

for val in inputString:
    if val.isdigit():
        if int(val)%2 == 0:
            evenList.append(int(val))
        else:
            oddList.append(int(val))

l = [i for i in zip(evenList,oddList)]

for val1 in l:
    for val2 in val1:
        out.append(val2)
print(out)


for val in oddList:
    if val not in out:
        out.append(val)
print(out)

# difference = abs(len(oddList) - len(evenList))
# if len(oddList) > len(evenList):
#     l.append()
# print(difference)