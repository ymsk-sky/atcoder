n, q = map(int, input().split())
xl = list(map(int, input().split()))

ans = []
cnt = [0] * n
for x in xl:
    if x == 0:
        m = min(cnt)
        for i in range(n):
            if cnt[i] == m:
                cnt[i] += 1
                ans.append(i + 1)
                break
    else:
        cnt[x - 1] += 1
        ans.append(x)

print(*ans)
