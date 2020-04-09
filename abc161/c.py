n,k=map(int,input().split())
if n<k: print(min(n,abs(n-k)))
elif n==k or k==1: print(0)
else: print(min(n,abs(n-(n//k+1)*k)))
