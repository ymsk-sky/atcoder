"""
a以上b以下のcでもdでも割り切れない整数の数
->cまたはd(もしくは両方)で割り切れる数
"""
from math import gcd
a,b,c,d=map(int,input().split())
e=(c*d)//gcd(c,d)  # cとdの最小公倍数
xc=b//c - (a-1)//c
xd=b//d - (a-1)//d
xe=b//e - (a-1)//e
print(b-a+1-xc-xd+xe)
"""
10 40 6 8
23
  1    2    3    4    5    6.   7    8*   9  |10
 11   12.  13   14   15   16*  17   18.  19   20
 21   22   23   24.* 25   26   27   28   29   30.
 31   32*  33   34   35   36.  37   38   39   40*
|41   42.  ...

6->5.
8->4*
最小公倍数=24->1
31 - 8
"""
