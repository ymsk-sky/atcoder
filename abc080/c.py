from itertools import product
n=int(input())
fs=[list(map(int,input().split())) for _ in range(n)]
ps=[list(map(int,input().split())) for _ in range(n)]
ans=-float('inf')
for b in product((0,1),repeat=10):
    #eg) b = tuple(0,0,1,0,1,0,1,0,0,1) (len(b)=10)
    if sum(b)==0:
        continue
    v=0
    for f,p in zip(fs,ps):
        #eg) f = [1,0,1,0,0,0,1,0,1,0] (len(f)=10)
        #eg) p = [0,4,-1,2,-1,3,1,1,0,2,-4] (len(p)=11)
        cnt=sum([a&b for a,b in zip(b,f)])
        v+=p[cnt]
    ans=max(ans,v)
print(ans)
