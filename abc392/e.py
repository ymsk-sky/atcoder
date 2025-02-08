from collections import defaultdict, deque

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
abl = [list(map(lambda e: int(e) - 1, input().split())) for _ in range(m)]

uf = UnionFind(n)
not_used = []
for i, (a, b) in enumerate(abl):
    if uf.same(a, b):
        not_used.append(i)
        continue
    uf.unite(a, b)

# グループごとのケーブルの余りを求める
d = {r: [] for r in uf.roots()}
for i in not_used:
    a, b = abl[i]
    d[uf.find(a)].append(i)

ans = []
rl = sorted(list(d.keys()), key=lambda r: -len(d[r]))
que_r = deque([rl[0]])
for r in rl[1:]:
    # ケーブルの余り本数が多い順に処理
    que_r.append(r)
    while que_r:
        s = que_r.popleft()
        if len(d[s]) > 0:
            break
    # つなげる
    i = d[s].pop()
    a, b = abl[i]
    ans.append((i + 1, a + 1, r + 1))
    # 戻す
    if len(d[s]):
        que_r.append(s)

if len(ans) == 0:
    print(0)
    exit()
print(len(ans))
for an in ans:
    print(*an)
