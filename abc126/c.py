n,k=map(int,input().split())
ans=0
for i in range(1, n+1):
    tmp=1/n
    p=i
    while p<k:
        p=2*p
        tmp=tmp/2
    ans+=tmp
print(ans)
