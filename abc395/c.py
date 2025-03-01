n = int(input())
al = list(map(int, input().split()))

d = dict()
for i, a in enumerate(al):
    if a not in d:
        d[a] = []
    d[a].append(i)

ans = n + 1
for l in d.values():
    if len(l) >= 2:
        for i, j in zip(l, l[1:]):
            tmp = j - i + 1
            ans = min(ans, tmp)
print(-1 if ans == n + 1 else ans)
