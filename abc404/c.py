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

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

n, m = map(int, input().split())
nums = [0] * n
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    nums[a] += 1
    nums[b] += 1
    uf.unite(a, b)

if uf.group_size() != 1:
    print("No")
    exit()

for num in nums:
    if num != 2:
        print("No")
        exit()

print("Yes")
