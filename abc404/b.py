n = int(input())
sl = [input() for _ in range(n)]
tl = [input() for _ in range(n)]

ans = 1 << 60
for i in range(4):
    tmp = i
    for i in range(n):
        for j in range(n):
            tmp += sl[i][j] != tl[i][j]
    sl = list(zip(*sl[::-1]))
    ans = min(ans, tmp)
print(ans)
