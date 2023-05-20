n, q = map(int, input().split())
ql = [list(map(int, input().split())) for _ in range(q)]
l = [set() for _ in range(n)]
ans = n
for query in ql:
    if query[0] == 1:
        u, v = query[1:]
        u, v = u - 1, v - 1
        if len(l[u]) == 0:
            ans -= 1
        if len(l[v]) == 0:
            ans -= 1
        l[u].add(v)
        l[v].add(u)
    else:
        v = query[1] - 1
        if len(l[v]) > 0:
            ans += 1
        for u in l[v]:
            l[u].remove(v)
            if len(l[u]) == 0:
                ans += 1
        l[v].clear()
    print(ans)


"""
2<=n<=3*10**5
1<=q<=3*10**5
queryが1の操作のとき, uとvは繋がっていないことが保証
"""
