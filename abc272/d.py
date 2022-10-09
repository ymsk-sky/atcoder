from collections import deque

n, m = map(int, input().split())

"""
0<=x<=mに対してxの平方数を事前に計算
"""
hl = []
for x in range(m + 1):
    xh = x ** 0.5
    if xh.is_integer():
        hl.append([x, int(xh)])

INF = float("inf")
ans = [[INF] * (n + 1) for _ in range(n + 1)]

q = deque()
q.append([1, 1])
while q:
    i, j = q.popleft()
    for x, xh in hl:
        pass


for i in range(1, n + 1):
    tmp = []
    for j in range(1, n + 1):
        if ans[i][j] == INF:
            tmp.append(-1)
        else:
            tmp.append(ans[i][j])
    print(*tmp)
