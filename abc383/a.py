n = int(input())
tvl = [list(map(int, input().split())) for _ in range(n)]
ans = 0
bef_t = 0
for t, v in tvl:
    ans = max(0, ans - (t - bef_t))
    ans += v
    bef_t = t
print(ans)
