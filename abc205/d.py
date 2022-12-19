"""二分探索
A=(A1,A2,...,AN)
においてAi未満の「良い整数」は(Ai - i)個ある
よって S(A1-1,A2-2,...,AN-N)とすると
KがSのどの要素に入るかを二分探索で調べれば, どのAi以上A(i+1)未満かがわかる
"""
from bisect import bisect_left

n, q = map(int, input().split())
al = list(map(int, input().split()))
sl = [al[i] - (i + 1) for i in range(n)]
kl = [int(input()) for _ in range(q)]
for k in kl:
    ix = bisect_left(sl, k)
    if ix == 0:
        print(k)
    else:
        # K未満,最大,使用不可の数字 + (K -)
        print(al[ix - 1] + (k - sl[ix - 1]))
"""
K = 3: ix = 2
1 2 3 4 5 6
  2 3   o 6
al = [2, 3, 6]
sl = [1, 1, 3]
3 + (3 - 1) = 5
"""