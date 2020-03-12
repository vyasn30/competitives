inputString = list(map(str, input()))
specialIndices = []
ans = []
for i in range(0,len(inputString)):
    if not inputString[i].isalnum():
        specialIndices.append(i)
for i in range(0, len(inputString)):
    if i in specialIndices:
        continue
    else:
        ans.append(inputString[i])
ans.reverse()
answer = []
for val in specialIndices:
        ans.insert(val, inputString[val])
print("".join(ans))











