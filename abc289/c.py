n, m = map(int, input().split())
l = []
for _ in range(m):
    c = int(input())
    al = set(list(map(int, input().split())))
    l.append(al)

ans = 0
for i in range(1, 1 << m):
    s = set()
    for k in range(m):
        if (i >> k)&1 == 1:
            s = s | l[k]
    for x in range(1, n + 1):
        if x in s:
            continue
        else:
            break
    else:
        ans += 1

print(ans)
