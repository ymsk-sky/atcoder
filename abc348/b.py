n = int(input())
xyl = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    x1, y1 = xyl[i]
    ans = -1
    d = 0
    for j in range(n):
        if i == j:
            continue
        x2, y2 = xyl[j]
        tmp = ((x2 - x1)**2 + (y2 - y1)**2)
        if tmp > d:
            d = tmp
            ans = j + 1
    print(ans)
