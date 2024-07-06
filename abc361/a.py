n, k, x = map(int, input().split())
al = list(map(int, input().split()))
print(*al[:k], x, *al[k:])
