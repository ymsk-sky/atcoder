n=int(input())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
cl=list(map(int,input().split()))

d2={i:0 for i in range(1,n+1)}
for c in cl:
    d2[c]+=1

d1={i:0 for i in range(1,n+1)}
for i,b in enumerate(bl,start=1):
    d1[b]+=d2[i]

ans=0
for a in al:
    ans+=d1[a]
print(ans)
