n, q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(q)]

al = [i + 1 for i in range(n)]
th = 0
for query in queries:
    if query[0] == 1:
        p, x = query[1:]
        al[(p - 1 + th) % n] = x
    elif query[0] == 2:
        p = query[1]
        ans = al[(p - 1 + th) % n]
        print(ans)
    else:
        k = query[1]
        th += k
        th %= n
