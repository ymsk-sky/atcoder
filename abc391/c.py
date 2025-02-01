n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

d = {i: i for i in range(n)}
num = [1] * n
ans = 0

for query in queries:
    if query[0] == 1:
        p, h = query[1:]
        p, h = p - 1, h - 1
        bef_h = d[p]
        num[bef_h] -= 1
        if num[bef_h] == 1:
            ans -= 1
        num[h] += 1
        if num[h] == 2:
            ans += 1
        d[p] = h
    else:
        print(ans)
