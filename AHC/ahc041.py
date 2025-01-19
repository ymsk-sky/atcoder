"""AHC041 A - Christmas Tree Cutting
N = 1000
1000 <= M <= 3000
H = 10
1 <= a <= 100
0 <= x, y <= 1000

美しさa, 高さhの頂点のスコア: (h + 1)*a
-> 美しさが大きいほど高い位置にあるべき

各木の直径を保持しておき, 隣接する木に接続可能なら接続したかった
"""

import random
import sys
from collections import deque
from time import time

program_start_ts = time()
random.seed(41)

LIMIT_TIME = 1.8  # この値[s]を超えると処理終了
C = 1.1  # 補正値: 処理時間*Cを考慮する(C>=1.0)

def input():
    return sys.stdin.readline().strip()

def check_stopping(crt_time: float, fin_time: float) -> bool:
    if fin_time == 0.0:
        return False
    loop_time = crt_time - fin_time
    return LIMIT_TIME - (crt_time - program_start_ts) <= loop_time*C

def calc_score(hl: list, al: list) -> int:
    res = 0
    for h, a in zip(hl, al):
        res += (h + 1)*a
    return res

def solve() -> None:
    fin_time = 0.0

    # 入力受付
    N, M, H = map(int, input().split())
    al = list(map(int, input().split()))  # al[i]: 頂点iの美しさ
    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    xyl = [list(map(int, input().split())) for _ in range(N)]  # xyl[i]: 頂点iの座標(x, y)

    k = sorted(al)[-N//3]  # 美しい上位1/3の閾値

    # 根を順に決定し, 高さH=10まで可能な限り伸ばしていく
    pl_l = []
    scores = []
    while 1:
        crt_time = time()
        if check_stopping(crt_time, fin_time):
            break

        rl = [random.randint(0, N) for _ in range(N)]
        ul = sorted(range(N), key=lambda i: rl[i])

        pl = [-1] * N
        hl = [-1] * N
        for u in ul:
            if hl[u] > -1:
                continue
            # 頂点uを根とする
            hl[u] = 0
            que = deque([u])
            while que:
                crt = que.popleft()
                for nxt in edges[crt]:
                    if hl[nxt] > -1:
                        continue
                    if al[nxt] >= k and hl[crt] <= H // 2:
                        # 美しいものは上位のときのみつなげる
                        continue
                    pl[nxt] = crt
                    hl[nxt] = hl[crt] + 1
                    if hl[nxt] < H:
                        que.append(nxt)
        for i in range(N):
            if pl[i] > -1:
                continue
            for j in edges[i]:
                if pl[j] == i:
                    break
            else:
                # 頂点iは単独のため近くのものに可能なら接続
                h_max = -1
                j_max = -1
                for j in edges[i]:
                    if hl[j] < H and hl[j] > h_max:
                        h_max = hl[j]
                        j_max = j
                pl[i] = j_max
                hl[i] = h_max + 1
        score = calc_score(hl, al)
        scores.append(score)
        pl_l.append(pl)
        fin_time = time()
    # 解答
    idx = max(range(len(scores)), key=lambda i: scores[i])
    print(*pl_l[idx])


if __name__ == "__main__":
    solve()


# cat .\tools_x86_64-pc-windows-gnu\in\0000.txt | python .\ahc041.py > out0000.txt
