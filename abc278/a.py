n, k = map(int, input().split())
al = list(map(int, input().split()))
al = al[k:] + [0] * k
print(*al[:n])