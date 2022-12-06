import sys
sys.setrecursionlimit(10 ** 9)

# メモ化再帰
n = int(input())

fl = [0] * (n + 1)

def f(k):
    if k == 0:
        return 0
    if fl[k] > 0:
        return fl[k]
    ans = float("inf")
    ans = min(ans, f(k - 1) + 1)
    x = 6
    while x <= k:
        ans = min(ans, f(k - x) + 1)
        x *= 6
    x = 9
    while x <= k:
        ans = min(ans, f(k - x) + 1)
        x *= 9

    fl[k] = ans
    return ans

print(f(n))
