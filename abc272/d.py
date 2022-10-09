from collections import deque

n, m = map(int, input().split())

"""
(a, b) -> (a + i, b + j) の移動
iをforで回して i**2 + j**2 = m なる整数jが存在するかを判定
"""
move = []
for i in range(m + 1):
    j = m - i ** 2
    if j < 0:
        # iは単調増加のため一旦jがマイナスになると以降すべてマイナスのため打ち切り
        break
    j **= 0.5
    if int(j) == j:
        j = int(j)
        move.append([i, j])
        move.append([i, -j])
        move.append([-i, j])
        move.append([-i, -j])

dist = [[-1] * n for _ in range(n)]
dist[0][0] = 0

def judge(x, y):
    return 0 <= x < n and 0 <= y < n and dist[x][y] == -1

q = deque()
q.append([0, 0])

while q:
    i, j = q.popleft()
    for a, b in move:
        k, l = i + a, j + b
        if judge(k, l):
            dist[k][l] = dist[i][j] + 1
            q.append([k, l])

for d in dist:
    print(*d)
