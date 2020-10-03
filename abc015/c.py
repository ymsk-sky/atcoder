n,k=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
def dfs(q,v):
    if q==n:
        return v==0
    for i in range(k):
        if dfs(q+1,v^l[q][i]):
            return True
    return False
print('Found' if dfs(0,0) else 'Nothing')
