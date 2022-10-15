from bisect import bisect_left

h, w, rs, cs = map(int, input().split())
n = int(input())
rcl = [list(map(int, input().split())) for _ in range(n)]
q = int(input())

d_r = dict()
d_c = dict()
for r, c in rcl:
    if r in d_r:
        d_r[r].append(c)
    else:
        d_r[r] = [c]
    if c in d_c:
        d_c[c].append(r)
    else:
        d_c[c] = [r]
for k in d_r:
    d_r[k].append(0)
    d_r[k].append(w + 1)
    d_r[k] = sorted(d_r[k])
for k in d_c:
    d_c[k].append(0)
    d_c[k].append(h + 1)
    d_c[k] = sorted(d_c[k])

dll = [input().split() for _ in range(q)]

for d, l in dll:
    l = int(l)
    if d == "R":
        if rs in d_r:
            line = d_r[rs]
            wi = bisect_left(line, cs)
            wall = line[wi] - 1
            cs = min(wall, cs + l)
        else:
            cs = min(w, cs + l)
    elif d == "L":
        if rs in d_r:
            line = d_r[rs]
            wi = bisect_left(line, cs) - 1
            wall = line[wi] + 1
            cs = max(wall, cs - l)
        else:
            cs = max(1, cs - l)
    elif d == "U":
        if cs in d_c:
            line = d_c[cs]
            wi = bisect_left(line, rs) - 1
            wall = line[wi] + 1
            rs = max(wall, rs - l)
        else:
            rs = max(1, rs - l)
    elif d == "D":
        if cs in d_c:
            line = d_c[cs]
            wi = bisect_left(line, rs)
            wall = line[wi] - 1
            rs = min(wall, rs + l)
        else:
            rs = min(h, rs + l)
    print(rs, cs)

"""
2 <= h,w <= 10**9
1 <= rs <= h
1,= cs <= w
0 <= n <= 2 * 10**5
1 <= r <= h
1 <= c <= w
1 <= q <= 2 * 10**5
1 <= l <= 10**9
"""
