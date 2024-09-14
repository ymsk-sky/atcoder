"""
遅延セグメント木

区間和 + 区間加算
"""

class RSQ_and_RAQ:
    """1-index"""
    def __init__(self, init_vals: list) -> None:
        self.n = len(init_vals)
        self.data0 = [0] * (self.n + 1)
        self.data1 = [0] * (self.n + 1)
        # O(NlogN)かかるので初期化不要ならいらない
        for i, v in enumerate(init_vals):
            self.add(i, i + 1, v)

    def _add0(self, k: int, x: int) -> None:
        while k <= self.n:
            self.data0[k] += x
            k += k & -k

    def _add1(self, k: int, x: int) -> None:
        while k <= self.n:
            self.data1[k] += x
            k += k & -k

    def add(self, l: int, r: int, x: int) -> None:
        """半開区間[l, r)すべてにxを加算"""
        self._add0(l, -x * (l - 1))
        self._add0(r, x * (r - 1))
        self._add1(l, x)
        self._add1(r, -x)

    def _get0(self, k: int) -> int:
        s = 0
        while k:
            s += self.data0[k]
            k -= k & -k
        return s

    def _get1(self, k: int) -> int:
        s = 0
        while k:
            s += self.data1[k]
            k -= k & -k
        return s

    def query(self, l: int, r: int) -> int:
        """半開区間[l, r)の和を算出"""
        return (
            self._get1(r - 1) * (r - 1) + self._get0(r - 1)
            - self._get1(l - 1) * (l - 1) - self._get0(l - 1)
        )
