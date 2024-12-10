import random
import sys
from time import time
from typing import Tuple

program_start_ts = time()
random.seed(40)

INF = 10**12
X = 1.2  # 外箱の横幅を補正する定数(最小/最大の幅*Xの範囲にする)
C = 1.2  # ループ時間を補正する定数(測定時間*Cの値を参考にする)
LIMIT_TIME = 2.6  # この時間経過すると最後の処理へ移る(途中打ち切り)

def input():
    return sys.stdin.readline().strip()

def check_stopping(crt_time: float, fin_time: float) -> bool:
    if fin_time == 0.0:
        return False
    loop_time = crt_time - fin_time  # 1つ解答する時間
    # 残り時間が今回のループ時間(*補正値)分余っているならTrue
    return LIMIT_TIME - (crt_time - program_start_ts) <= loop_time*C

def query(res: list, is_last: bool = False) -> Tuple[int, int]:
    """結果を出力しそれに対応した横/縦幅を返す"""
    print(len(res), flush=True)
    for p, r, d, b in res:
        print(p, r, d, b, flush=True)
    if is_last:
        return -1, -1
    w, h = map(int, input().split())
    return w, h

def solve() -> None:
    """解答
    横幅は最低/最高幅を決めて, その範囲でランダムに(T - 1)個生成する
    """
    N, T, sigma = map(int, input().split())
    whl = [tuple(map(int, input().split())) for _ in range(N)]
    ROOT_N = N**0.5

    res_list = []  # (W + H, res)
    fin_time = 0.0
    interval = int(-(-ROOT_N // 1))
    for _ in range(T - 1):
        # TLE対策: 残り時間が足りそうにない場合は途中打ち切り
        crt_time = time()
        if check_stopping(crt_time, fin_time):
            break

        res = []
        for st in range(0, N, interval):
            q = -1
            for p in range(st, min(st + interval, N)):
                w, h = whl[p]
                # p:自分i, r:90度回転するか(0/1), d:方向(U/L), b:基準i
                """回転方向を決定"""
                # 通常と回転を乱択
                r = random.randint(0, 1)
                if r:
                    w, h = h, w
                """設置場所を確定"""
                res.append((p, r, "U", q))
                q = p
        W, H = query(res=res)
        res_list.append((W + H, res))
        fin_time = time()
    # 途中で打ち切った場合に残り回数を消費
    for _ in range(T - 1 - len(res_list)):
        query([])
    ans = min(res_list)[1]
    # T回目=最終結果を出力
    query(ans, is_last=True)


if __name__ == "__main__":
    solve()
