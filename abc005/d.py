n = int(input())
# 二次元累積和
dl = [[0]*(n + 1)] + [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    l = [0]
    for d in dl[i]:
        l.append(l[-1] + d)
    dl[i] = l
for i in range(1, n + 1):
    for j in range(n + 1):
        dl[i][j] += dl[i - 1][j]
# メモ化
memo = [[0] * n for _ in range(n)]
def calc(x, y):
    if memo[x - 1][y - 1] != 0:
        return memo[x - 1][y - 1]
    res = 0
    for i in range(n - y + 1):
        for j in range(n - x + 1):
            tmp = dl[i + y][j + x] + dl[i][j] - dl[i + y][j] - dl[i][j + x]
            res = max(res, tmp)
    memo[x - 1][y - 1] = res
    return res

def f(p):
    """範囲pで最大"""
    res = 0
    for x in range(1, p + 1):
        if x > n:
            break
        for y in range(1, p + 1):
            if y > n:
                break
            if x*y <= p:
                res = max(res, calc(x, y))
    return res

q = int(input())
ans = []
for _ in range(q):
    p = int(input())
    ans.append(f(p))
print(*ans, sep="\n")