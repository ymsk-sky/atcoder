import heapq

h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]
bl = [list(map(int, input().split())) for _ in range(h)]
INF = float("inf")
d_h = dict()
que = [(0, list(range(h)))]
heapq.heapify(que)
while que:
    cnt, l = heapq.heappop(que)
    if tuple(l) in d_h:
        continue
    d_h[tuple(l)] = cnt
    for i in range(h - 1):
        tmp = l[:]
        tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
        if tuple(tmp) in d_h:
            continue
        heapq.heappush(que, (cnt + 1, tmp))
d_w = dict()
que = [(0, list(range(w)))]
heapq.heapify(que)
while que:
    cnt, l = heapq.heappop(que)
    if tuple(l) in d_w:
        continue
    d_w[tuple(l)] = cnt
    for i in range(w - 1):
        tmp = l[:]
        tmp[i], tmp[i + 1] = tmp[i + 1], tmp[i]
        if tuple(tmp) in d_w:
            continue
        heapq.heappush(que, (cnt + 1, tmp))

ans = INF
for k_h in d_h.keys():
    for k_w in d_w.keys():
        f = True
        for i_b, i_a in enumerate(k_h):
            for j_b, j_a in enumerate(k_w):
                if al[i_a][j_a] == bl[i_b][j_b]:
                    continue
                else:
                    f = False
        if f:
            tmp = d_h[k_h] + d_w[k_w]
            ans = min(ans, tmp)
print(-1 if ans == INF else ans)
