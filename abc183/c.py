from itertools import permutations
n,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
cnt=0
for p in permutations(range(1,n)):
    t=[0]+list(p)+[0]
    tmp=0
    for i,j in zip(t,t[1:]):
        tmp+=l[i][j]
    if tmp==k:
        cnt+=1
print(cnt)
