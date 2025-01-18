from collections import deque

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]
th = 0
que = deque()
for query in queries:
    if query[0] == 1:
        l = query[1]
        if que:
            bef = que.pop()
            crt = (bef[1], bef[1] + l)
            que.append(bef)
            que.append(crt)
        else:
            que.append((0, l))
    elif query[0] == 2:
        head = que.popleft()
        th += head[1] - head[0]
        if len(que) == 0:
            th = 0
    else:
        k = query[1]
        crt = que[k - 1]
        ans = crt[0] - th
        print(ans)

"""
5
1 10
3 1
2
1 10
3 1
"""