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

"""
3 4
1 3 5 17
2 4 2 3
1 3 2 9

5 3
89 62 15
44 36 17
4 24 24
25 98 99
66 33 57
"""
