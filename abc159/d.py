from math import factorial
def comb(n,r):
    if n<2: return 0
    return factorial(n)//(factorial(n-r)*factorial(r))
n=int(input())
l=list(map(int,input().split()))
d={i:0 for i in range(1,n+1)}
for a in l:
    d[a]+=1
base=sum([comb(v,2) for v in d.values()])
for k in l:
    ans=base-(d[k]-1)
    print(ans)
