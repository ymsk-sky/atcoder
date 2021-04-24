n,m=map(int,input().split())
abl=[list(map(int,input().split())) for _ in range(m)]
tr={k:[] for k in range(n)}
for a,b in abl:
    tr[a-1].append(b-1)
    tr[b-1].append(a-1)
def dfs(i,):
    pass
print(dfs(0))
