a,b,k=map(int,input().split())
n=0
for i in range(min(a,b),0,-1):
    if (a/i==a//i) and (b/i==b//i):
        n+=1
        if n==k:
            print(i)
            exit()
