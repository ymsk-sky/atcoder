"""AHC040
Packing Uncertain Rectangles

30 <= N <= 100
N/2 <= T <= 4*N
1000 <= sigma <= 10000: 標準偏差σ
1 <= w,h <= 10**9

同じ面積でも正方形に近いほど(横幅+縦幅)の値は小さくなる = 正方形を目指す
"""

C = 0.9

def query(res: list) -> tuple:
    """結果を出力しそれに対応した横/縦幅を返す"""
    print(len(res))
    for p, r, d, b in res:
        print(p, r, d, b, flush=True)
    w, h = map(int, input().split())
    return w, h

def solve() -> None:
    """解答"""
    N, T, sigma = map(int, input().split())
    whl = [tuple(map(int, input().split())) for _ in range(N)]

    m_max = int(-(-sum([max(w, h) for w, h in whl]) // N**0.5))
    m_min = int(-(-sum([min(w, h) for w, h in whl]) // N**0.5))
    interval = (m_max - m_min) // (T - 2)

    res_list = []
    for x_len in range(m_min, m_max + 1, interval)[:T-1]:
        res = []
        b = -1
        y_sum = 0  # 全てのy軸長
        y_max = 0
        x_line = 0
        for p, (w, h) in enumerate(whl):
            # p:自分i, r:90度回転するか(0/1), d:方向(U/L), b:基準i
            """回転方向を決定"""
            r = 0
            if y_sum*C >= x_len:
                # 横長に配置
                if h > w:
                    h, w = w, h
                    r = 1
            else:
                # 縦長に配置
                if w > h:
                    h, w = w, h
                    r = 1
            """設置場所を決定"""
            if x_line + w <= x_len:
                d = "L"
                x_line += w
                y_max = max(y_max, h)
            else:
                d = "U"
                x_line = w
                y_sum += y_max
                y_max = h
                b = -1
            res.append((p, r, d, b))
            b = p
        W, H = query(res=res)
        res_list.append((W + H, res))
    ans = min(res_list)[1]
    # T回目=最終結果を出力
    print(len(ans))
    for an in ans:
        print(*an)


if __name__ == "__main__":
    solve()
