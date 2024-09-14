n = int(input())
xl = list(map(int, input().split()))
pl = list(map(int, input().split()))
q = int(input())
lrl = [list(map(int, input().split())) for _ in range(q)]

s = set()
for x in xl:
    s.add(x)
for l, r in lrl:
    s.add(l)
    s.add(r)

d = {i: v for i, v in enumerate(sorted(s), start=1)}
b = {v: i for i, v in enumerate(sorted(s), start=1)}
m = len(d)
ql = [0] * (m + 1)
for x, p in zip(xl, pl):
    xb = b[x]
    ql[xb] += p
for i in range(m):
    ql[i + 1] += ql[i]

for l, r in lrl:
    lb, rb = b[l], b[r]
    ans = ql[rb] - ql[lb - 1]
    print(ans)
