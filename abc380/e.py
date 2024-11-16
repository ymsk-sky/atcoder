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


n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

uf = UnionFind(n + 1)
ml = {i: [i, i] for i in range(1, n + 1)}  # マスiと隣接する最小と最大
cl = {i: i for i in range(1, n + 1)}  # cl[i]: グループi(親がi)の色
cnt = {i: 1 for i in range(1, n + 1)}  # 色iの個数

for query in queries:
    if query[0] == 1:
        x, c = query[1:]
        r = uf.find(x)
        # 色をcへ変更
        i_min, i_max = ml[r]
        cnt[cl[r]] -= i_max - i_min + 1
        cl[r] = c
        cnt[c] += i_max - i_min + 1
        # 横と同じなら統合する
        if i_min > 1:
            # 左を確認
            r_left = uf.find(i_min - 1)
            if cl[r_left] == c:
                # 同じなので結合
                uf.unite(r_left, r)
                r_final = uf.find(r)
                ml[r_final] = [ml[r_left][0], ml[r][1]]
                r = r_final  # rを更新
        if i_max < n:
            # 右を確認
            r_right = uf.find(i_max + 1)
            if cl[r_right] == c:
                # 同じなので結合
                uf.unite(r, r_right)
                r_final = uf.find(r)
                ml[r_final] = [ml[r][0], ml[r_right][1]]
    else:
        c = query[1]
        ans = cnt[c]
        print(ans)
