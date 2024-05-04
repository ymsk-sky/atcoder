n = int(input())
abl = [list(map(int, input().split())) for _ in range(n)]
s = sum([a for a, _ in abl])
ans = 0
for i in range(n):
    a, b = abl[i]
    tmp = s - a + b
    ans = max(ans, tmp)
print(ans)
