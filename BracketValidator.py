openList = ["(", "{", "["]
closeList = [")", "}", "]"]
stack = []


def Validator(myStr):
    count = 0
    if len(myStr) == 1 and myStr[0] in openList:
        return 1+1
    elif len(myStr) == 1 and myStr[0] in closeList:
        return 1
    else:
        if myStr[0] in closeList:
            return 1
        for val in myStr:
            if val in openList:
                stack.append(val)
                count += 1
                print("pushing opening bracket " + val)
                continue
            elif val in closeList:
                pos = closeList.index(val)
                if len(stack) > 0 and (openList[pos] == stack[-1]):  # match condition
                    stack.pop()
                    count += 1
                    print("Match!! popping out opening bracket")
                else:
                    print("closing Not matched. Phata")
                    count += 1
                    return count

        if not stack:
            return 0
        else:
            if stack[0] in openList:
                return count + 1
            else:
                return count


myStr = input()
print(Validator(myStr))
