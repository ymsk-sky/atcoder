import heapq
from collections import deque

h, w, X = map(int, input().split())
p, q = map(int, input().split())
p, q = p - 1, q - 1
sl = [list(map(int, input().split())) for _ in range(h)]

fin = [[False] * w for _ in range(h)]  # 高橋君かどうか
fin[p][q] = True

que = deque([])
wait = []
power = sl[p][q]

# 初期化
for y, x in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    u, v = p + y, q + x
    if 0 > u or u >= h or 0 > v or v >= w:
        continue
    if sl[u][v]*X >= power:
        heapq.heappush(wait, (sl[u][v], u, v))
    else:
        power += sl[u][v]
        que.append((u, v))
        fin[u][v] = True

while que:
    i, j = que.popleft()
    for y, x in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + y, j + x
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if fin[u][v]:
            continue
        if sl[u][v]*X >= power:
            heapq.heappush(wait, (sl[u][v], u, v))
            continue
        power += sl[u][v]
        que.append((u, v))
        fin[u][v] = True
    while wait:
        qower, i, j = heapq.heappop(wait)
        if fin[i][j]:
            continue
        if qower*X >= power:
            heapq.heappush(wait, (qower, i, j))
            break
        power += qower
        fin[i][j] = True
        que.append((i, j))

print(power)
