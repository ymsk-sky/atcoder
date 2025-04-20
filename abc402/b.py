from collections import deque

q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

que = deque()
for query in queries:
    if query[0] == 1:
        x = query[1]
        que.append(x)
    else:
        ans = que.popleft()
        print(ans)
