n, k = map(int, input().split())
al = list(map(int, input().split()))
ans = al[-k:] + al[:n - k]
print(*ans)
