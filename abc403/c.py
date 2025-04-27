n, m, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

l = [set() for _ in range(n)]
for query in queries:
    if query[0] == 1:
        x, y = query[1:]
        if isinstance(l[x - 1], set):
            l[x - 1].add(y)
    elif query[0] == 2:
        x = query[1]
        l[x - 1] = "ALL"
    else:
        x, y = query[1:]
        if isinstance(l[x - 1], str):
            ans = "Yes"
        else:
            ans = "Yes" if y in l[x - 1] else "No"
        print(ans)
