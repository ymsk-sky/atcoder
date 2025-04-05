from collections import deque

INF = float("inf")

h, w = map(int, input().split())
sl = [input() for _ in range(h)]
a, b, c, d = map(int, input().split())
a, b, c, d = a - 1, b - 1, c - 1, d - 1

dist = [[INF] * w for _ in range(h)]
dist[a][b] = 0
que = deque([(a, b)])
while que:
    i, j = que.popleft()
    d_tmp = dist[i][j]
    for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        u, v = i + p, j + q
        if 0 > u or u >= h or 0 > v or v >= w:
            continue
        if sl[u][v] == "#":  # 前蹴り
            if dist[u][v] > d_tmp + 1:
                dist[u][v] = d_tmp + 1
                que.append((u, v))
            if p == 1 and u + 1 < h and sl[u + 1][v] == "#" and dist[u + 1][v] > d_tmp + 1:
                dist[u + 1][v] = d_tmp + 1
                que.append((u + 1, v))
            elif p == -1 and u - 1 >= 0 and sl[u - 1][v] == "#" and dist[u - 1][v] > d_tmp + 1:
                dist[u - 1][v] = d_tmp + 1
                que.append((u - 1, v))
            elif q == 1 and v + 1 < w and sl[u][v + 1] == "#" and dist[u][v + 1] > d_tmp + 1:
                dist[u][v + 1] = d_tmp + 1
                que.append((u, v + 1))
            elif q == -1 and v - 1 >= 0 and sl[u][v - 1] == "#" and dist[u][v - 1] > d_tmp + 1:
                dist[u][v - 1] = d_tmp + 1
                que.append((u, v - 1))
        else:
            if dist[u][v] <= d_tmp:
                continue
            dist[u][v] = d_tmp
            que.appendleft((u, v))

ans = dist[c][d]
print(ans)


print(*dist, sep="\n")

"""
10 10
S.........
#########.
#.......#.
#..####.#.
##....#.#.
#####.#.#.
G##.#.#.#.
###.#.#.#.
###.#.#.#.
#.....#...
1 1 7 1

"""