"""AHC046

移動M, 滑走S, 変更A

上U 下D 左L 右R

# 条件
- 2*N*Mターン以内
"""

import sys
from time import time

program_start_ts = time()


LIMIT_TIME = 1.8  # この値[s]を超えると処理終了
C = 1.1  # 補正値: 処理時間*Cを考慮(C>=1.0)

def input() -> str:
    return sys.stdin.readline().strip()

def check_stopping(crt_time: float, fin_time: float) -> bool:
    if fin_time == 0.0:
        return False
    loop_time = crt_time - fin_time
    return LIMIT_TIME - (crt_time - program_start_ts) <= loop_time*C

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
    crt_i, crt_j = map(int, input().split())
    goals = [list(map(int, input().split())) for _ in range(M - 1)]

    results = []

    # 貪欲 + 改善: 移動 > 滑空後に移動 の場合に滑空を使用
    for nxt_i, nxt_j in goals:
        dif_i = nxt_i - crt_i
        if dif_i > 0:
            d = "D"
        else:
            d = "U"
        dif_i = abs(dif_i)
        if d == "D":
            tmp = 1 + (N - 1) - nxt_i
            if tmp < dif_i:
                results.append(("S", d))
                d = reverse_dir(d)
                dif_i = (N - 1) - nxt_i
        elif d == "U":
            tmp = 1 + nxt_i - 0
            if tmp < dif_i:
                results.append(("S", d))
                d = reverse_dir(d)
                dif_i = nxt_i - 0
        for _ in range(dif_i):
            results.append(("M", d))
        dif_j = nxt_j - crt_j
        if dif_j > 0:
            d = "R"
        else:
            d = "L"
        dif_j = abs(dif_j)
        if d == "R":
            tmp = 1 + (N - 1) - nxt_j
            if tmp < dif_j:
                results.append(("S", d))
                d = reverse_dir(d)
                dif_j = (N - 1) - nxt_j
        elif d == "L":
            tmp = 1 + nxt_j - 0
            if tmp < dif_j:
                results.append(("S", d))
                d = reverse_dir(d)
                dif_j = nxt_j - 0
        for _ in range(dif_j):
            results.append(("M", d))

        crt_i, crt_j = nxt_i, nxt_j

    # while 1:
    #     crt_time = time()
    #     if check_stopping(crt_time, fin_time):
    #         break
    #     fin_time = time()

    # 回答
    for res in results:
        print(*res)


if __name__ == "__main__":
    solve()
