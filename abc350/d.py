from collections import defaultdict

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

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


n, m = map(int, input().split())
uf = UnionFind(n)
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)
    uf.unite(a, b)
gm = uf.group_members()
ans = 0
for r in gm:
    g = gm[r]
    ll = len(g)
    tmp = ll * (ll - 1) // 2 # このグループの最終的な本数
    g_sum = 0  # 今現在ある本数
    for c in g:
        g_sum += len(edges[c])
    g_sum //= 2
    tmp -= g_sum
    ans += tmp
print(ans)

"""
2<=n<=2*10**5
0<=m<=2*10**5
1<=a<b<=n
"""