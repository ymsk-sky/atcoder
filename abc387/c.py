"""解説の条件分けの通りに実装

R: n桁の数, [d1, d2, ..., dn]の数で構成
以下の状態を考える
1. x=R
2. xはn桁, 上からk桁(1<=k<=n-1)がRと一致しk+1桁目がdk+1より小さい
3. xはn桁, 上から1桁目がd1より小さい
4. xはk桁(1<=k<=n-1)


2.の条件が時間内にバグ取れず. = 解説のようにしっかり条件分けをすれば或は.
参考: https://atcoder.jp/contests/abc387/editorial/11832
"""

def snake(R: int) -> int:
    """R以下のへび数を求める
    Note:
        10未満の数はすべてへび数として扱う
    """
    dl = []
    while R:
        dl.append(R % 10)
        R //= 10
    dl = dl[::-1]  # 各桁の値[d1, d2, ..., dn]
    n = len(dl)  # 桁数
    res = 0

    # 1. x=R
    d1 = dl[0]
    for d in dl[1:]:
        if d >= d1:
            break
    else:
        res += 1

    # 2. xはn桁, 上からk桁(1<=k<=n-1)がRと一致しk+1桁目がdk+1より小さい
    for k, d in enumerate(dl[1:], start=1):
        tmp = 1
        for _ in range(n - k - 1):
            tmp *= d1
        res += min(d1, d) * tmp
        if d >= d1:
            break

    # 3. xはn桁, 上から1桁目がd1より小さい
    for head in range(1, d1):
        res += head**(n - 1)

    # 4. xはk桁(1<=k<=n-1)
    for k in range(1, n):
        for head in range(1, 10):
            res += head**(k - 1)

    return res

def solve():
    l, r = map(int, input().split())
    ans = snake(r) - snake(l - 1)
    print(ans)


if __name__ == "__main__":
    solve()
