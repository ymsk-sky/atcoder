n,m=map(int,input().split())
l=[list(map(int,input().split()))for _ in range(m)]
c=[]
d=[]
for a,b in l:
    if a==1:
        c.append(b)
    if b==n:
        d.append(a)
if len(set(c)&set(d))>0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
