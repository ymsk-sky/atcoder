n, l, r = map(int, input().split())
al = list(map(int, input().split()))

ans = sum(al)

tmp = ans
ti = 0
for x in range(1, n + 1):
    a = al[x - 1]
    tmp = tmp - a + l
    if ans > tmp:
        ans = tmp
        ti = x

for i in range(ti):
    al[i] = l

tmp = ans
for y in range(n, 0, -1):
    a = al[y - 1]
    tmp = tmp - a + r
    ans = min(ans, tmp)

print(ans)
