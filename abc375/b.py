n = int(input())
xyl = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)] + [[0, 0]]
ans = 0
for i in range(n + 1):
    x1, y1 = xyl[i]
    x2, y2 = xyl[i + 1]
    ans += ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print(ans)
