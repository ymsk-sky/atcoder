n = int(input())
al = list(map(int, input().split()))

d = {a: [] for a in al}
if n == 1:
    d[al[0]] = [-1, -1]
else:
    d[al[0]] = [-1, al[1]]
    d[al[-1]] = [al[-2], -1]
    for i in range(1, n - 1):
        d[al[i]] = [al[i - 1], al[i + 1]]

q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        # insert
        x, y = query[1:]
        x_bef, x_aft = d[x]
        d[x] = [x_bef, y]
        d[y] = [x, x_aft]
        if x_aft != -1:
            d[x_aft][0] = y
    else:
        # erase
        x = query[1]
        x_bef, x_aft = d[x]
        if x_bef != -1:
            d[x_bef][1] = x_aft
        if x_aft != -1:
            d[x_aft][0] = x_bef
        del d[x]
ans = []
a = min(d.items(), key=lambda e: e[1][0])[0]
while a != -1:
    ans.append(a)
    a = d[a][1]
print(*ans)
