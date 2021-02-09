from math import sqrt,ceil,floor
from decimal import Decimal as D
X,Y,R=[D(a) for a in input().split()]
ans=0
""" xの範囲を求める """
xmin=ceil(X-R)
xmax=floor(X+R)
""" 円内部のx=M*c(cは整数)すべてについてyの範囲を求めてカウントしていく """
R2=R**2
for x in range(xmin,xmax+1):
    y=(R2-(X-x)**2).sqrt()
    ymin=ceil(Y-y)
    ymax=floor(Y+y)
    cnt=ymax-ymin+1
    ans+=cnt
print(ans)


"""
0.2 0.8 1.1
3
"""
