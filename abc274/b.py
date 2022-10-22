h, w = map(int, input().split())
cl = [input() for _ in range(h)]

ans = []
for j in range(w):
    a = 0
    for i in range(h):
        if cl[i][j] == "#":
            a += 1
    ans.append(a)
print(*ans)