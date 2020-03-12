def listToString(s):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))


str_list = input()

char_list = []
for i in range(0, len(str_list)):
    if str_list[i] == "":
        continue
    chargrp = []
    chargrp.append(str_list[i])
    for j in range(i+len(chargrp), len(str_list)):
        if str_list[i].lower() == str_list[j].lower():
            chargrp.append(str_list[j])
            str_list[j] = ""

    str_list[i] = ""
    char_list.append(chargrp)

print(char_list)
newList = []
for val in char_list:
    newList.append(listToString(val))

lptr = 0
rptr = len(newList)-1
answer = ""
for i in range(0, len(newList)):
    if i % 2 == 0:
        answer += newList[lptr]
        lptr += 1
    else:
        answer += newList[rptr]
        rptr -= 1

print(newList)
print(answer)