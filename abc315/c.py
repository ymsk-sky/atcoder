n = int(input())
d = dict()
for _ in range(n):
    f, s = map(int, input().split())
    if f in d:
        d[f].append(s)
    else:
        d[f] = [s]

for k in d:
    d[k] = sorted(d[k], reverse=True)

ans = -1
for k in d:
    if len(d[k]) > 1:
        a, b = d[k][:2]
        ans = max(ans, a + b//2)
l = []
for k in d:
    l.append(d[k][0])
l.sort(reverse=True)
ans = max(ans, sum(l[:2]))

print(ans)
