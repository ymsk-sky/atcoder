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
sys.setrecursionlimit(10**7)

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
    """移動(p, q)の値から方向文字列を返す"""
    if p == 0:
        return " RL"[q]
    return " DU"[p]

def solve() -> None:
    """回答"""
    fin_time = 0.0

    # 入力受付
    N, M = map(int, input().split())  # N=20, M=40 固定
    goals = [list(map(int, input().split())) for _ in range(M)]  # 目的地は全て異なる

    maze = [[0] * N for _ in range(N)]  # マスの現在の状態
    for i, j in goals:
        # 到着予定地にはブロックを置かないように管理
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
                        u, v = i + (x - 1) * p, j + (x - 1) * q
                        if dist[u][v] > dist[i][j] + 1:
                            dist[u][v] = dist[i][j] + 1
                            que.append((u, v))
                        break
        res = dist[gi][gj]

        # 経路復元してそのときの行動列を生成
        l = []
        fin = [[False] * N for _ in range(N)]
        def dfs(i: int, j: int) -> bool:
            if i == si and j == sj:
                return True
            if fin[i][j]:
                return False
            # 移動M
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                u, v = i + p, j + q
                if 0 > u or u >= N or 0 > v or v >= N:
                    continue
                if dist[i][j] - 1 == dist[u][v]:
                    l.append(("M", reverse_dir(get_d(p, q))))
                    if dfs(u, v):
                        return True
                    l.pop()
            # 滑走S
            for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                _u, _v = i - p, j - q
                if 0 > _u or _u >= N or 0 > _v or _v >= N or maze[_u][_v] == BLOCK:
                    for x in range(1, N + 1):
                        u, v = i + x * p, j + x * q
                        if 0 > u or u >= N or 0 > v or v >= N or maze[u][v] == BLOCK:
                            break
                        if dist[i][j] - 1 == dist[u][v]:
                            l.append(("S", reverse_dir(get_d(p, q))))
                            if dfs(u, v):
                                return True
                            l.pop()
            fin[i][j] = True
            return False
        dfs(gi, gj)
        return res, l[::-1]

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
            tmp, l_tmp = bfs(si, sj, gi, gj)
            score_crt += tmp
            if jdx == idx:
                res_ready = l_tmp[:]

        for p, q in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            si, sj = goals[idx]
            u, v = si + p, sj + q
            # 対象がマス外, 既にブロック, 到達予定地の場合はスキップ
            if 0 > u or u >= N or 0 > v or v >= N or maze[u][v] == BLOCK or maze[u][v] == GOAL:
                continue
            maze[u][v] = BLOCK
            score_tmp = 1  # 変更A
            for jdx in range(idx, M - 1):
                gi, gj = goals[jdx + 1]
                tmp, l_tmp = bfs(si, sj, gi, gj)
                score_tmp += tmp
                if jdx == idx:
                    l = l_tmp[:]
                si, sj = gi, gj

            maze[u][v] = 0  # 元に戻しておく
            if score_tmp < score_crt:
                # 採用準備
                res_ready = [("A", get_d(p, q))] + l[:]
                score_crt = score_tmp
                uv = (u, v)
            else:
                # 不採用
                si, sj = goals[idx]
                gi, gj = goals[idx + 1]
                _, l = bfs(si, sj, gi, gj)
                res_ready = l[:]
                uv = None
        results.extend(res_ready)
        if uv is not None:
            u, v = uv
            maze[u][v] = BLOCK

        fin_time = time()

    # 回答
    for res in results:
        print(*res)


if __name__ == "__main__":
    solve()
