from itertools import permutations
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
ds=[[] for _ in range(n)]
for i,(x,y) in enumerate(l):
    for j,(a,b) in enumerate(l):
        if i==j:
            ds[i].append(0)
        else:
            k=((x-a)**2+(y-b)**2)**(1/2)
            ds[i].append(k)
ans=0
num=0
for p in permutations(range(n)):
    t=sum([ds[x][y] for x,y in zip(p,p[1:])])
    ans+=t
    num+=1
print(ans/num)
