n, k = map(int, input().split())
al = list(map(int, input().split()))

ans = 1
for a in al:
    ans *= a
    if len(str(ans)) > k:
        ans = 1
print(ans)
