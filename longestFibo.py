def getFibboncci(maximum):
    nterms = maximum

    # first two terms
    n1, n2 = 0, 1
    count = 0
    fibboList = []
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            fibboList.append(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

    return fibboList

inputlist = [1,3,7,11,12,14,18]
fibbolist = getFibboncci(max(inputlist))

answer = []
for val in inputlist:
    if val in fibbolist:
        answer.append(val)

print(answer)