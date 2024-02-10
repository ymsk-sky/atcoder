def segfunc(x,y):
    return min(x,y)
class LazySegTree_RAQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [0]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v==0:
                continue
            self.lazy[i] = 0
            self.lazy[2*i] += v
            self.lazy[2*i+1] += v
            self.tree[2*i] += v
            self.tree[2*i+1] += v
    def add(self,l,r,x):
        ids = self.gindex(l,r)
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r&1:
                self.lazy[r-1] += x
                self.tree[r-1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1]) + self.lazy[i]
    def query(self,l,r):
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res


n, m = map(int, input().split())
al = list(map(int, input().split()))  # n個の箱内のボールの数
bl = list(map(int, input().split()))

st = LazySegTree_RAQ(
    init_val=al, segfunc=segfunc, ide_ele=float("inf"),
)

for b in bl:
    # 取り出す
    a = st.query(b, b + 1)
    st.add(b, b + 1, -a)
    # 全体への加算
    st.add(0, n, a // n)
    m = a % n  # 残り分
    if m == 0:
        continue
    # 最後まで
    st.add((b + 1)%n, min(n, (b + 1)%n + m), 1)
    m -= n - (b + 1)%n
    # あれば、残りを最初から
    if m < 1:
        continue
    st.add(0, m, 1)

ans = []
for i in range(n):
    v = st.query(i, i + 1)
    ans.append(v)
print(*ans)
