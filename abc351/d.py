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


h, w = map(int, input().split())
sl = [input() for _ in range(h)]
# 0:移動可能, 1:これ以上移動不可, 2: 入れない(磁石)
tl = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if sl[i][j] == "#":
            tl[i][j] = 2
        else:
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                u, v = i + p, j + q
                if 0 > u or u >= h or 0 > v or v >= w:
                    continue
                if sl[u][v] == "#":
                    tl[i][j] = 1
uf = UnionFind(h*w)
for i in range(h):
    for j in range(w):
        if tl[i][j] > 0:
            continue
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            if tl[u][v] > 0:
                continue
            uf.unite(i*w + j, u*w + v)
d = {r: set() for r in uf.roots()}
for i in range(h):
    for j in range(w):
        if tl[i][j] > 0:
            continue
        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            u, v = i + p, j + q
            if 0 > u or u >= h or 0 > v or v >= w:
                continue
            if tl[u][v] == 1:
                d[uf.find(i*w + j)].add(u*w + v)
gm = uf.group_members()
ans = 0
for r in d.keys():
    members = len(gm[r])
    edges = len(d[r])
    tmp = members + edges
    ans = max(ans, tmp)
print(ans)


"""
1<=h,w<=1000

3 5
.#.xx
x.xx.
.#..#

"""