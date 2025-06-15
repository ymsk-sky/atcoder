n = int(input())
al = list(map(int, input().split()))
k = int(input())

ans = 0
for a in al:
    if a >= k:
        ans += 1
print(ans)
