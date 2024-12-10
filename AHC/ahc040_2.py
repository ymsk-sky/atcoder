"""AHC040
Packing Uncertain Rectangles

30 <= N <= 100
N/2 <= T <= 4*N
1000 <= sigma <= 10000: 標準偏差σ
1 <= w,h <= 10**9

同じ面積でも正方形に近いほど(横幅+縦幅)の値は小さくなる = 正方形を目指す
"""
import random

TO_UP = "U"
TO_LEFT = "L"

def query(res: list) -> tuple:
    """結果を出力しそれに対応した横/縦幅を返す"""
    print(len(res))
    for p, r, d, b in res:
        print(p, r, d, b, flush=True)
    w, h = map(int, input().split())
    return w, h

def search(p: int, state: list) -> tuple:
    """左上に詰められる場所を探索
    斜めに走査して最初の空きに配置
    """
    n = len(state)
    for k in range(n):
        for i in range(k, -1, -1):
            _i, _j = i, k - i
            if state[_i][_j] > -1:
                continue
            if _i == 0 and _j == 0:
                state[_i][_j] = p
                return -1, TO_UP
            if _i == 0:
                state[_i][_j] = p
                return state[_i][_j - 1], TO_LEFT
            if _j == 0:
                state[_i][_j] = p
                return state[_i - 1][_j], TO_UP
            state[_i][_j] = p
            return [state[_i - 1][_j], state[_i][_j - 1]][random.randint(0, 1)], [TO_UP, TO_LEFT][random.randint(0, 1)]
    for k in range(n - 2, -1, -1):
        for i in range(k, -1, -1):
            j = k - i
            _i, _j = n - 1 - j, n - 1 - i
            if state[_i][_j] > -1:
                continue
            if _i == 0:
                state[_i][_j] = p
                return state[_i][_j - 1], TO_LEFT
            if _j == 0:
                state[_i][_j] = p
                return state[_i - 1][_j], TO_UP
            state[_i][_j] = p
            return [state[_i - 1][_j], state[_i][_j - 1]][random.randint(0, 1)], [TO_UP, TO_LEFT][random.randint(0, 1)]
    return -1, TO_UP

def solve() -> None:
    """解答
    左上に詰めていく
    """
    N, T, sigma = map(int, input().split())
    whl = [tuple(map(int, input().split())) for _ in range(N)]

    M = int(-(-N**0.5 // 1))

    res_list = []
    for _ in range(T - 1):
        res = []
        state = [[-1] * M for _ in range(M)]
        for p, (w, h) in enumerate(whl):
            # p:自分i, r:90度回転するか(0/1), d:方向(U/L), b:基準i
            r = random.randint(0, 1)
            q, d = search(p, state)
            res.append((p, r, d, q))
        W, H = query(res=res)
        res_list.append((W + H, res))
    ans = min(res_list)[1]
    # T回目=最終結果を出力
    print(len(ans))
    for an in ans:
        print(*an)


if __name__ == "__main__":
    solve()
