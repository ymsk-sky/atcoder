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


n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))
al = list(map(int, input().split()))
bl = list(map(int, input().split()))

cnt_a = [0] * n
cnt_b = [0] * n
for a, b in zip(al, bl):
    cnt_a[a - 1] += 1
    cnt_b[b - 1] += 1

uf = UnionFind(n)
edges.sort()
ans = 0
for w, u, v in edges:
    if uf.same(u, v):
        continue
    r_u = uf.find(u)
    r_v = uf.find(v)
    uf.unite(u, v)
    r = uf.find(u)
    cnt_a[r] = cnt_a[r_u] + cnt_a[r_v]
    cnt_b[r] = cnt_b[r_u] + cnt_b[r_v]
    e = min(cnt_a[r], cnt_b[r])
    ans += w*e
    cnt_a[r] -= e
    cnt_b[r] -= e
print(ans)
