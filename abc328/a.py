n, x = map(int, input().split())
sl = list(map(int, input().split()))
ans = sum([s for s in sl if s <= x])
print(ans)
