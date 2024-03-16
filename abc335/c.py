n, q = map(int, input().split())
d = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
m = []
for i in range(n, 0, -1):
    m.append((i, 0))
i, j = 1, 0
ans = []
for _ in range(q):
    query = input().split()
    if query[0] == "1":
        c = query[1]
        a, b = d[c]
        i, j = i + a, j + b
        m.append((i, j))
    else:
        p = int(query[1])
        ans.append(m[-p])
for an in ans:
    print(*an)
