n = int(input())
al = list(map(int, input().split()))
d = {}
for a in al:
    if a not in d:
        d[a] = 0
    d[a] += 1
e = {}
ans = 0
for a in al:
    d[a] -= 1
    if d[a] == 0:
        del d[a]
    if a not in e:
        e[a] = 0
    e[a] += 1
    tmp = len(d) + len(e)
    ans = max(ans, tmp)
print(ans)
