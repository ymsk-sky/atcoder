n, l = map(int, input().split())
al = list(map(int, input().split()))
ans = sum([1 for a in al if a >= l])
print(ans)
