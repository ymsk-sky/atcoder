n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    edges[b].append(a)
ans = -1
for i in range(n):
    if len(edges[i]) == 0:
        if ans == -1:
            ans = i + 1
        else:
            print(-1)
            exit()
print(ans)
