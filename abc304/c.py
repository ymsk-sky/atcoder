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


n, d = map(int, input().split())
uf = UnionFind(n)
xyl = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    x1, y1 = xyl[i]
    for j in range(i + 1, n):
        x2, y2 = xyl[j]
        dist = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if dist <= d:
            uf.unite(i, j)

gm = uf.group_members()
s = set(gm[uf.find(0)])
for i in range(n):
    print("Yes" if i in s else "No")
