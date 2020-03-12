inputString = "qwert@12"
numbers = []

for val in inputString:
    if val.isdigit():
        numbers.append(int(val))

min = numbers[0]

for val in numbers:
    if val <= 2 and val % 2 == 0:
        min = val

numbers = list(dict.fromkeys(numbers))
numbers.remove(min)
numbers = sorted(numbers)
answer = []
answer.append(min)

for val in numbers:
    answer.append(val)

answer.reverse()
answerstr = ""

for val in answer:
    answerstr = answerstr + str(val)

print(answerstr)