n = int(input())

l = [["."] * n for _ in range(n)]
for i in range(n):
    j = n - i - 1
    if i <= j:
        m = "#" if i % 2 == 0 else "."
        for y in range(i, j + 1):
            for x in range(i, j + 1):
                l[y][x] = m
for e in l:
    print(*e, sep="")
