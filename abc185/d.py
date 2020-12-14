"""
連続した白マスの部分を求める.
 - n個の部分
 - 各長さはx

xooxoooxooxxooxo
||  |   |  ||  | |

13 3
13 3 9
ooxoooooxooox
"""
from math import ceil
n,m=map(int,input().split())
al=sorted(list(map(int,input().split()))+[0,n+1])
xl=[b-a-1 for a,b in zip(al,al[1:]) if b-a-1>0]  # 連続した白マス部分の長さxのリスト
if not xl:  # 押す場所なし
    print(0)
    exit()
k=min(xl)  # 作成するハンコの長さ
ans=0
for x in xl:
    ans+=ceil(x/k)
print(ans)
