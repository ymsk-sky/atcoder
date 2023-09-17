from collections import deque

n, m = map(int, input().split())
l = [[] for _ in range(n)]
for _ in range(m):
    a, b, x, y = map(int, input().split())
    a, b = a - 1, b - 1
    l[a].append((b, x, y))
    l[b].append((a, -x, -y))

ans = [None] * n
ans[0] = (0, 0)
que = deque([0])
while que:
    crt = que.popleft()
    x, y = ans[crt]
    for nxt, u, v in l[crt]:
        if ans[nxt]:
            continue
        ans[nxt] = (x + u, y + v)
        que.append(nxt)

for an in ans:
    if an:
        print(*an)
    else:
        print("undecidable")
