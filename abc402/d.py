n, m = map(int, input().split())
abl = [list(map(int, input().split())) for _ in range(m)]

ans = 0
l = [0] * n
for i, (a, b) in enumerate(abl):
    x = (a + b) % n
    ans += i - l[x]
    l[x] += 1
print(ans)
