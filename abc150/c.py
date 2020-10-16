from itertools import permutations
n=int(input())
ps=list(map(int,input().split()))
qs=list(map(int,input().split()))
pc=0
qc=0
for i,s in enumerate(permutations(range(1,n+1)),start=1):
    xc=0
    yc=0
    for a,x,y in zip(s,ps,qs):
        if a==x:
            xc+=1
        if a==y:
            yc+=1
    if xc==n:
        pc=i
    if yc==n:
        qc=i
print(abs(pc-qc))
