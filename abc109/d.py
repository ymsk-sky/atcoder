h, w = map(int, input().split())
al = [list(map(int, input().split())) for _ in range(h)]

ans = []
for i in range(h):
    for j in range(w):
        if al[i][j]%2 == 0 or al[i][j] == 0:
            continue
        if i - 1 >= 0:
            if al[i - 1][j]%2 == 1:
                al[i - 1][j] += 1
                al[i][j] -= 1
                ans.append((i + 1, j + 1, i, j + 1))
                continue
        if j - 1 >= 0:
            if al[i][j - 1]%2 == 1:
                al[i][j - 1] += 1
                al[i][j] -= 1
                ans.append((i + 1, j + 1, i + 1, j))
                continue
        if j + 1 < w:
            if al[i][j + 1]%2 == 1:
                al[i][j + 1] += 1
                al[i][j] -= 1
                ans.append((i + 1, j + 1, i + 1, j + 2))
                continue
        if i + 1 < h:
            if al[i + 1][j]%2 == 1:
                al[i + 1][j] += 1
                al[i][j] -= 1
                ans.append((i + 1, j + 1, i + 2, j + 1))
                continue
        if j + 1 < w:
            al[i][j + 1] += 1
            al[i][j] -= 1
            ans.append((i + 1, j + 1, i + 1, j + 2))
            continue
        if i + 1 < h:
            al[i + 1][j] += 1
            al[i][j] -= 1
            ans.append((i + 1, j + 1, i + 2, j + 1))

print(len(ans))
for an in ans:
    print(*an)