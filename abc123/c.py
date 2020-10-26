"""
最小パイプをイメージ
水が15L/s流れるパイプと12L/sのパイプを繋げた場合、
全体では12L/sとなる。

最小の交通機関 * 回数 + その交通機関を使っていない時間が答えとなる
"""
from math import ceil
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
print(ceil(n/min(a,b,c,d,e))+4)
