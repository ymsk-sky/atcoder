from bisect import bisect_left, bisect_right
from collections import defaultdict

M = 10**15
n, m, sx, sy = map(int, input().split())
xd = defaultdict(list)
yd = defaultdict(list)
for _ in range(n):
    x, y = map(int, input().split())
    xd[x].append(y)
    yd[y].append(x)

for x in xd.keys():
    xd[x] = sorted(xd[x])
for y in yd.keys():
    yd[y] = sorted(yd[y])

for x in xd.keys():
    xd[x].append(M)
for y in yd.keys():
    yd[y].append(M)

acc_xd = {x: [0] * len(xd[x]) for x in xd.keys()}
acc_yd = {y: [0] * len(yd[y]) for y in yd.keys()}

for _ in range(m):
    d, c = input().split()
    c = int(c)
    if d == "U":
        sy += c
        if sx not in xd:
            continue
        i = bisect_left(xd[sx], sy - c)
        j = bisect_right(xd[sx], sy)
        acc_xd[sx][i] += 1
        acc_xd[sx][j] -= 1
    elif d == "D":
        sy -= c
        if sx not in xd:
            continue
        i = bisect_left(xd[sx], sy)
        j = bisect_right(xd[sx], sy + c)
        acc_xd[sx][i] += 1
        acc_xd[sx][j] -= 1
    elif d == "L":
        sx -= c
        if sy not in yd:
            continue
        i = bisect_left(yd[sy], sx)
        j = bisect_right(yd[sy], sx + c)
        acc_yd[sy][i] += 1
        acc_yd[sy][j] -= 1
    elif d == "R":
        sx += c
        if sy not in yd:
            continue
        i = bisect_left(yd[sy], sx - c)
        j = bisect_right(yd[sy], sx)
        acc_yd[sy][i] += 1
        acc_yd[sy][j] -= 1

ans = set()

for x in xd.keys():
    size = len(acc_xd[x])
    l = acc_xd[x]
    for i in range(size - 1):
        l[i + 1] += l[i]
    xl = xd[x]
    for i in range(size - 1):
        if l[i] > 0:
            ans.add((x, xl[i]))
for y in yd.keys():
    size = len(acc_yd[y])
    l = acc_yd[y]
    for i in range(size - 1):
        l[i + 1] += l[i]
    yl = yd[y]
    for i in range(size - 1):
        if l[i] > 0:
            ans.add((yl[i], y))

print(sx, sy, len(ans))
