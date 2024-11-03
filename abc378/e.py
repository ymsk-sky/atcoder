def segfunc(x, y):
    return x + y

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

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k^1])
            k >>= 1

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
al = list(map(int, input().split()))

acc = [0] + al[:]
for i in range(n):
    acc[i + 1] += acc[i]
    acc[i + 1] %= m

st = SegTree(init_val=[0] * (m + 1), segfunc=segfunc, ide_ele=0)

acc_s = 0
ans = 0
for i in range(1, n + 1):
    x = st.query(acc[i] + 1, m)
    ans += acc[i]*i - acc_s + m*x
    acc_s += acc[i]
    st.add(acc[i], 1)
print(ans)
