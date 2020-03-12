# X = int(input)
# inputList = list(map(int, input().split()))
X = 2
inputList = [1, 1, 1, 1, 2, 2, 2, 4, 4]
totalNumberOfDistinctElements = len(list(dict.fromkeys(inputList)))
distlist = list(dict.fromkeys(inputList))
repList = []
print("Total Distinct elements"+str(totalNumberOfDistinctElements))

for val in distlist:
     repList.append(inputList.count(val))

print()
print(repList)

minOccuring = min(repList)  #2

# jiska count == minOccuring ho vo element ko inputlist me se nikaalo
