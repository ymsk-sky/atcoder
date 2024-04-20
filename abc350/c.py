n = int(input())
al = list(map(int, input().split()))
d = {a: i for i, a in enumerate(al, start=1)}
e = {i: a for i, a in enumerate(al, start=1)}
cnt = 0
res = []
for a in range(1, n + 1):
    i = d[a]
    b = e[a]
    if a == b:
        continue
    j = d[b]
    d[a], d[b], e[i], e[j] = d[b], d[a], e[j], e[i]
    res.append((a, i))
    cnt += 1

print(cnt)
for r in res:
    print(*r)
