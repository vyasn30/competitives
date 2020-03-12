testcases = int(input())
while(testcases>0):
    noOfElephants,noOfCandies = map(int, input().split())
    elephantNeed = list(map(int, input().split()))
    if noOfCandies >= sum(elephantNeed):
        print("Yes\n")
    else:
        print("No\n")