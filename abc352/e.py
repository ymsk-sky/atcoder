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
final_group = set()
cl = []
al_l = []
for i in range(m):
    k, c = map(int, input().split())
    al = list(map(int, input().split()))
    for a in al:
        final_group.add(a)
    cl.append((c, i))
    al_l.append(al)

if len(final_group) < n:
    print(-1)
    exit()

cl.sort()  # 重みが小さい順に処理していく
ans = 0
for c, i in cl:
    al = al_l[i]
    for a, b in zip(al, al[1:]):
        a, b = a - 1, b - 1
        if uf.same(a, b):
            continue
        uf.unite(a, b)
        ans += c
print(ans)

"""
2<=n,m<=2*10**5
2<=k<=n
sum(k)<=4*10**5
1<=a1<a2<...<ak<=n
1<=c<=10**9
"""