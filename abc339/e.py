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

n, d = map(int, input().split())
al = list(map(int, input().split()))
M = 5 * 10**5 + 1
# init_val[j]: 末尾がjのときの最大長
st = SegTree(
    init_val=[0] * (M + 1), segfunc=max, ide_ele=0,
)
for a in al:
    l = max(0, a - d)
    r = min(M - 1, a + d)
    bef = st.query(l, r + 1)
    st.update(a, bef + 1)
ans = st.query(0, M + 1)
print(ans)


"""
1<=n<=5*10**5
0<=d<=5*10**5
1<=a<=5*10**5

4 2
3 5 1 2


5 10
10 20 100 110 120

"""