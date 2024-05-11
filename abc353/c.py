from bisect import bisect_left

n = int(input())
al = list(map(int, input().split()))
al.sort()
s = sum(al)
M = 10**8
ans = 0
for i, a in enumerate(al):
    s -= a
    ans += a * (n - i - 1) + s
    j = bisect_left(al, M - a)
    j = max(i + 1, j)
    ans -= M * (n - j)
print(ans)

"""
2<=n<=3*10**5
1<=a<10**8
"""