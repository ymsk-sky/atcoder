"""
切る候補は(l-1)個で、そこから異なる11個を選ぶので
(l-1)C11: コンビネーション
を求めればよい.
(l-1)C11 = ((l-1)(l-2)...(l-11))/11!
"""
from math import factorial
l=int(input())
a=1
for i in range(1,12):
    a*=(l-i)
b=factorial(11)  # 39916800
print(a//b)
