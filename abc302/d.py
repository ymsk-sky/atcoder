from bisect import bisect_right

n, m, d = map(int, input().split())
al = list(map(int, input().split()))
bl = list(map(int, input().split()))
al.sort()
bl.sort()

ans = -1
for a in al:
    for x in (-1, 0, 1):
        ad = a + x*d
        i = bisect_right(bl, ad)
        for j in (i - 1, i, i + 1):
            if j >= m:
                continue
            b = bl[j]
            dif = abs(a - b)
            if dif <= d:
                ans = max(ans, a + b)

print(ans)
