from bisect import bisect_left, bisect_right

INF = float("inf")

n, q = map(int, input().split())
al = list(map(int, input().split()))
rxl = [list(map(int, input().split())) for _ in range(q)]

d = dict()
for i, (r, _) in enumerate(rxl):
    if r not in d:
        d[r] = []
    d[r].append(i)
ans = [0] * q
dp = [INF]
for idx, a in enumerate(al, start=1):
    i = bisect_left(dp, a)
    if i == len(dp):
        dp.append(a)
    else:
        dp[i] = a
    if idx not in d:
        continue
    for j in d[idx]:
        _, x = rxl[j]
        res = bisect_right(dp, x)
        ans[j] = res
print(*ans, sep="\n")
