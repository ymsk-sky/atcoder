r, c = map(int, input().split())
bl = [list(input()) for _ in range(r)]
for i in range(r):
    for j in range(c):
        b = bl[i][j]
        if b == "." or b == "#":
            continue
        bl[i][j] = "."
        power = int(b)
        for p in range(r):
            for q in range(c):
                if abs(i - p) + abs(j - q) <= power:
                    if bl[p][q] == "#":
                        bl[p][q] = "."

for l in bl:
    print(*l, sep="")
