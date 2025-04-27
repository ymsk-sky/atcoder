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
BLOCK = 2

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

def get_d(p: int, q: int) -> str:
    if p == 0:
        return " RL"[q]
    return " DU"[p]

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

    def bfs(si: int, sj: int, gi: int, gj: int) -> tuple[int, list]:
        """(si, sj) -> (gi, gj)への最短距離
        追加で移動を復元
        """
        dist = [[INF] * N for _ in range(N)]
        dist[si][sj] = 0
        que = deque([(si, sj)])
        while que:
            i, j = que.popleft()
            if i == gi and j == gj:
                break
            # 移動M
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                u, v = i + p, j + q
                if 0 > u or u >= N or 0 > v or v >= N:
                    continue
                if maze[u][v] == BLOCK:
                    continue
                if dist[u][v] <= dist[i][j] + 1:
                    continue
                dist[u][v] = dist[i][j] + 1
                que.append((u, v))
            # 滑走S
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                for x in range(1, N + 1):
                    u, v = i + x * p, j + x * q
                    if 0 > u or u >= N or 0 > v or v >= N or maze[u][v] == BLOCK:
                        u, v  = i + (x - 1) * p, j + (x - 1) * q
                        if dist[u][v] > dist[i][j] + 1:
                            dist[u][v] = dist[i][j] + 1
                            que.append((u, v))
                        break
        return dist[gi][gj], [("M", "?")]

    results = []
    # 移動前に壁を仮設置して、改善された場合のみ採用していく
    for idx in range(M - 1):
        crt_time = time()
        if check_stopping(crt_time, fin_time):
            break

        score_crt = 0  # 何もしない場合の現状のスコア
        for jdx in range(idx, M - 1):
            si, sj = goals[jdx]
            gi, gj = goals[jdx + 1]
            tmp, _ = bfs(si, sj, gi, gj)
            score_crt += tmp

        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            si, sj = goals[idx]
            u, v = si + p, sj + q
            if 0 > u or u >= N or 0 > v or v >= N:
                continue
            if maze[u][v] == BLOCK or maze[u][v] == GOAL:
                continue
            maze[u][v] = BLOCK
            score_tmp = 1  # 変更A
            for jdx in range(idx, M - 1):
                gi, gj = goals[jdx + 1]
                tmp, l_tmp = bfs(si, sj, gi, gj)
                score_tmp += tmp
                if jdx == idx:
                    l = l_tmp[:]

            if score_tmp < score_crt:
                # 採用
                results.append(("A", get_d(p, q)))
                results.extend(l)
            else:
                # 不採用
                maze[u][v] = 0  # 元に戻す

        fin_time = time()

    # 回答
    for res in results:
        print(*res)


if __name__ == "__main__":
    solve()
