from bisect import bisect_left
from collections import Counter


def segfunc(x,y):
    return x+y
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


n = int(input())
al = list(map(int, input().split()))

val_l = []
num_l = []
sum_l = []
for val, num in sorted(Counter(al).items()):
    val_l.append(val)
    num_l.append(num)
    sum_l.append(val * num)
st_num = SegTree(
    init_val=num_l, segfunc=segfunc, ide_ele=0,
)
st_sum = SegTree(
    init_val=sum_l, segfunc=segfunc, ide_ele=0,
)
l = len(val_l)
ans = 0
for a in al:
    i = bisect_left(val_l, a)
    tmp = st_sum.query(i + 1, l) - a*st_num.query(i + 1, l)
    ans += tmp
    st_num.add(i, -1)
    st_sum.add(i, -a)
print(ans)

print(val_l)
print(num_l)
print(sum_l)
