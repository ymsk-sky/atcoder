n,m,k=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
a=[0]
b=[0]
for i in range(n):
    a.append(a[i]+al[i])
for i in range(m):
    b.append(b[i]+bl[i])
ans=0
j=m
for i in range(n+1):
    if a[i]>k:
        break
    while b[j]>k-a[i]:
        j-=1
    ans=max(ans,i+j)
print(ans)
