h, w, d = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
lrl = [list(map(int, input().split())) for _ in range(q)]

positions = [None] * (h*w + 1)
for i in range(h):
    for j in range(w):
        a = al[i][j]
        positions[a] = (i, j)

dists = dict()
for i in range(1, h*w + 1):
    if i - d > 0:
        break
    dists[i] = [0]
    for j in range(i, h*w - d + 1, d):
        pi, pj = positions[j]
        qi, qj = positions[j + d]
        dists[i].append(abs(pi - qi) + abs(pj - qj))

for k in dists:
    for i in range(1, len(dists[k])):
        dists[k][i] += dists[k][i - 1]

for l, r in lrl:
    head = d if r%d == 0 else r%d
    dist = dists[head]
    print(dist[-(-r//d) - 1] - dist[-(-l//d) - 1])