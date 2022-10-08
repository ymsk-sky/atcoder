from collections import deque

n, m  = map(int, input().split())
INF = float("inf")
ans = [[INF] * (n + 1) for _ in range(n + 1)]
ans[1][1] = 0

q = deque()
q.append([1, 1])

while q:
    i, j = q.popleft()
    for k in range(1, n + 1):
        tm = m - (i - k) ** 2
        if tm < 0:
            continue
        tmp = tm ** 0.5
        if tmp != int(tmp):
            continue
        else:
            tmp = int(tmp)
        for l in [j + tmp, j - tmp]:
            if 1 <= l <= n:
                if ans[k][l] == INF:
                    ans[k][l] = ans[i][j] + 1
                    q.append([k, l])

for i in range(1, n + 1):
    tmp = []
    for j in range(1, n + 1):
        if ans[i][j] != INF:
            tmp.append(ans[i][j])
        else:
            tmp.append(-1)
    print(*tmp)


"""
i,j と k,l について (i - k)**2 + (j - l)**2 == M となるところに移動可能
"""
