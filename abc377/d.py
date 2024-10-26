from sortedcontainers import SortedList

def segfunc(x, y):
    return min(x, y)

class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i + 1])

    def query(self, l, r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n, m = map(int, input().split())
lrl = [list(map(int, input().split())) for _ in range(n)]
lrl.sort()
ll = []
rl = []
for l, r in lrl:
    ll.append(l)
    rl.append(r)
sl = SortedList(ll)
st = SegTree(init_val=rl, segfunc=segfunc, ide_ele=float("inf"))

ans = 0
for p in range(1, m + 1):
    i = sl.bisect_left(p)
    if i == n:
        q = m
    else:
        q = st.query(i, n) - 1
    ans += max(0, q - p + 1)
print(ans)
