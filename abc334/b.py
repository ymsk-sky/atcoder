a, m, l, r = map(int, input().split())
if l == r:
    print(int((r - a) % m == 0))
    exit()
M = 10**18 + 1
a, l, r = a + M, l + M, r + M
f = a % m
l, r = l - f, r - f
print(r // m - (l - 1) // m)
