n, k = map(int, input().split())
al = list(map(int, input().split()))
l = [a // k for a in al if a % k == 0]
l.sort()
print(*l)
