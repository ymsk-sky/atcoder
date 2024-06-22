def segfunc(x,y):
    return max(x,y)
class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
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
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v
    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def query(self,l,r):
        ids = self.gindex(l,r)
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


n = int(input())
hl = list(map(int, input().split()))
s = set(hl + [float("inf")])
m = len(s)
e = {h: i + 1 for i, h in enumerate(sorted(s))}
lst = LazySegTree_RUQ(
    init_val=[0] * (m + 2), segfunc=segfunc, ide_ele=0,
)
ans = [0]
h_max = 0
i_max = 0
for i, h in enumerate(hl, start=1):
    if h >= h_max:
        res = h*i + 1
        h_max = h
        i_max = i
    else:
        bef = lst.query(e[h], e[h] + 1)
        res = ans[bef] +  h*(i - bef)
    ans.append(res)
    lst.update(0, e[h], i)
print(*ans[1:])

"""
1<=n<=2*10**5
1<=h<=10**9
"""
