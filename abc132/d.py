from math import factorial as f
n,k=map(int,input().split())
mod=10**9+7
def comb(n,r):
    return f(n)//(f(n-r)*f(r))
if n==k:
    for i in range(k):
        print(1 if i==0 else 0)
else:
    for i in range(1,k+1):
        if i-n+k>1:
            ans=0
        else:
            ans=(comb(n-k+1,i)%mod)*(comb(k-1,i-1)%mod)
        print(ans%mod)
