n, l, r = map(int, input().split())
al = list(range(1, l)) + list(range(r, l - 1, -1)) + list(range(r + 1, n + 1))
print(*al)
