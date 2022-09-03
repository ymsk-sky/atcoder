n, m = map(int, input().split())
al = list(map(int, input().split()))

# 1こずつの和
sec = 0
# i * Bi
ans = 0

for i in range(m):
    ans += (i + 1) * al[i]
    sec += al[i]

tmp = ans
for i in range(m, n):
    a = al[i]
    b = al[i - m]
    tmp -= sec
    sec -= b
    tmp += m * a
    sec += a
    ans = max(ans, tmp)

print(ans)
