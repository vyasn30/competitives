inputList = list(map(int, input().split(",")))
# inputList = [3, 2, 6, 5, 1, 4, 8, 9]
indexof5 = inputList.index(5)
indexof8 = inputList.index(8)

# print(indexof5, indexof8)
var2 = inputList[indexof5:indexof8+1]
num2 = ""

for val in var2:
    num2 = num2 + str(val)

num2 = int(num2)
num1 = 0
for val in inputList:
    if val in var2:
        continue
    else:
        num1 += val

print(num1+num2)