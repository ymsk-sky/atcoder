n,k=map(int,input().split())
l=list(map(int,input().split()))
d=dict()
for a in l:
    if a in d:
        d[a]+=1
    else:
        d[a]=1
ans=0
for _,c in sorted(d.items(),key=lambda x:x[1])[:len(d)-k]:
    ans+=c
print(ans)
