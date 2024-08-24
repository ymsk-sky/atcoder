import sys
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)
vl = [v - 1 for v in list(map(int, input().split()))]
v = vl[0]
s = set(vl)

ans = n
def dfs(crt: int, bef: int) -> bool:
    global ans
    need = False
    need_child = False
    for nxt in edges[crt]:
        if nxt == bef:
            continue
        need_child |= dfs(nxt, crt)
    if crt in s:
        need |= True
    else:
        need |= False
        if not need_child:
            ans -= 1
    return need | need_child

dfs(v, -1)
print(ans)
