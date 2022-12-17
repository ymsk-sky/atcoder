from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


n, m = map(int, input().split())
edges = [[] for _ in range(n)]
lines = [0] * n
uf = UnionFind(n)
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
    uf.unite(u, v)
    if u < v:
        lines[u] += 1
    else:
        lines[v] += 1

# 2彩色
col = dict()
def dfs(crt, color):
    x = uf.find(crt)
    if not x in col:
        col[x] = dict()    
    if not crt in col[x]:
        col[x][crt] = -1

    if col[x][crt] != -1:
        return

    col[x][crt] = color
    for nxt in edges[crt]:
        y = uf.find(nxt)
        if not y in col:
            col[y] = dict()
        if not nxt in col[y]:
            col[y][nxt] = -1

        if col[y][nxt] == color:
            # 与えられたグラフ自体が二部グラフでない
            print(0)
            exit()
        if col[y][nxt] == -1:
            dfs(nxt, 1 - color)

for i in range(n):
    dfs(i, 0)

ans = 0

gm = uf.group_members()
cols = dict()  # 各塊ごとの色の数
for r in gm:
    cols[r] = [0, 0]
    for c in gm[r]:
        cols[r][col[r][c]] += 1

for i in range(n):
    r = uf.find(i)
    line = lines[i]
    color = col[r][i]
    # 同じ塊内の自分と異なる色 かつ つながっていない, 自分より大きい値のノード
    ans += cols[r][1 - color] - line
    cols[r][color] -= 1
    # 他の塊は 自分より大きい値のノード どれでも
    ans += n - i - 1 - len(gm[r])

print(ans)

"""
ans = 0
for i in range(n):
    line = lines[i]
    color = col[i]
    if color == 0:  # 自身がwhite
        ans += black - line
        white -= 1
    else:  # 自身がblack
        ans += white - line
        black -= 1
print(ans)
"""
"""
2<=n<=2*10**5
0<=m<=min(2*10**5, n(n-1)/2)
1<=u,v<=n
グラフは単純
"""
