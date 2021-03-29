from itertools import product
n=int(input())
l=list(map(int,input().split()))
ans=float('inf')
for prd in product((0,1),repeat=n-1):
    splited=[]
    tmp=[]
    for i,s in enumerate(prd+(0,)):
        tmp.append(l[i])
        if s==1:
            splited.append(tmp)
            tmp=[]
    splited.append(tmp)
    b=splited[0][0]
    for v in splited[0][1:]:
        b|=v
    crt=b
    for a in splited[1:]:
        b=a[0]
        for v in a[1:]:
            b|=v
        crt^=b
    ans=min(ans,crt)
print(ans)
