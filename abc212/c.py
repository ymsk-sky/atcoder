from bisect import bisect_left
n,m=map(int,input().split())
al=list(map(int,input().split()))
bl=list(map(int,input().split()))
bl.sort()
ans=float('inf')
for a in al:
    i=bisect_left(bl,a)
    if i==0:
        ans=min(ans,abs(a-bl[0]))
    elif i<m:
        ans=min(ans,abs(a-bl[i-1]),abs(a-bl[i]))
    else:
        ans=min(ans,abs(a-bl[-1]))
print(ans)
