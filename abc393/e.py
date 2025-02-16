n, k = map(int, input().split())
al = list(map(int, input().split()))

m = max(al)
sl = [0] * (m + 1)
for a in al:
    sl[a] += 1

tl = [0] * (m + 1)
for i in range(1, m + 1):
    for j in range(i, m + 1, i):
        tl[i] += sl[j]

ans = [0] * (m + 1)
for i in range(1, m + 1):
    if tl[i] < k:
        continue
    for j in range(i, m + 1, i):
        ans[j] = max(ans[j], i)

for a in al:
    print(ans[a])
