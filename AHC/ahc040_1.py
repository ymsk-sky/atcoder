"""AHC040
Packing Uncertain Rectangles

30 <= N <= 100
N/2 <= T <= 4*N
1000 <= sigma <= 10000: 標準偏差σ
1 <= w,h <= 10**9

同じ面積でも正方形に近いほど(横幅+縦幅)の値は小さくなる = 正方形を目指す
"""

import random
from typing import List, Tuple

INF = 1 << 60

class Rect:
    def __init__(self, x: int, y: int, w: int, h: int, r: int = 0, p: int = -1) -> None:
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
        self.w = w
        self.h = h
        self.r = r  # 回転しているか
        self.p = p  # 長方形の番号

    def overlap(self, b: "Rect"):
        return max(self.x1, b.x1) < min(self.x2, b.x2) and max(self.y1, b.y1) < min(self.y2, b.y2)

    def subtract_by(self, b: "Rect") -> List["Rect"]:
        if self.overlap(b):
            rooms = []
            if (self.x1 < b.x1 and b.x1 < self.x2) and max(self.y1, b.y1) < min(self.y2, b.y2):
                rooms.append(Rect(self.x1, self.y1, b.x1 - self.x1, self.h))
            if (self.x1 < b.x2 and b.x2 < self.x2) and max(self.y1, b.y1) < min(self.y2, b.y2):
                rooms.append(Rect(b.x2, self.y1, self.x2 - b.x2, self.h))
            if (self.y1 < b.y1 and b.y1 < self.y2) and max(self.x1, b.x1) < min(self.x2, b.x2):
                rooms.append(Rect(self.x1, self.y1, self.w, b.y1 - self.y1))
            if (self.y1 < b.y2 and b.y2 < self.y2) and max(self.x1, b.x1) < min(self.x2, b.x2):
                rooms.append(Rect(self.x1, b.y2, self.w, self.y2 - b.y2))
            return rooms
        else:
            return [self]

    def include(self, b: "Rect") -> bool:
        return self.x1 <= b.x1 and b.x2 <= self.x2 and self.y1 <= b.y1 and b.y2 <= self.y2

    def larger_than(self, w: int, h: int) -> bool:
        return w <= self.w and h <= self.h


def query(res: list) -> Tuple[int, int]:
    """結果を出力しそれに対応した横/縦幅を返す"""
    print(len(res))
    for p, r, d, b in res:
        print(p, r, d, b, flush=True)
    # w, h = map(int, input().split())
    w, h = 1, 1
    return w, h

def solve() -> None:
    """解答
    二次元パッキング問題
    横幅を(T - 1)個設定し、各横幅で二次元パッキング問題を解決
    その中の最高スコアをT回目に提出

    横幅は最低/最高幅を決めて, その範囲でランダムに(T - 1)個生成する
    """
    N, T, sigma = map(int, input().split())
    whl = [tuple(map(int, input().split())) for _ in range(N)]

    ROOT_N = N**0.5
    width_min = int(-(-sum([min(w, h) for w, h in whl]) // ROOT_N))
    width_max = int(-(-sum([max(w, h) for w, h in whl]) // ROOT_N))

    res_list = []  # (W + H, res)
    for _ in range(1):
        width = random.randint(width_min, width_max)
        out_box = Rect(0, 0, width, INF, -1)  # 外箱: これに詰めていく
        rects: List[Rect] = []
        spaces = [out_box]

        for p, (w, h) in enumerate(whl):
            # p:自分i, r:90度回転するか(0/1), d:方向(U/L), b:基準i
            """回転方向を決定"""
            r = random.randint(0, 1)
            if r:
                w, h = h, w
            """設置場所を仮決定"""
            for i in range(len(spaces)):
                space = spaces[i]
                if space.larger_than(w, h):
                    rect = Rect(space.x1, space.y1, w, h, r, p)
                    rects.append(rect)
                    break
            new_spaces = []
            for space in spaces:
                new_spaces += space.subtract_by(rect)
            # 総当たり
            spaces = []
            for n_space in new_spaces:
                flg = False
                for m_space in new_spaces:
                    if n_space == m_space:
                        continue
                    if m_space.include(n_space):
                        flg = True
                        break
                    if not flg:
                        spaces.append(n_space)
        res = []
        d_dict = {}
        for rect in sorted(rects, key=lambda r: r.p):
            if rect.x1 in d_dict:
                b = d_dict[rect.x1]
            else:
                b = -1
            d_dict[rect.x2] = rect.p
            res.append((rect.p, rect.r, "U", b))
        W, H = query(res=res)
        res_list.append((W + H, res))
    for _ in range(T - 2):
        query([])
    ans = min(res_list)[1]
    # T回目=最終結果を出力
    print(len(ans))
    for an in ans:
        print(*an)


if __name__ == "__main__":
    solve()
