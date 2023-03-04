from collections import deque

n, m = map(int, input().split())
edges = [set() for _ in range(n)]  # 有向辺
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].add(v)

ans = 0
for i in range(n):
    que = deque()
    for j in edges[i]:
        que.append(j)

    while que:
        j = que.popleft()
        for k in edges[j]:
            # i->j and j->k
            if k in edges[i] or k == i:
                continue
            # i->kが無い
            edges[i].add(k)
            que.append(k)
            ans += 1
print(ans)


"""
3<=n<=2000
0<=m<=2000

5 8
1 2
2 1
1 3
3 1
1 4
4 1
1 5
5 1
12
"""
