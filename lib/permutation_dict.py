"""
1~Nまでの順列　(1, 2, 3, ..., Nを並び替えてできる数列) の個数はN!個.

# kth_perm
- ある順列Pが与えられたときにその順列が辞書順で何番目かを出力する.

# index_of_permutation
- また長さNの順列Qが辞書順で何番目かを出力する.
"""

from math import factorial
def index_of_permutation(L):
    index = 0
    while len(L) > 1:
        a = len([l for l in L if l < L[0]])
        index = index + a*factorial(len(L) - 1)
        L = L[1:]
    return index


def kth_perm(n, k):
    S = list(range(1, n + 1))
    rs = []
    for i in range(1, n + 1):
        r = k%i
        k //= i
        rs.append(r)
    ans = []
    for r in rs[::-1]:
        s = S[r]
        ans.append(s)

        S = S[:r] + S[r+1:]
    return ans
