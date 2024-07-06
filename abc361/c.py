n, k = map(int, input().split())
al = list(map(int, input().split()))
al.sort()
ans = 10**10
for i in range(k + 1):
    ans = min(ans, al[i + (n - k) - 1] - al[i])
print(ans)
