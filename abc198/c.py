from math import ceil,sqrt
from decimal import Decimal as D
r,x,y=map(int,input().split())
d=D(x**2+y**2)**D('0.5')
dpr=D(d/r)
if dpr<1:
    print(2)
else:
    print(ceil(dpr))
