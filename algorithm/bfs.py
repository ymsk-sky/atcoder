"""
幅優先探索(BFS: Breadth First Search)

AtCoder ABC007 C問題に対応
https://atcoder.jp/contests/abc007/tasks/abc007_3

(example input)
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########

"""

from collections import deque

# 入力受付
r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
m = [input() for _ in range(r)]

# スタート地点からの距離を格納していく配列(未探索を-1で初期化)
visited = [[-1]*c for _ in range(r)]
# 値を-1する(インデックスとして使用するため)
sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1

def bfs(sy, sx, gy, gx, m, visited):
    visited[sy][sx] = 0
    q = deque([])
    q.append([sy, sx])
    while q:
        y, x = q.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if m[y+i][x+j] == '.' and visited[y+i][x+j] == -1:
                # 探索可能(道である)かつ未探索の場合
                visited[y+i][x+j] = visited[y][x] + 1
                q.append([y+i, x+j])

print(bfs(sy, sx, gy, gx, m, visited))
