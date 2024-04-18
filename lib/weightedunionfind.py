"""
参考: https://at274.hatenablog.com/entry/2018/02/03/140504

main関数は以下の解答.
https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/1/DSL_1_B
"""

class WeightedUnionFind:
    """重み付きUnionFind"""
    def __init__(self, n: int) -> None:
        """木を初期化

        Args:
            n (int): 要素数
        """
        self.n = n
        self.root = [i for i in range(n)]
        self.rank = [0] * n
        self.weight = [0] * n  # rootへの重み

    def find(self, x: int) -> int:
        """xの根を探す

        Args:
            x (int): 対象の要素

        Returns:
            int: xの根
        """
        if self.root[x] == x:
            return x
        else:
            y = self.find(self.root[x])
            self.weight[x] += self.weight[self.root[x]]
            self.root[x] = y
            return y

    def unite(self, x: int, y: int, w: int) -> None:
        """xとyを重みwで併合する

        Args:
            x (int): 要素x
            y (int): 要素y
            w (int): xとyの重み
        """
        x_root = self.find(x)
        y_root = self.find(y)
        if self.rank[x_root] < self.rank[y_root]:
            self.root[x_root] = y_root
            self.weight[x_root] = w - self.weight[x] + self.weight[y]
        else:
            self.root[y_root] = x_root
            self.weight[y_root] = -w - self.weight[y] + self.weight[x]
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1

    def same(self, x: int, y: int) -> bool:
        """xとyが同じ集合か判定する

        Args:
            x (int): 要素x
            y (int): 要素y

        Returns:
            bool: 同じ集合かの真偽値
        """
        return self.find(x) == self.find(y)

    def diff(self, x: int, y: int) -> int:
        """xとyの重みを求める. 異なる集合の場合None.

        Args:
            x (int): 要素x
            y (int): 要素y

        Returns:
            int: xとyの重み
        """
        if not self.same(x, y):
            return None
        return self.weight[x] - self.weight[y]


def main():
    n, q = map(int, input().split())
    wuf = WeightedUnionFind(n)
    queries = [list(map(int, input().split())) for _ in range(q)]
    for query in queries:
        if query[0] == 0:
            # relate
            x, y, z = query[1:]
            wuf.unite(x, y, z)
        else:
            # diff
            x, y = query[1:]
            res = wuf.diff(x, y)
            print("?" if res == None else res)


if __name__ == "__main__":
    main()


"""
5 6
0 0 2 5
0 1 2 3
1 0 1
1 1 3
0 1 4 8
1 0 4
2
?
10
"""