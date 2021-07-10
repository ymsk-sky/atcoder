n=int(input())
cl=list(map(int,input().split()))
cl.sort()
mod=10**9+7
ans=1
for i,c in enumerate(cl):
    ans*=(c-i)
    ans%=mod
print(ans)
