from math import factorial as f
n,k=map(int,input().split())
mod=10**9+7
def comb(n,r):
    return f(n)//(f(n-r)*f(r))
for i in range(1,k+1):
    ans=(comb(n-k+1,i)%mod)*(comb(k-1,i-1)%mod)
    print(ans%mod)
