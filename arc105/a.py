from itertools import product
l=list(map(int,input().split()))
for p in product((0,1),repeat=4):
    if sum(p)==0:
        continue
    x=0
    y=0
    for b,v in zip(p,l):
        if b==0:
            x+=v
        else:
            y+=v
    if x==y:
        print('Yes')
        exit()
print('No')
