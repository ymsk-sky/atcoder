n,k=map(int,input().split())
l=list(map(int,input().split()))
if n<=k:
    print(1)
    exit()
c=1
while 1:
    if n<=k:
        break
    n-=(k-1)
    c+=1
print(c)
