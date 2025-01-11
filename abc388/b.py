n, d = map(int, input().split())
tll = [list(map(int, input().split())) for _ in range(n)]

for k in range(1, d + 1):
    ans = max([t*(l + k) for t, l in tll])
    print(ans)
