from itertools import product
l=list(map(int,input().split()))
a=set()
for p in product((0,1),repeat=5):
    if sum(p)==3:
        s=0
        for i,q in enumerate(p):
            if q==1:
                s+=l[i]
        a.add(s)
print(sorted(a,reverse=True)[2])
