n=int(input())
ps=list(map(int,input().split()))
c=0
for i,p in enumerate(ps, start=1):
    if not p==i:
        c+=1
print('YES' if c<3 else 'NO')
