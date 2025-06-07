n = int(input())
al = list(map(int, input().split()))

ans = 0
for x in range(n + 1):
    cnt = 0
    for a in al:
        if a >= x:
            cnt += 1
    if cnt >= x:
        ans = max(ans, x)
print(ans)
