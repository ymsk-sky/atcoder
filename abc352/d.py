class SegTree:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def add(self,k,x):
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def update(self,k,x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def query(self,l,r):
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


n, k = map(int, input().split())
pl = list(map(int, input().split()))
# index
ql = [0] * n
for i, p in enumerate(pl):
    ql[p - 1] = i + 1
INF = float("inf")
st_max = SegTree(
    init_val=ql, segfunc=max, ide_ele=-INF,
)
st_min = SegTree(
    init_val=ql, segfunc=min, ide_ele=INF,
)
ans = INF
for i in range(n - k + 1):
    mx = st_max.query(i, i + k)
    mi = st_min.query(i, i + k)
    ans = min(ans, mx - mi)
print(ans)
