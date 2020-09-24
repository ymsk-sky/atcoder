from collections import deque

# 入力受付
h, w, t=map(int, input().split())
ss = [input() for _ in range(h)]

# Sからの距離を格納(白[.]:要素0, 黒[#]:要素1) -> 幅優先探索(BFS)
visited = [[[-1, -1]] * w for _ in range(h)]

# スタートとゴールを探索
for i in range(h):
    for j in range(w):
        if ss[i][j] == 'S':
            sy, sx = i, j
        if ss[i][j] == 'G':
            gy, gx = i, j

visited[sx][sy] = 0
q = deque([])
q.append([sx, sy])
while q:
    x, y = q.popleft()
    if [x, y] == [gx, gy]:
        pass
    for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        if 0<=y+i<=h and 0<=x+j<=w:
            if ss[y+i][x+j]
