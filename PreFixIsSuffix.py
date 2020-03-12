inputString = "abcdab"

def util(myStr):
    print(myStr)
    counter = 0
    taruptr = 0
    wannaRecurse = False
    for i in range(0, len(myStr)):
        print("comparing " + myStr[i] + " and " + inputString[i])
        print()
        if myStr[i] == inputString[i]:
            counter += 1
            taruptr += 1
        elif myStr[i] != inputString[i]:
            print("Not Match")
            wannaRecurse = True
            break

    if wannaRecurse == False:
        return counter
    else:
        return util(myStr[taruptr + 1:])


taruptr = len(inputString) // 2
taristr = inputString[taruptr:]
print(util(taristr))
