"""メモ化再帰
期待値
DP
"""

import sys
from functools import lru_cache
sys.setrecursionlimit(10**7)

n, a, x, y = map(int, input().split())
@lru_cache(maxsize=10**7)
def f(n):
    if n == 0:
        return 0
    res1 = x + f(n // a)
    res2 = 6/5*y + (f(n // 2) + f(n // 3) + f(n // 4) + f(n // 5) + f(n // 6))/5
    return min(res1, res2)

ans = f(n)
print(ans)

"""
1<=n<=10**18
2<=a<=6
1<=x,y<=10**9

期待値とは, 確率の逆数
* 有効なカードを引く期待値は, 有効なカードを引く確率の逆数
-> 3/40でカードを引く期待値は, 40/3 = 13.3333333
"""