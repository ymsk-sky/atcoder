from math import ceil
n=int(input())
l=sorted(list(map(int,input().split())))
ans=0
for i in range(1,n):
    ans+=l[n-i//2-1]
print(ans)
