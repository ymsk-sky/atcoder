n,k=map(int,input().split())
cl=list(map(int,input().split()))
d=dict()
for c in cl[:k]:
    if c in d:
        d[c]+=1
    else:
        d[c]=1
ans=len(d)
tmp=ans
for i in range(n-k):
    out=cl[i]
    add=cl[i+k]
    d[out]-=1
    if d[out]==0:
        tmp-=1
    if add in d and d[add]>0:
        d[add]+=1
    else:
        d[add]=1
        tmp+=1
    ans=max(ans,tmp)
print(ans)
