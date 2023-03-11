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


n, m = map(int, input().split())
uf = UnionFind(n)
x, y = 0, n
# sl = [[-1, -1] for _ in range(n)]  # R, Bの状態: -1:Free T:Connected to T
for _ in range(m):
    a, b, c, d = input().split()
    a, c = int(a) - 1, int(c) - 1
    b = 0 if b == "R" else 1
    d = 0 if d == "R" else 1
    if uf.same(a, c):
        # 輪になる
        # sl[a][b] = c
        # sl[c][d] = a
        y -= 1
        x += 1
    else:
        y -= 1
        uf.unite(a, c)

print(x, y)
