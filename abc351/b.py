n = int(input())
al = [input() for _ in range(n)]
bl = [input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if al[i][j] == bl[i][j]:
            continue
        print(i + 1, j + 1)
        exit()
