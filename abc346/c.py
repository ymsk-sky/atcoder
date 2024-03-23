n, k = map(int, input().split())
al = list(map(int, input().split()))
ans = k * (k + 1) // 2
for a in set(al):
    if a <= k:
        ans -= a
print(ans)

"""
1<=n<=2*10**5
1<=k<=2*10**9
1<=a<=2*10**9

1 2 3 4 5
15-1-3

1 6 3 1
"""