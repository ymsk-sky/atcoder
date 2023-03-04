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
edges = [-1] * m
for i in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    uf.unite(u, v)
    edges[i] = u

d = defaultdict(int)
for e in edges:
    d[uf.find(e)] += 1

gm = uf.group_members()

for parent in gm:
    # 頂点数
    n_num = len(gm[parent])
    # 辺数
    m_num = d[parent]

    if n_num != m_num:
        print("No")
        exit()
print("Yes")
