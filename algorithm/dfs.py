"""
深さ優先探索(DFS: Depth First Search)

AtCoder ABC138 D問題に対応
https://atcoder.jp/contests/abc138/tasks/abc138_d

(example input)
4 3
1 2
2 3
2 4
2 10
1 100
3 1

"""

n, q = map(int, input().split())
tree = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)

xs = [0] * n
for _ in range(q):
    p, x = map(int, input().split())
    xs[p-1] += x

ans = [0] * n

def dfs(u, parent=None):
    ans[u] = ans[parent] + xs[u]
    for v in tree[u]:
        if not v == parent:
            dfs(v, u)

dfs(0, 0)
print(' '.join([str(i) for i in ans]))
