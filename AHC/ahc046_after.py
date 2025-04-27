"""AHC046

移動M, 滑走S, 変更A

上U 下D 左L 右R

# 条件
- 2*N*Mターン以内
"""

import sys
from collections import deque
from time import time

program_start_ts = time()


LIMIT_TIME = 1.8  # この値[s]を超えると処理終了
C = 1.0  # 補正値: 処理時間*Cを考慮(C>=1.0)
INF = 1 << 60
GOAL = 1
WALL = 2

def input() -> str:
    return sys.stdin.readline().strip()

def check_stopping(crt_time: float, fin_time: float) -> bool:
    if fin_time == 0.0:
        return False
    loop_time = crt_time - fin_time
    return LIMIT_TIME - (crt_time - program_start_ts) <= loop_time * C

def reverse_dir(d: str) -> str:
    """今の方向と逆向きを返す"""
    if d == "U":
        return "D"
    if d == "D":
        return "U"
    if d == "L":
        return "R"
    return "L"

def solve() -> None:
    """回答"""
    fin_time = 0.0

    # 入力受付
    N, M = map(int, input().split())  # N=20, M=40 固定
    # 目的地は全て異なる
    goals = [list(map(int, input().split())) for _ in range(M)]

    maze = [[0] * N for _ in range(N)]  # マスの現在の状態
    for i, j in goals:
        maze[i][j] = GOAL

    def bfs(si: int, sj: int, gi: int, gj: int) -> int:
        """(si, sj) -> (gi, gj)への最短距離"""
        dist = [[INF] * N for _ in range(N)]
        dist[si][sj] = 0
        que = deque([(si, sj)])
        while que:
            i, j = que.popleft()
            # 移動M
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                u, v = i + p, j + q
                if 0 > u or u >= N or 0 > v or v >= N:
                    continue
                if maze[u][v] == WALL:
                    continue
                if dist[u][v] <= dist[i][j] + 1:
                    continue
                dist[u][v] = dist[i][j] + 1
                que.append((u, v))
            # 滑走S
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                for x in range(1, N + 1):
                    u, v = i + x * p, j + x * q
                    if 0 > u or u >= N or 0 > v or v >= N or maze[u][v] == WALL:
                        u, v  = i + (x - 1) * p, j + (x - 1) * q
                        if dist[u][v] > dist[i][j] + 1:
                            dist[u][v] = dist[i][j] + 1
                            que.append((u, v))
                        break
        return dist[gi][gj]

    sl = [[] for _ in range(M)]  # 移動後に壁を設置する記録
    for idx in range(M - 1):
        crt_time = time()
        if check_stopping(crt_time, fin_time):
            break
        # 目的地に到着時に壁を仮設置して、改善された場合のみ採用
        score_max = 0  # 何もしない場合の現状のスコア
        for jdx in range(M - 1):
            si, sj = goals[jdx]
            gi, gj = goals[jdx + 1]
            score_max += bfs(si, sj, gi, gj)

        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            score_tmp = 0
            for jdx in range(M - 1):
                si, sj = goals[jdx]
                gi, gj = goals[jdx + 1]
                score_tmp += bfs(si, sj, gi, gj)
                if jdx + 1 == idx:
                    u, v = gi + p, gj + q
                    if 0 > u or u >= N or 0 > v or v >= N:
                        continue
                    if maze[u][v] == WALL or maze[u][v] == GOAL:
                        continue
                    score_tmp += 1  # 変更A
                    maze[u][v] = WALL

        fin_time = time()

    # 回答
    print("fin", idx)


if __name__ == "__main__":
    solve()
