# cook your dish here
for _ in range(int(input())):
    a,b,n = map(int,input().split())
    
    for i in range(n):
        if i%2 == 0:        #alice ni vaari
            a = a*2
        else:
            b = b*2
    
    print(max(a,b)//min(a,b))
