from math import gcd  # v3.4 math=>fractions
from functools import reduce
def gcd_list(nums):
    return reduce(gcd, nums)
n=int(input())
l=list(map(int,input().split()))
a=1
for i in range(n):
    t=l[:i]+l[i+1:]
    a=max(a,gcd_list(t))
print(a)
