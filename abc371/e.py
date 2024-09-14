n = int(input())
al = list(map(int, input().split()))
last = [None] * (n + 1)

data0 = [0] * (n + 1)
data1 = [0] * (n + 1)

def _add(data: list, k: int, x: int) -> None:
    while k <= n:
        data[k] += x
        k += k & -k

def add(l: int, r: int, x: int) -> None:
    _add(data0, l, -x*(l - 1))
    _add(data0, r, x*(r - 1))
    _add(data1, l, x)
    _add(data1, r, -x)

def _get(data: list, k: int) -> int:
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

def query(l: int, r: int) -> int:
    return _get(data1, r - 1) * (r - 1) + _get(data0, r - 1) - _get(data1, l - 1) * (l - 1) - _get(data0, l - 1)

ans = 0
for i in range(n, 0, -1):
    a = al[i - 1]
    if last[a] is None:
        # 初出現 = 種類数UP
        add(i, n + 1, 1)
    else:
        add(i, last[a], 1)
    q = query(1, n + 1)
    ans += q
    last[a] = i
print(ans)


"""
9
5 4 2 2 3 2 4 4 1

1 2 3 3 4 4 4 4 5
  1 2 2 3 3 3 3 4
    1 1 2 2 3 3 4
      1 2 2 3 3 4
        1 2 3 3 4
          1 2 2 3
            1 1 2
              1 2
                1
各値が最後に出現した場所を記録
それ以降は変化しない
"""
