n=int(input())
zs=[list(map(int,input().split())) for _ in range(n)]
ls=[]
for _ in range(n):
    print(zs)
    l=0
    for zi,zj in zip(zs,zs[1:]):
        l+=((zi[0]-zj[0])**2+(zi[1]-zj[1])**2)**(1/2)
    ls.append(l)
    h=zs.pop(0)
    zs.append(h)
print(ls)
print(sum(ls)/len(ls))
