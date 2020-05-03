n,k=map(int,input().split())
h=[]
for _ in range(k):
    d=int(input())
    as_=list(map(int,input().split()))
    for a in as_:
        h.append(a)
ans=0
for m in range(1, n+1):
    if not m in h:
        ans+=1
print(ans)
