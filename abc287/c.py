n, m = map(int, input().split())
edges = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    edges[u].append(v)
    edges[v].append(u)
if n - 1 != m:
    print("No")
    exit()

e1, e2 = -1, -1
for i in range(n):
    if len(edges[i]) == 1:
        if e1 == -1:
            e1 = i
        elif e2 == -1:
            e2 = i
        else:
            print("No")
            exit()

l = [0] * n
i = e1
bef = -1
while 1:
    if len(edges[i]) > 2:
        print("No")
        exit()
    for j in edges[i]:
        if j != bef:
            bef = i
            break
